pipeline {
    agent any 
    environment {
        PYTHON_HOME = 'C:\\Users\\cmarcosd\\AppData\\Local\\Programs\\Python\\Python310'
    }
    stages {
        stage('Stage Prueba') {
            steps {
                bat 'echo "Hello world!"' 
            }
        }
        stage('Stage Python Version') {
            steps {
                bat """
                set PATH=%PYTHON_HOME%;%PATH%
                python --version
                """
            }
        }
        stage('Stage PIP Version') {
            steps {
                bat """
                set PATH=%PYTHON_HOME%;%PATH%
                python -m pip --version
                """
            }
        }
        stage('Stage Pytest Version') {
            steps {
                bat """
                set PATH=%PYTHON_HOME%;%PATH%
                python -m pytest --version
                """
            }
        }
        stage('Checkout') {
            steps {
                // Paso para obtener el código fuente desde el repositorio Git
                cleanWs()
                checkout scm: [$class: 'GitSCM', branches: [[name: '*/main']],userRemoteConfigs:
                [[url: 'https://github.com/cmarcosd/pruebasJenkins.git']]]
            }
        }
        stage('Run tests') {
            steps {
                // Paso para ejecutar las pruebas de pytest
                try {
                    bat """
                    set PATH=%PYTHON_HOME%;%PATH%
                    python -m pytest --junitxml=test-report.xml
                    """
                } catch (Exception e) {
                    // Capturar la excepción en caso de pruebas fallidas
                    echo "Error en las pruebas: ${e.message}"
                }
            }
        }
        stage('Publish test results') {
            steps {
                // Paso para publicar el informe JUnit XML en Jenkins
                junit 'test-report.xml'
            }
        }
    }
}
