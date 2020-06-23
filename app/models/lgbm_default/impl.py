from .. import CarbonModelBase
import lightgbm as lgb
import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, r2_score

class LGBMDefault(CarbonModelBase):

    def __preprocess(self, X):
        cat_cols = ["category-1", "category-2", "category-3", 
            "size", "made_in", "gender", "colour", 
            "brand", "fabric_type", "season"]

        X[cat_cols] = X[cat_cols].astype("category")
        X = X.drop("weight", axis=1)

        return X


    def train(self, X, y, save_to=None):
        print("Train")


    def eval(self, X, y):
        X = self.__preprocess(X)

        params = {'bagging_fraction': 1.0,
                'bagging_freq': 1,
                'boosting_type': 'gbdt',
                'colsample_bytree': 0.4,
                'lambda_l1': 0.0,
                'lambda_l2': 0.0,
                'learning_rate': 0.1,
                'max_depth': 12,
                'metric': 'rmse',
                'n_jobs': -1,
                'num_leaves': 300,
                'objective': 'regression',
                'seed': 42}
        
        kf = KFold(n_splits=5, shuffle=True)
        preds = np.zeros(len(X))
        nrounds = 5000
        early_stopping_rounds = 200

        models = []

        for fold, (trn_idx, val_idx) in enumerate(kf.split(X, y)):
            X_train, y_train = X.iloc[trn_idx], y.iloc[trn_idx]
            X_valid, y_valid = X.iloc[val_idx], y.iloc[val_idx]

            trn_data = lgb.Dataset(X_train, label=y_train)
            val_data = lgb.Dataset(X_valid, label=y_valid)

            lgb_clf = lgb.train(params,
                            trn_data,
                            nrounds,
                            valid_sets = [trn_data, val_data],
                            early_stopping_rounds = early_stopping_rounds,
                            verbose_eval = 100)

            preds[val_idx] = lgb_clf.predict(X_valid)

            models.append(lgb_clf)

        s_rmse = np.sqrt(mean_squared_error(y, preds))
        s_r2 = r2_score(y, preds)
        
        return s_r2

