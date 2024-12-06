# Este script cria uma pipeline simples de análise de dados, incluindo carregamento de dados, pré-processamento, treinamento de modelo e avaliação.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Carregar dados
path = "../data/raw/608DE39_ALL_LATEST.csv"
data = pd.read_csv(path)
data.head()
# Pré-processamento
data = data.dropna()
X = data.drop('target', axis=1)
y = data['target']

# Dividir em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliar modelo
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print('Acurácia do modelo:', accuracy)