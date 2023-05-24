# LocalStack Performance Testing

This is a quick attempt to assess the Lambda performance after migrating from the old to the new Lambda provider [Lambda Provider Behavioral Changes](https://docs.localstack.cloud/references/lambda-provider-v2/).

## Install

```bash
make install
```

## Generate Plots

```bash
make plots
```

## Collect Data

Check out [localstack](https://github.com/localstack/localstack) under `tests/integration/awslambda/test_lambda_performance.py`.

## Improvements

* Environment: Run in EC2 or dedicated Linux machine. It seems that Docker on macOS could be quite a bit slower
* Metadata: Report more metadata such as Docker version, LocalStack version and commit hash, operating system and version
* Logging: Disable verbose logs in LocalStack, in the external AWS client, in the Lambda containers
* Community vs. Pro: Compare against each other. Currently, host mode ran in community and Docker compose in Pro.
