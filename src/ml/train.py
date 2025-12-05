from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

def treinar_modelo(preprocessor, X_train, y_train):
    modelo = RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        max_depth=12
    )

    pipe = Pipeline([
        ("pre", preprocessor),
        ("rf", modelo)
    ])

    pipe.fit(X_train, y_train)

    return pipe
