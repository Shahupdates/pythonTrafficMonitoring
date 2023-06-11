import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from collaborative_filtering import CollaborativeFiltering
from content_based_filtering import ContentBasedFiltering
from hybrid_filtering import HybridFiltering

# Gather and preprocess user data
data = pd.read_csv('user_data.csv')
data = data.dropna()
data = data.drop_duplicates()
data['age_in_days'] = (pd.to_datetime('today') - pd.to_datetime(data['birth_date'])).dt.days
data['is_male'] = (data['gender'] == 'male').astype(int)
X = data[['age_in_days', 'is_male', 'product_interest']]
y = data['purchase_history']

# Implement machine learning algorithms
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
cf_model = CollaborativeFiltering()
cf_model.fit(X_train, y_train)
cb_model = ContentBasedFiltering()
cb_model.fit(X_train, y_train)
hybrid_model = HybridFiltering(cf_model, cb_model)
hybrid_model.fit(X_train, y_train)

# Develop a recommendation system
def recommend(user_data):
    recommendations = hybrid_model.predict(user_data)
    return recommendations.head(5)

# Test and evaluate the system
scores = cross_val_score(hybrid_model, X, y, cv=5)
print(f"Mean cross-validation score: {np.mean(scores)}")
