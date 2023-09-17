
from mlserver import MLServer, Settings, ModelSettings, MLModel
from mlserver.codecs import decode_args
import numpy as np
import joblib
import asyncio


class DiabetesClassifier(MLModel):
    async def load(self):
        self.model = joblib.load("models/diabetes/lr_cls_diabetes.pkl")

    @decode_args
    async def predict(self, payload: np.ndarray) -> np.ndarray:
        model_output = self.model.predict_proba(payload)
        return model_output


class DiabetesExplainer(MLModel):
    async def load(self):
        self.explainer = joblib.load("models/diabetes/lr_cls_explainer.pkl")

    @decode_args
    async def predict(self, payload: np.ndarray) -> np.ndarray:
        model_output = self.explainer.explain(payload)
        return model_output.shap_values[1]


async def main():
    settings   = Settings(debug=True)
    my_server  = MLServer(settings=settings)
    classifier = ModelSettings(name='diabetes_classifier', implementation=DiabetesClassifier)
    explainer  = ModelSettings(name='diabetes_explainer', implementation=DiabetesExplainer)
    await my_server.start(models_settings=[classifier, explainer])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
