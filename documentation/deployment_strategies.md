

# All at Once Deployments
- All at Once deployments perform an in-place deployment on all instances at the same time.
- All at Once deployments are simple and fast, however, it would lead to downtime and the
  rollback would take time in case of any issues.
# Rolling Deployments
- Elastic Beanstalk splits the environment’s EC2 instances into batches and deploys the new
  version of the application on the existing instance one batch at a time, leaving the rest
  of the instances in the environment running the old version.
- Elastic Beanstalk performs the rolling deployments as
    - When processing a batch, detaches all instances in the batch from the load balancer, deploys
      the new application version, and then reattaches the instances.
    - To avoid any connection issues when the instances are detached, connection draining can be
      enabled on the load balancer
    - After reattaching the instances in a batch to the load balancer, ELB waits until they pass
      a minimum number of health checks
    - If a batch of instances does not become healthy within the command timeout, the deployment fails.
    - If the instances are terminated from the failed deployment, Elastic Beanstalk replaces them with
      instances running the application version from the most recent successful deployment.
# Rolling with Additional Batch Deployments
- Rolling with Additional Batch deployments is helpful when you need to maintain full capacity during
  deployments.
- This deployment is similar to Rolling deployments, except they do not do an in-place deployment but
  a disposable one, launching a new batch of instances prior to taking any instances out of service
- When the deployment completes, Elastic Beanstalk terminates the additional batch of instances.
- Rolling with additional batch deployment does not impact the capacity and ensures full capacity during
  the deployment process.
# Immutable Deployments
- All at Once and Rolling deployment method updates existing instances.
- Immutable updates are performed by launching a second Auto Scaling group in the environment and the
  new version serves traffic alongside the old version until the new instances pass health checks.
- Immutable deployments can prevent issues caused by partially completed rolling deployments. If the new
  instances don’t pass health checks, Elastic Beanstalk terminates them, leaving the original instances
  untouched.
# Blue Green Deployments
- Elastic Beanstalk enables the Blue Green deployment through the Swap Environment URLs feature.
- Blue Green deployment provides an almost zero downtime solution, where a new version is deployed to a
  separate environment, and then CNAMEs of the two environments are swapped to redirect traffic to the
    new version.
- Blue/green deployments require that the environment runs independently of the production database i.e.
  not maintained by Elastic Beanstalk if your application uses one. Because if the environment has an
  RDS DB instance attached to it, the data will not transfer over to the second environment and will be
  lost if the original environment is terminated