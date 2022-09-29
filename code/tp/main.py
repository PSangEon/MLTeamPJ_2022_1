from sklearn.preprocessing import StandardScaler, Binarizer
import joblib 
import numpy as np
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

Name="홍길동"
Pregnancies = 0
Glucose=0
BloodPressure=0 
SkinThickness=0
Insulin=0 
BMI=0 
DiabetesPedigreeFunction=0 
Age=0
file_name = "./data.pkl"

mainUIform_class = uic.loadUiType("mainUI.ui")[0]
class mainUIWindowClass(QMainWindow, mainUIform_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_event)
        self.NamelineEdit.setText(Name)
        self.PregnancieslineEdit.setText(str(Pregnancies)) 
        self.GlucoselineEdit.setText(str(Glucose))
        self.BloodPressurelineEdit.setText(str(BloodPressure))
        self.SkinThicknesslineEdit.setText(str(SkinThickness))
        self.InsulinlineEdit.setText(str(Insulin))
        self.BMIlineEdit.setText(str(BMI))
        self.DiabetesPedigreeFunctionlineEdit.setText(str(DiabetesPedigreeFunction))
        self.AgelineEdit.setText(str(Age))
    def button_event(self):
        global Name
        global Pregnancies
        global Glucose
        global BloodPressure
        global SkinThickness
        global Insulin
        global BMI
        global DiabetesPedigreeFunction
        global Age
        Name=self.NamelineEdit.text() # line_edit text 값 가져오기
        Pregnancies = self.PregnancieslineEdit.text() # line_edit text 값 가져오기
        Glucose = self.GlucoselineEdit.text()
        BloodPressure=self.BloodPressurelineEdit.text()
        SkinThickness=self.SkinThicknesslineEdit.text()
        Insulin=self.InsulinlineEdit.text()
        BMI=self.BMIlineEdit.text()
        DiabetesPedigreeFunction=self.DiabetesPedigreeFunctionlineEdit.text()
        Age=self.AgelineEdit.text()
        obj = joblib.load(file_name)
        resultWindowClass(self)

class resultWindowClass(QDialog):
    def __init__(self, parent):  #부모 window 설정        
        super(resultWindowClass, self).__init__(parent)        
        option_ui = "result.ui"        
        uic.loadUi(option_ui, self)
        obj = joblib.load(file_name)
        result=obj(ML())
        if(int(result[1])==1):
            self.resultlabel_2.setText("위험")
            self.resultlabel_2.setStyleSheet("Color : red")
        else:
            self.resultlabel_2.setText("안전")
        self.Namelabel_2.setText(str(Name))
        self.Pregnancieslabel_2.setText(str(Pregnancies))
        self.Glucoselabel_2.setText(str(Glucose))
        self.BloodPressurelabel_2.setText(str(BloodPressure))
        self.SkinThicknesslabel_2.setText(str(SkinThickness))
        self.Insulinlabel_2.setText(str(Insulin))
        self.BMIlabel_2.setText(str(BMI))
        self.DiabetesPedigreeFunctionlabel_2.setText(str(DiabetesPedigreeFunction))
        self.Agelabel_2.setText(str(Age))
        self.show()
        
def main():
    # pickled binary file 형태로 저장된 객체를 로딩한다  
    app = QApplication(sys.argv)
    Window = mainUIWindowClass()
    Window.show()
    app.exec_()

def ML():
    Jack = np.array([3.845052,120.894531,69.105469,20.536458,79.799479,31.992578,0.471876,33.240885])
    inputdata = np.array([float(Pregnancies),float(Glucose),float(BloodPressure),float(SkinThickness),float(Insulin),float(BMI),float(DiabetesPedigreeFunction),float(Age)])
    #Pregnancies: 임신 횟수 Glucose: 포도당 부하 검사 수치 BloodPressure: 혈압(mm Hg) 
    #SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm) Insulin: 혈청 인슐린(mu U/ml)
    #BMI: 체질량지수(체중(kg)/키(m))^2 DiabetesPedigreeFunction: 당뇨 내력 가중치 값 Age: 나이
    sample_passengers = np.array([Jack,inputdata])
    scaler = StandardScaler()
    scaler_sample = scaler.fit_transform(sample_passengers)
    return scaler_sample

if __name__ == "__main__":
	main()