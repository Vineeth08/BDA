def main():
    return 'Container is up & running'


@app.route('/SimpleLinearRegression/Train')
def train():
    # Step 1 :: Prepossess the data
    # Reading the dataset
    print("Reading the Dataset")
    dataset = pd.read_csv('car.csv')
    print("Dataset contains {0} records".format(dataset.count()))

    # Extracting height(independent variable) and weight(dependent variable)
    # from dataset
    print("Extracting weight and MPG from the dataset")
    weight = dataset.iloc[:, :-1].values
    MPG = dataset.iloc[:, -1].values

    # Splitting dataset for training and testing purposes
    print("Splitting dataset for training and testing purposes")
    from sklearn.model_selection import train_test_split
    weight_train, weight_test, MPG_train, MPG_test = train_test_split(weight, MPG, test_size=1 / 3,
                                                                            random_state=0)
    print("Training dataset contains {0} records".format(len(weight_train)))
    print("Test dataset contains {0} records".format(len(weight_test)))

    # Step 2 :: Training model on training set
    print("Fitting linear regression model to dataset")
    from sklearn.linear_model import LinearRegression
    linear_regression = LinearRegression()
    linear_regression.fit(X=weight_train, y=MPG_train)

    with open("linear_regression.pickle","wb") as pickle_out:
        pickle.dump(linear_regression, pickle_out)

    return "Train Successfully"


@app.route('/SimpleLinearRegression/Predict')
def predict():

    weight = request.args.get('weight')
    _input = np.array([weight], dtype=float).reshape(-1, 1)

    with open("linear_regression.pickle", "rb") as pickle_in:
        linear_regression = pickle.load(pickle_in)
        result = linear_regression.predict(_input)
        return "The predict MPG against weight {0} is {1}".format(weight, round(result[0], 2))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
