from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import joblib

 # 샘플 데이터 생성 및 모델 학습
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
model = LinearRegression()
model.fit(X, y)
 # 모델 저장
joblib.dump(model, 'linear_model.pkl')
print("Model saved successfully.")


