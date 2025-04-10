from sklearn.linear_model import LinearRegression

# Sample labeled data
X_train = [[70, 80], [90, 95], [65, 75], [85, 90]]  # Input features (face match %, fingerprint match %)
y_train = [75, 92, 70, 88]  # Output labels (match %)

# Define the weights for face match and fingerprint match percentages
face_weight = 0.5
fingerprint_weight = 2

# Apply the weights to the training data
weighted_X_train = [[face_weight * face, fingerprint_weight * fingerprint] for face, fingerprint in X_train]

# Train the regression model
model = LinearRegression()
model.fit(weighted_X_train, y_train)

# Input the face match percentage and fingerprint match percentage for prediction
face_match = float(input("Enter face match percentage: "))
fingerprint_match = float(input("Enter fingerprint match percentage: "))

# Apply the weights to the input data
weighted_X_test = [[face_weight * face_match, fingerprint_weight * fingerprint_match]]

# Predict the match percentage
predicted_match_percentage = model.predict(weighted_X_test)

# Define the threshold for considering the user genuine
threshold = 85

# Make the prediction
prediction = predicted_match_percentage >= threshold

# Print the prediction
if prediction:
    print("Genuine User")
else:
    print("False User")

