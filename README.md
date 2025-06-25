# GODML – Governed, Observable & Declarative Machine Learning

> **GODML** es un framework de MLOps que unifica la gobernanza, la observabilidad y la implementación declarativa de modelos de Machine Learning en producción. Diseñado para empresas que no solo quieren que su modelo funcione, sino también *entender por qué funciona, cuándo dejará de hacerlo y cómo mantener el control*.

---

## 📌 Índice

1. [Visión General](#visión-general)
2. [Problemas que Resuelve](#problemas-que-resuelve)
3. [Arquitectura del Framework](#arquitectura-del-framework)
4. [Casos de Uso Típicos](#casos-de-uso-típicos)
5. [Componentes Principales](#componentes-principales)
6. [Cómo Empezar](#cómo-empezar)
7. [Roadmap](#roadmap)
8. [Licencia](#licencia)

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
           ┌────────────────────────────┐
           │    Declarative ML Layer    │
           │ YAMLs | Infra as Code | CI │
           └────────────────────────────┘



🔁 Integración con:
- Step Functions / Vertex Pipelines
- Terraform / CDK / Pulumi
- MLflow, SageMaker, Bedrock, Vertex AI
- Prometheus, CloudWatch, Grafana, Datadog

---

## 🧪 Casos de Uso Típicos

- Auditoría completa de un modelo de predicción de churn bancario.
- Pipeline de ML en salud con cumplimiento normativo (HIPAA).
- Sistema de recomendaciones con detección automática de drift.
- Automatización de retraining cuando el MSE excede umbral.

---

## 🧩 Componentes Principales

| Componente          | Descripción                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `godml-core`        | API principal para definir y versionar modelos declarativamente             |
| `godml-observe`     | Módulo de observabilidad (integración con Prometheus, CloudWatch, etc.)     |
| `godml-governance`  | Trazabilidad, metadata, reglas de cumplimiento y validación de pipelines     |
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
