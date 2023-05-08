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
        stage('Stage PIP') {
            steps {
                bat """
                set PATH=%PYTHON_HOME%;%PATH%
                python --version
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
                bat 'pytest .\test_calculator.py'
            }
        }
    }
}
