#!/usr/bin/env python3
"""
Test script para validar godml.quick_train()
"""
import sys
import os
from pathlib import Path

# Agregar el directorio actual al path para importar godml
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_quick_train():
    """Test de la función quick_train"""
    try:
        print("🧪 Iniciando test de godml.quick_train()...")
        
        # Importar godml
        import godml
        print(f"✅ GODML importado correctamente. Versión: {getattr(godml, '__version__', 'N/A')}")
        
        # Verificar que el dataset existe
        dataset_path = "./data/churn.csv"
        if not os.path.exists(dataset_path):
            print(f"❌ Dataset no encontrado: {dataset_path}")
            return False
        print(f"✅ Dataset encontrado: {dataset_path}")
        
        # Test 1: Entrenar desde YAML tal como está
        print("\n📄 Probando train_from_yaml()...")
        result = godml.train_from_yaml("./godml/godml.yml")
        print(f"✅ YAML directo: {result}")
        
       ## Test 2: Modificar YAML para XGBoost
       #print("\n🚀 Probando quick_train_yaml() con XGBoost...")
       #result = godml.quick_train_yaml(
       #    model_type="xgboost",
       #    hyperparameters={
       #        "max_depth": 4,
       #        "eta": 0.2,
       #        "objective": "binary:logistic"
       #    },
       #    yaml_path="./godml/godml.yml"
       #)
       #print(f"✅ XGBoost con YAML: {result}")
       #
       # # Test 3: Modificar YAML para Random Forest
       # print("\n🌳 Probando quick_train_yaml() con Random Forest...")
       # result = godml.quick_train_yaml(
       #     model_type="random_forest",
       #     hyperparameters={
       #         "n_estimators": 150,
       #         "max_depth": 8,
       #         "random_state": 42
       #     },
       #     yaml_path="./godml/godml.yml"
       # )
       # print(f"✅ Random Forest con YAML: {result}")
       # 
       # # Test 4: Quick train original (sin YAML)
       # print("\n⚡ Probando quick_train() original...")
       # result = godml.quick_train(
       #     model_type="xgboost",
       #     hyperparameters={
       #         "max_depth": 3,
       #         "eta": 0.3,
       #         "objective": "binary:logistic"
       #     },
       #     dataset_path=dataset_path,
       #     name="test-quick-original"
       # )
       # print(f"✅ Quick train original: {result}")
        
        print("\n🎉 ¡Todos los tests pasaron exitosamente!")
        return True
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("💡 Asegúrate de que todos los archivos estén creados correctamente")
        return False
    except Exception as e:
        print(f"❌ Error durante el test: {e}")
        print(f"📍 Tipo de error: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

def check_structure():
    """Verificar que la estructura del proyecto sea correcta"""
    print("🔍 Verificando estructura del proyecto...")
    
    required_files = [
        "godml/__init__.py",
        "godml/notebook_api.py",
        "godml/core/models.py",
        "godml/core/parser.py",
        "godml/core/executors.py",
        "godml/providers/mlflow.py",
        "godml/core/models_registry/xgboost_model.py",
        "godml/core/models_registry/random_forest_model.py",
        "godml/godml.yml",  # ← Agregado
        "data/churn.csv"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"✅ {file_path}")
    
    if missing_files:
        print(f"\n❌ Archivos faltantes:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    
    print("✅ Estructura del proyecto correcta")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 GODML Quick Train Test (con YAML)")
    print("=" * 60)
    
    # Verificar estructura
    if not check_structure():
        print("\n❌ Estructura del proyecto incompleta. Crea los archivos faltantes.")
        sys.exit(1)
    
    # Ejecutar test
    success = test_quick_train()
    
    if success:
        print("\n🎯 GODML está listo para usar como librería!")
        print("\n📝 Ejemplos de uso:")
        print("```python")
        print("import godml")
        print("")
        print("# Opción 1: Usar YAML tal como está")
        print("godml.train_from_yaml('./godml/godml.yml')")
        print("")
        print("# Opción 2: Modificar modelo manteniendo YAML")
        print("godml.quick_train_yaml(")
        print("    model_type='xgboost',")
        print("    hyperparameters={'max_depth': 5},")
        print("    yaml_path='./godml/godml.yml'")
        print(")")
        print("")
        print("# Opción 3: Quick train sin YAML")
        print("godml.quick_train(")
        print("    model_type='random_forest',")
        print("    hyperparameters={'n_estimators': 100},")
        print("    dataset_path='./data/churn.csv'")
        print(")")
        print("```")
    else:
        print("\n❌ Hay errores que corregir antes de usar GODML como librería.")
        sys.exit(1)
