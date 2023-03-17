#import pandas as pd 
import numpy as np 
import pickle
import json
#import sklearn

class diamond_prediction():
    def __init__(self,data):
        self.data = data

    def loading_files(self):

        with open(r'artifacts/diamond_model.pkl','rb') as file :
            self.model = pickle.load(file)

        with open(r'artifacts/diamond_scale.pkl','rb') as file :
            self.scaler = pickle.load(file)

        with open(r'artifacts/project_data.json','r') as file :
            self.project_data = json.load(file)

    def price_prediction(self):

        self.loading_files()

        carat = self.data['html_carat']
        color = self.data['html_color']
        cut = self.data['html_cut']
        clarity = self.data['html_clarity']
        depth = self.data['html_depth']
        table = self.data['html_table']
        x = self.data['html_x']
        y = self.data['html_y']
        z = self.data['html_z']

        user_data = np.zeros(len(self.project_data['column_names']))

        user_data[0]=carat
        #cut
        user_data[1]=self.project_data['cut'][cut]

        #clarity
        user_data[2]=self.project_data['clarity'][clarity]

        user_data[3]=depth
        user_data[4]=table
        user_data[5]=x
        user_data[6]=y
        user_data[7]=z

        #color
        search_color='color_'+color ##(color_E)
        index=np.where(self.project_data['column_names']==search_color)
        user_data[index]=1

        ## prediction
        scale=self.scaler.transform([user_data])
        result = self.model.predict(scale)[0]
        return result


