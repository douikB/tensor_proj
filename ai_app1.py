from sklearn.datasets import make_regression
import joblib

 # 샘플 데이터 생성 및 모델 학습
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

load_model = joblib.load('linear_model.pkl')
print('load_ok!')

y_pred = load_model.predict(X)
print(y_pred)