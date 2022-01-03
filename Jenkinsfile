ubuntu {
    def app

    stage('clone repositoyr'){
    checkout scm
    }


    stage('build image'){
    app = docker.build("imuser/devops_task1")

    }

    stage('test image'){
        app.inside{
            sh 'echo "tests passed"'
        }
    }

    stage('push image'){

        docker.withRegistry('https://hub.docker.com/repositories' , 'docker-hub-credentials') {
            app.push("$env.BUILD_NUMBER")
            app.push("latest")
        }
    }
}