import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.dates as dates

#mySEIR = SEIR(df)
#mySEIR.predict("data", ["totale_casi","totale_ospedalizzati","deceduti","ricoverati_con_sintomi"])
#mySEIR.plot()
class SEIR:
    def __init__(self, df):
        self.df = df
    def predict(self, datetimeCol, valueCols):
        self.valueCols = valueCols
        self.X = {}
        self.y = {}
        self.X_pred = {}
        self.y_pred = {}
        self.dailyCoeff = {}
        # two column: datetime [datetime64[ns]], value [int64]
        for valueCol in self.valueCols:
            # Delete <=0 values (because of log)
            df = self.df[self.df[valueCol]>0].copy()
            df = df.groupby([datetimeCol]).agg({valueCol:"sum"}).reset_index()
            df["yLog"] = np.log(df[valueCol])
            # Extract time
            self.X[valueCol] = df[[datetimeCol]]
            # Convert to int
            X_int = self.X[valueCol].copy().astype(int)
            ## for backwards conversion to datetime: pd.to_datetime(X[datetimeCol].astype(int))
            self.y[valueCol] = df[valueCol]
            y_log = df["yLog"]
            # Create model
            regressor = LinearRegression()
            model = regressor.fit(X_int, y_log)
            r_sq = model.score(X_int, y_log)
            coeff = regressor.coef_[0]
            # Factor of daily evolution
            self.dailyCoeff[valueCol] = round(10**(3600*24*(10**9)*regressor.coef_[0]), 1)
            print(self.dailyCoeff[valueCol])
            #print('intercept:', model.intercept_)
            #print('slope:', model.coef_[0])

            # Generate prediction: regressor.predict(convertedX)
            self.X_pred[valueCol] = pd.DataFrame([
                self.X[valueCol].min(), 
                self.X[valueCol].min() + pd.Timedelta(1, unit='d'), 
                self.X[valueCol].max() + pd.Timedelta(14, unit='d')])
            self.y_pred[valueCol] = np.exp(regressor.predict(self.X_pred[valueCol].astype(int)))
    def plot(self):
        # Plot result
        fig, ax = plt.subplots(ncols=1, nrows=1)
        ax.set_yscale("log")
        #ax.set_ylim(1,10000)

        ax.grid(True, which="minor", axis="y", color='g', linestyle='--', linewidth=1)
        ax.grid(True, which="major", axis="y", color='g', linestyle='-', linewidth=2)

        ax.xaxis.set_minor_locator(dates.DayLocator(bymonthday=range(1,32), interval=1))
        ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
        ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))
        ax.xaxis.set_major_formatter(dates.DateFormatter('\n%m-%d'))
        ax.grid(True, which="major", axis="x", color='g', linestyle='-', linewidth=2)
        fig.set_size_inches(20,10)
        for valueCol in self.valueCols:
            plotDf = pd.DataFrame(self.X[valueCol])
            plotDf["y"]=self.y[valueCol]
            plotDf.columns = ["date","y"]
            plotDf.plot(x="date", y="y", ax=ax, style="o:", label="act "+valueCol)

            plotDf_pred = pd.DataFrame(self.X_pred[valueCol])
            plotDf_pred["y"]=self.y_pred[valueCol]
            plotDf_pred.columns = ["date","y"]
            plotDf_pred.plot(x="date", y="y", ax=ax, style="--", label="pred "+valueCol)
        plt.title('prediction')
        plt.xlabel('datetime')
        plt.ylabel('yLabel')
        plt.show()