from sklearn.datasets import make_regression
import pickle

 # 샘플 데이터 생성 및 모델 학습
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)


with open('linear_model2.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

print("Model loaded successfully.")

y_pred = loaded_model.predict(X)
print(y_pred)