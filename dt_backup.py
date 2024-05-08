import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

data = pd.read_csv('cleaned_data.csv')

# Impute missing values, for example with the median for numerical data
imputer = SimpleImputer(strategy='median')
data['User-Age'] = imputer.fit_transform(data[['User-Age']])

# Encode categorical variables using LabelEncoder or OneHotEncoder
label_encoder = LabelEncoder()
for column in ['User-City', 'User-State', 'User-Country', 'Book-Author', 'Book-Publisher', 'Series-Title']:
    data[column] = label_encoder.fit_transform(data[column])

# Prepare features and labels
X = data.drop(columns=['User-ID', 'ISBN', 'Book-Title', 'Genre'])
y = label_encoder.fit_transform(data['Genre'])  # Encoding the target variable

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier

# Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42, max_depth=8, min_samples_split=100, min_samples_leaf=500)
clf.fit(X_train, y_train)


from sklearn.metrics import accuracy_score, classification_report

# Predict the labels for the test set
y_pred = clf.predict(X_test, )

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# More detailed performance analysis
print(classification_report(y_test, y_pred, zero_division=0))


from sklearn import tree
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(60, 30))


plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

tree.plot_tree(
    clf,
    filled=True,
    feature_names=X.columns,
    class_names=label_encoder.classes_,
    fontsize=8,
    ax=ax
)

# 保存并展示图像
plt.savefig('adjusted_decision_tree_no_param_change.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
