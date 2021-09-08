pipeline {
    agent any
    environment {
        TOKENDISCCORD1 = credentials('discord-token')
    }
    stages {
        stage('clean') {
            steps {
                echo 'clean'
            }
        }
        stage('Build') {
            steps {
                dir('home'){
                    echo 'build'
                }
            }
        }
    }
}
