```bash

helm package . -d docs/

helm repo index docs --url https://mindmug2018-oss.github.io/helm-microservice/


[user1@master step24_microservice_helm]$ helm package . -d docs/
Successfully packaged chart and saved it to: docs/msa-platform-0.1.0.tgz

[user1@master step24_microservice_helm]$ helm repo index docs --url https://mindmug2018-oss.github.io/helm-microservice/

[user1@master step24_microservice_helm]$ git add .

[user1@master step24_microservice_helm]$ git commit -m "docs folder added"
[master 9e0c01b] docs folder added
 3 files changed, 36 insertions(+)
 create mode 100644 docs/index.yaml
 create mode 100644 docs/msa-platform-0.1.0.tgz
 create mode 100644 memo.md

[user1@master step24_microservice_helm]$ git push origin master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 22.24 KiB | 22.24 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:mindmug2018-oss/helm-microservice.git
   40d6019..9e0c01b  master -> master

[user1@master step24_microservice_helm]$ helm repo ls
NAME                    URL                                               
cnpg                    https://cloudnative-pg.github.io/charts           
argo                    https://argoproj.github.io/argo-helm              
my-repo                 https://mindmug2018-oss.github.io/my-helm-chart/  
prometheus-community    https://prometheus-community.github.io/helm-charts

[user1@master step24_microservice_helm]$ helm repo add msa https://mindmug2018-oss.github.io/helm-microservice/
"msa" has been added to your repositories

[user1@master step24_microservice_helm]$ helm repo ls
NAME                    URL                                                 
cnpg                    https://cloudnative-pg.github.io/charts             
argo                    https://argoproj.github.io/argo-helm                
my-repo                 https://mindmug2018-oss.github.io/my-helm-chart/    
prometheus-community    https://prometheus-community.github.io/helm-charts  
msa                     https://mindmug2018-oss.github.io/helm-microservice/

[user1@master step24_microservice_helm]$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "msa" chart repository
...Unable to get an update from the "cnpg" chart repository (https://cloudnative-pg.github.io/charts):
        Get "https://cloudnative-pg.io/charts/index.yaml": tls: failed to verify certificate: x509: certificate has expired or is not yet valid: current time 2026-06-27T19:17:56+09:00 is before 2026-06-28T02:19:53Z
...Successfully got an update from the "my-repo" chart repository
...Successfully got an update from the "argo" chart repository
...Successfully got an update from the "prometheus-community" chart repository
Update Complete. ⎈Happy Helming!⎈

[user1@master step24_microservice_helm]$ helm search repo msa
NAME                    CHART VERSION   APP VERSION     DESCRIPTION          
msa/msa-platform        0.1.0           1.0.0           index + market + post

[user1@master step24_microservice_helm]$ helm install msa-release msa/msa-platform -n msa --create-namespace
NAME: msa-release
LAST DEPLOYED: Sat Jun 27 19:21:38 2026
NAMESPACE: msa
STATUS: deployed
REVISION: 1
TEST SUITE: None

[user1@master step24_microservice_helm]$ k get pod,svc -n msa
NAME                             READY   STATUS    RESTARTS   AGE
pod/index-app-6bdf6db4d6-vzzd9   1/1     Running   0          48s
pod/index-app-6bdf6db4d6-xqxs7   1/1     Running   0          48s

NAME                    TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
service/svc-index-app   ClusterIP   10.97.31.18   <none>        80/TCP    48s



```