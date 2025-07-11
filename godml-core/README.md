# GODML – Governed, Observable & Declarative Machine Learning

godml-core/
├── godml/
│   ├── __init__.py
|   ├── godml_cli.py
|   ├── godml.yml
│   ├── core/
|   |   ├── executors.py
│   │   ├── parser.py            # Carga y validación de YAMLs
│   │   ├── models.py            # Esquemas internos (dataclasses / Pydantic)
│   │   ├── engine.py            # Orquestador local de ejecución (base class)
│   │   └── validators.py        # Reglas de gobernanza y validaciones
│   ├── providers/
|   |   ├── mlflow.py
│   │   ├── __init__.py
│   │   ├── sagemaker.py         # Implementación provider AWS
│   │   └── vertex.py            # Implementación provider GCP
│   └── utils/
│       ├── logger.py            # Logger estructurado
│       └── hash.py              # Hash para datasets y modelos
├── pyproject.toml               # Configuración de build
├── README.md                    # Docs internas del core
└── tests/
    └── test_parser.py


> **GODML** es un framework de MLOps que unifica la gobernanza, la observabilidad y la implementación declarativa de modelos de Machine Learning en producción. Diseñado para que no solo quieren que su modelo funcione, sino también *entender por qué funciona, cuándo dejará de hacerlo y cómo mantener el control*.

---

## 📌 Índice

1. [Visión General](#visión-general)
2. [Problemas que Resuelve](#problemas-que-resuelve)
3. [Arquitectura del Framework](#arquitectura-del-framework)
4. [Casos de Uso Típicos](#casos-de-uso-típicos)
5. [Componentes Principales](#componentes-principales)
6. [Cómo Empezar](#cómo-empezar)
7. [Roadmap](#roadmap)
#8. [Licencia](#licencia)

---

## 🎯 Visión General

GODML nace como respuesta a una realidad que muchas empresas enfrentan hoy:

- Modelos en producción sin trazabilidad.
- Decisiones de IA que no se pueden explicar.
- Retrainings manuales sin control de versiones ni validaciones.
- Observabilidad fragmentada y pobre integración con herramientas de DevOps.

GODML propone una solución estructurada, modular y *cloud-native* que permite escalar proyectos de ML sin perder gobernanza, transparencia ni capacidad de auditoría.

---

## ❗ Problemas que Resuelve

- 🔍 **¿Quién entrenó este modelo?** → Metadata con versionado y tracking automático.
- 📦 **¿Qué datos usó?** → Trazabilidad completa de datasets (con hashes y linaje).
- 🧠 **¿Por qué está tomando esta decisión?** → Explicabilidad integrada.
- 📊 **¿Está cumpliendo normativas (GDPR, HIPAA, etc.)?** → Logging estructurado y cumplimiento por diseño.
- 🛠️ **¿Qué pasa cuando el modelo degrada?** → Monitoreo de métricas + triggers automáticos para retraining o alertas.

---

## 🧱 Arquitectura del Framework

GODML se compone de **3 capas principales**, pensadas para desplegarse en AWS, GCP o entornos híbridos:

           ┌────────────────────────────┐
           │     Observabilidad         │
           │ Logs | Métricas | Tracing  │
           └────────────────────────────┘
                       ▲
                       │
           ┌────────────────────────────┐
           │      Orquestación          │
           │ DAGs | Pipelines | Events  │
           └────────────────────────────┘
                       ▲
                       │
           ┌─────────────────────────────┐
           │    Declarative ML Layer     │
           │ YAMLs | Infra as Code | CLI │
           └─────────────────────────────┘


🔁 Integración con:
- Step Functions / Vertex Pipelines
- Terraform / CDK / CloudFormation
- MLflow, SageMaker, Vertex AI
- CloudWatch, Grafana

---

## 🧪 Casos de Uso Típicos

- Auditoría completa de un modelo de predicción.
- Pipeline de ML en salud con cumplimiento normativo (HIPAA).
- Sistema de recomendaciones con detección automática de drift.
- Automatización de retraining cuando el MSE excede umbral.

---

## 🧩 Componentes Principales

| Componente          | Descripción                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `godml-core`        | API principal para definir y versionar modelos declarativamente             |
| `godml-observe`     | Módulo de observabilidad (integración con Prometheus, CloudWatch, etc.)     |
| `godml-governance`  | Trazabilidad, metadata, reglas de cumplimiento y validación de pipelines    |
| `godml-cli`         | Interfaz de línea de comandos para bootstrap, validación y despliegue       |

---

## 🚀 Cómo Empezar

```bash
# 1. Instala el CLI
pip install godml

# 2. Inicializa un proyecto
godml init my-churn-project

# 3. Declara tu pipeline
vim godml.yml

# 4. Despliega
godml deploy --env=staging



source venv/Scripts/activate

pip install -r requirements.txt

python -m godml.godml_cli run --file "godml/godml.yml"


mlflow ui --backend-store-uri ./mlruns

---



model:
  type: random_forest
  hyperparameters:
    n_estimators: 100
    max_depth: 5
    max_features: sqrt
    random_state: 42

model:
  type: xgboost  # ✅ esto debe coincidir con el nombre del archivo: xgboost_model.py
  hyperparameters:
    eta: 0.3
    max_depth: 5
    objective: binary:logistic
    eval_metric: logloss
    random_state: 42


modificacion de pyproject y requirements

pip install build
python -m build

# Verificar que el comando está disponible
godml --help

pip install godml-0.1.0-py3-none-any.whl
godml init test-project
cd test-project
python -m godml.godml_cli run --file "godml/godml.yml"
godml run -f godml.yml



pip uninstall godml -y
pip uninstall -y -r requirements.txt


✅ **Próximos pasos recomendados:**
- Agregar badges (versión, build passing, licencia).
- Crear ejemplos en `examples/` con YAMLs reales.
- Preparar logo o visual simple (si quieres, te genero uno tipo AWS-style).
- Agregar sección de contribución y comunidad (`CONTRIBUTING.md` + `CODE_OF_CONDUCT.md`).

#importante !!!!!
Es parte de la estructura estándar de MLOps para separar datos, código y resultados.