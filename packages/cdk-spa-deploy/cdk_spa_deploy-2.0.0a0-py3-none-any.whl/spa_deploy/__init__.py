'''
# CDK-SPA-Deploy

[![npm](https://img.shields.io/npm/dt/cdk-spa-deploy)](https://www.npmjs.com/package/cdk-spa-deploy)
[![Vulnerabilities](https://img.shields.io/snyk/vulnerabilities/npm/cdk-spa-deploy)](https://www.npmjs.com/package/cdk-spa-deploy)

This is an AWS CDK Construct to make deploying a single page website (Angular/React/Vue) to AWS S3 behind SSL/Cloudfront as easy as 5 lines of code.

## Installation and Usage

### Typescript

```console
npm install --save cdk-spa-deploy
```

As of version 103.0 this construct now declares peer dependencies rather than bundling them so you can use it with any version of CDK higher than 103.0 without waiting on me to release a new version. The downside is that you will need to install the dependencies it uses for yourself, here is a list:

```json
{
    "constructs": "^3.3.75",
    "@aws-cdk/aws-certificatemanager": "^1.103.0",
    "@aws-cdk/aws-cloudfront": "^1.103.0",
    "@aws-cdk/aws-iam": "^1.103.0",
    "@aws-cdk/aws-route53": "^1.103.0",
    "@aws-cdk/aws-route53-patterns": "^1.103.0",
    "@aws-cdk/aws-route53-targets": "^1.103.0",
    "@aws-cdk/aws-s3": "^1.103.0",
    "@aws-cdk/aws-s3-deployment": "^1.103.0",
    "@aws-cdk/core": "^1.103.0"
}
```

```python
# Example automatically generated from non-compiling source. May contain errors.
import * as cdk from '@aws-cdk/core';
import { SPADeploy } from 'cdk-spa-deploy';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new SPADeploy(this, 'spaDeploy')
      .createBasicSite({
        indexDoc: 'index.html',
        websiteFolder: '../blog/dist/blog'
      });

    new SPADeploy(this, 'cfDeploy')
      .createSiteWithCloudfront({
        indexDoc: 'index.html',
        websiteFolder: '../blog/dist/blog'
      });
  }
}
```

### Python

```console
pip install cdk-spa-deploy
```

Note As of version 103.0 this construct now declares peer dependencies rather than bundling them so you can use it with any version of CDK higher than 103.0 without waiting on me to release a new version. The downside is that you will need to install the dependencies it uses for yourself. The npm versioms are listed above.

```python
from aws_cdk import core
from spa_deploy import SPADeploy

class PythonStack(core.Stack):
  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    SPADeploy(self, 'spaDeploy').create_basic_site(
      index_doc='index.html',
      website_folder='../blog/blog/dist/blog'
    )


    SPADeploy(self, 'cfDeploy').create_site_with_cloudfront(
      index_doc='index.html',
      website_folder='../blog/blog/dist/blog'
    )
```

### Dotnet / C#

This project has now been published to nuget, more details to follow soon but you can find it [here](https://www.nuget.org/packages/CDKSPADeploy/1.80.0)

Note As of version 103.0 this construct now declares peer dependencies rather than bundling them so you can use it with any version of CDK higher than 103.0 without waiting on me to release a new version. The downside is that you will need to install the dependencies it uses for yourself. The npm versioms are listed above.

```bash
# package manager
Install-Package CDKSPADeploy -Version 1.80.0
# .NET CLI
dotnet add package CDKSPADeploy --version 1.80.0
# Package reference
<PackageReference Include="CDKSPADeploy" Version="1.80.0" />
# Paket CLI
paket add CDKSPADeploy --version 1.80.0
```

### Java

A version has now been published to maven.

Note As of version 103.0 this construct now declares peer dependencies rather than bundling them so you can use it with any version of CDK higher than 103.0 without waiting on me to release a new version. The downside is that you will need to install the dependencies it uses for yourself. The npm versioms are listed above.

```xml
<dependency>
  <groupId>com.cdkpatterns</groupId>
  <artifactId>CDKSPADeploy</artifactId>
  <version>1.81.0</version>
</dependency>
```

## Advanced Usage

### Auto Deploy From Hosted Zone Name

If you purchased your domain through route 53 and already have a hosted zone then just use the name to deploy your site behind cloudfront. This handles the SSL cert and everything for you.

```python
# Example automatically generated from non-compiling source. May contain errors.
new SPADeploy(this, 'spaDeploy', { encryptBucket: true })
  .createSiteFromHostedZone({
    zoneName: 'cdkpatterns.com',
    indexDoc: 'index.html',
    websiteFolder: '../website/dist/website'
  });
```

### Custom Domain and SSL Certificates

You can also pass the ARN for an SSL certification and your alias routes to cloudfront

```python
# Example automatically generated from non-compiling source. May contain errors.
import cdk = require('@aws-cdk/core');
import { SPADeploy } from 'cdk-spa-deploy';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new SPADeploy(this, 'cfDeploy')
      .createSiteWithCloudfront({
        indexDoc: '../blog/dist/blog',
        certificateARN: 'arn:...',
        cfAliases: ['www.alias.com']
      });
  }
}
```

### Encrypted S3 Bucket

Pass in one boolean to tell SPA Deploy to encrypt your website bucket

```python
# Example automatically generated from non-compiling source. May contain errors.
new SPADeploy(this, 'cfDeploy', {encryptBucket: true}).createBasicSite({
    indexDoc: 'index.html',
    websiteFolder: 'website'
});
```

### Custom Origin Behaviors

Pass in an array of CloudFront Behaviors

```python
# Example automatically generated from non-compiling source. May contain errors.
new SPADeploy(this, 'cfDeploy').createSiteWithCloudfront({
  indexDoc: 'index.html',
  websiteFolder: 'website',
  cfBehaviors: [
    {
      isDefaultBehavior: true,
      allowedMethods: cf.CloudFrontAllowedMethods.ALL,
      forwardedValues: {
        queryString: true,
        cookies: { forward: 'all' },
        headers: ['*'],
      },
    },
    {
      pathPattern: '/virtual-path',
      allowedMethods: cf.CloudFrontAllowedMethods.GET_HEAD,
      cachedMethods: cf.CloudFrontAllowedCachedMethods.GET_HEAD,
    },
  ],
});
```

### Restrict Access to Known IPs

Pass in a boolean and an array of IP addresses and your site is locked down!

```python
# Example automatically generated from non-compiling source. May contain errors.
new SPADeploy(stack, 'spaDeploy', {
  encryptBucket: true,
  ipFilter: true,
  ipList: ['1.1.1.1']
}).createBasicSite({
    indexDoc: 'index.html',
    websiteFolder: 'website'
  })
```

### Modifying S3 Bucket Created in Construct

An object is now returned containing relevant artifacts created if you need to make any further modifications:

* The S3 bucket is present for all of the methods
* When a CloudFront Web distribution is created it will be present in the return object

```python
# Example automatically generated from non-compiling source. May contain errors.
export interface SPADeployment {
  readonly websiteBucket: s3.Bucket,
}

export interface SPADeploymentWithCloudFront extends SPADeployment {
  readonly distribution: CloudFrontWebDistribution,
}
```

## Issues / Feature Requests

https://github.com/nideveloper/CDK-SPA-Deploy
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_cloudfront
import aws_cdk.aws_iam
import aws_cdk.aws_s3
import constructs


@jsii.data_type(
    jsii_type="cdk-spa-deploy.HostedZoneConfig",
    jsii_struct_bases=[],
    name_mapping={
        "index_doc": "indexDoc",
        "website_folder": "websiteFolder",
        "zone_name": "zoneName",
        "cf_behaviors": "cfBehaviors",
        "error_doc": "errorDoc",
        "role": "role",
        "subdomain": "subdomain",
    },
)
class HostedZoneConfig:
    def __init__(
        self,
        *,
        index_doc: builtins.str,
        website_folder: builtins.str,
        zone_name: builtins.str,
        cf_behaviors: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.Behavior]] = None,
        error_doc: typing.Optional[builtins.str] = None,
        role: typing.Optional[aws_cdk.aws_iam.Role] = None,
        subdomain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param index_doc: -
        :param website_folder: -
        :param zone_name: -
        :param cf_behaviors: -
        :param error_doc: -
        :param role: -
        :param subdomain: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "index_doc": index_doc,
            "website_folder": website_folder,
            "zone_name": zone_name,
        }
        if cf_behaviors is not None:
            self._values["cf_behaviors"] = cf_behaviors
        if error_doc is not None:
            self._values["error_doc"] = error_doc
        if role is not None:
            self._values["role"] = role
        if subdomain is not None:
            self._values["subdomain"] = subdomain

    @builtins.property
    def index_doc(self) -> builtins.str:
        result = self._values.get("index_doc")
        assert result is not None, "Required property 'index_doc' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def website_folder(self) -> builtins.str:
        result = self._values.get("website_folder")
        assert result is not None, "Required property 'website_folder' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_name(self) -> builtins.str:
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cf_behaviors(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudfront.Behavior]]:
        result = self._values.get("cf_behaviors")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_cloudfront.Behavior]], result)

    @builtins.property
    def error_doc(self) -> typing.Optional[builtins.str]:
        result = self._values.get("error_doc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.Role]:
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.Role], result)

    @builtins.property
    def subdomain(self) -> typing.Optional[builtins.str]:
        result = self._values.get("subdomain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SPADeploy(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-spa-deploy.SPADeploy",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        encrypt_bucket: typing.Optional[builtins.bool] = None,
        ip_filter: typing.Optional[builtins.bool] = None,
        ip_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        role: typing.Optional[aws_cdk.aws_iam.Role] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param encrypt_bucket: -
        :param ip_filter: -
        :param ip_list: -
        :param role: -
        '''
        config = SPAGlobalConfig(
            encrypt_bucket=encrypt_bucket,
            ip_filter=ip_filter,
            ip_list=ip_list,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="createBasicSite")
    def create_basic_site(
        self,
        *,
        index_doc: builtins.str,
        website_folder: builtins.str,
        block_public_access: typing.Optional[aws_cdk.aws_s3.BlockPublicAccess] = None,
        certificate_arn: typing.Optional[builtins.str] = None,
        cf_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        cf_behaviors: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.Behavior]] = None,
        error_doc: typing.Optional[builtins.str] = None,
        export_website_url_name: typing.Optional[builtins.str] = None,
        export_website_url_output: typing.Optional[builtins.bool] = None,
        role: typing.Optional[aws_cdk.aws_iam.Role] = None,
        security_policy: typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol] = None,
        ssl_method: typing.Optional[aws_cdk.aws_cloudfront.SSLMethod] = None,
    ) -> "SPADeployment":
        '''Basic setup needed for a non-ssl, non vanity url, non cached s3 website.

        :param index_doc: -
        :param website_folder: -
        :param block_public_access: -
        :param certificate_arn: -
        :param cf_aliases: -
        :param cf_behaviors: -
        :param error_doc: -
        :param export_website_url_name: -
        :param export_website_url_output: -
        :param role: -
        :param security_policy: -
        :param ssl_method: -
        '''
        config = SPADeployConfig(
            index_doc=index_doc,
            website_folder=website_folder,
            block_public_access=block_public_access,
            certificate_arn=certificate_arn,
            cf_aliases=cf_aliases,
            cf_behaviors=cf_behaviors,
            error_doc=error_doc,
            export_website_url_name=export_website_url_name,
            export_website_url_output=export_website_url_output,
            role=role,
            security_policy=security_policy,
            ssl_method=ssl_method,
        )

        return typing.cast("SPADeployment", jsii.invoke(self, "createBasicSite", [config]))

    @jsii.member(jsii_name="createSiteFromHostedZone")
    def create_site_from_hosted_zone(
        self,
        *,
        index_doc: builtins.str,
        website_folder: builtins.str,
        zone_name: builtins.str,
        cf_behaviors: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.Behavior]] = None,
        error_doc: typing.Optional[builtins.str] = None,
        role: typing.Optional[aws_cdk.aws_iam.Role] = None,
        subdomain: typing.Optional[builtins.str] = None,
    ) -> "SPADeploymentWithCloudFront":
        '''S3 Deployment, cloudfront distribution, ssl cert and error forwarding auto
configured by using the details in the hosted zone provided.

        :param index_doc: -
        :param website_folder: -
        :param zone_name: -
        :param cf_behaviors: -
        :param error_doc: -
        :param role: -
        :param subdomain: -
        '''
        config = HostedZoneConfig(
            index_doc=index_doc,
            website_folder=website_folder,
            zone_name=zone_name,
            cf_behaviors=cf_behaviors,
            error_doc=error_doc,
            role=role,
            subdomain=subdomain,
        )

        return typing.cast("SPADeploymentWithCloudFront", jsii.invoke(self, "createSiteFromHostedZone", [config]))

    @jsii.member(jsii_name="createSiteWithCloudfront")
    def create_site_with_cloudfront(
        self,
        *,
        index_doc: builtins.str,
        website_folder: builtins.str,
        block_public_access: typing.Optional[aws_cdk.aws_s3.BlockPublicAccess] = None,
        certificate_arn: typing.Optional[builtins.str] = None,
        cf_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        cf_behaviors: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.Behavior]] = None,
        error_doc: typing.Optional[builtins.str] = None,
        export_website_url_name: typing.Optional[builtins.str] = None,
        export_website_url_output: typing.Optional[builtins.bool] = None,
        role: typing.Optional[aws_cdk.aws_iam.Role] = None,
        security_policy: typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol] = None,
        ssl_method: typing.Optional[aws_cdk.aws_cloudfront.SSLMethod] = None,
    ) -> "SPADeploymentWithCloudFront":
        '''This will create an s3 deployment fronted by a cloudfront distribution
It will also setup error forwarding and unauth forwarding back to indexDoc.

        :param index_doc: -
        :param website_folder: -
        :param block_public_access: -
        :param certificate_arn: -
        :param cf_aliases: -
        :param cf_behaviors: -
        :param error_doc: -
        :param export_website_url_name: -
        :param export_website_url_output: -
        :param role: -
        :param security_policy: -
        :param ssl_method: -
        '''
        config = SPADeployConfig(
            index_doc=index_doc,
            website_folder=website_folder,
            block_public_access=block_public_access,
            certificate_arn=certificate_arn,
            cf_aliases=cf_aliases,
            cf_behaviors=cf_behaviors,
            error_doc=error_doc,
            export_website_url_name=export_website_url_name,
            export_website_url_output=export_website_url_output,
            role=role,
            security_policy=security_policy,
            ssl_method=ssl_method,
        )

        return typing.cast("SPADeploymentWithCloudFront", jsii.invoke(self, "createSiteWithCloudfront", [config]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalConfig")
    def global_config(self) -> "SPAGlobalConfig":
        return typing.cast("SPAGlobalConfig", jsii.get(self, "globalConfig"))

    @global_config.setter
    def global_config(self, value: "SPAGlobalConfig") -> None:
        jsii.set(self, "globalConfig", value)


@jsii.data_type(
    jsii_type="cdk-spa-deploy.SPADeployConfig",
    jsii_struct_bases=[],
    name_mapping={
        "index_doc": "indexDoc",
        "website_folder": "websiteFolder",
        "block_public_access": "blockPublicAccess",
        "certificate_arn": "certificateARN",
        "cf_aliases": "cfAliases",
        "cf_behaviors": "cfBehaviors",
        "error_doc": "errorDoc",
        "export_website_url_name": "exportWebsiteUrlName",
        "export_website_url_output": "exportWebsiteUrlOutput",
        "role": "role",
        "security_policy": "securityPolicy",
        "ssl_method": "sslMethod",
    },
)
class SPADeployConfig:
    def __init__(
        self,
        *,
        index_doc: builtins.str,
        website_folder: builtins.str,
        block_public_access: typing.Optional[aws_cdk.aws_s3.BlockPublicAccess] = None,
        certificate_arn: typing.Optional[builtins.str] = None,
        cf_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        cf_behaviors: typing.Optional[typing.Sequence[aws_cdk.aws_cloudfront.Behavior]] = None,
        error_doc: typing.Optional[builtins.str] = None,
        export_website_url_name: typing.Optional[builtins.str] = None,
        export_website_url_output: typing.Optional[builtins.bool] = None,
        role: typing.Optional[aws_cdk.aws_iam.Role] = None,
        security_policy: typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol] = None,
        ssl_method: typing.Optional[aws_cdk.aws_cloudfront.SSLMethod] = None,
    ) -> None:
        '''
        :param index_doc: -
        :param website_folder: -
        :param block_public_access: -
        :param certificate_arn: -
        :param cf_aliases: -
        :param cf_behaviors: -
        :param error_doc: -
        :param export_website_url_name: -
        :param export_website_url_output: -
        :param role: -
        :param security_policy: -
        :param ssl_method: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "index_doc": index_doc,
            "website_folder": website_folder,
        }
        if block_public_access is not None:
            self._values["block_public_access"] = block_public_access
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if cf_aliases is not None:
            self._values["cf_aliases"] = cf_aliases
        if cf_behaviors is not None:
            self._values["cf_behaviors"] = cf_behaviors
        if error_doc is not None:
            self._values["error_doc"] = error_doc
        if export_website_url_name is not None:
            self._values["export_website_url_name"] = export_website_url_name
        if export_website_url_output is not None:
            self._values["export_website_url_output"] = export_website_url_output
        if role is not None:
            self._values["role"] = role
        if security_policy is not None:
            self._values["security_policy"] = security_policy
        if ssl_method is not None:
            self._values["ssl_method"] = ssl_method

    @builtins.property
    def index_doc(self) -> builtins.str:
        result = self._values.get("index_doc")
        assert result is not None, "Required property 'index_doc' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def website_folder(self) -> builtins.str:
        result = self._values.get("website_folder")
        assert result is not None, "Required property 'website_folder' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def block_public_access(self) -> typing.Optional[aws_cdk.aws_s3.BlockPublicAccess]:
        result = self._values.get("block_public_access")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.BlockPublicAccess], result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cf_aliases(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("cf_aliases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cf_behaviors(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudfront.Behavior]]:
        result = self._values.get("cf_behaviors")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_cloudfront.Behavior]], result)

    @builtins.property
    def error_doc(self) -> typing.Optional[builtins.str]:
        result = self._values.get("error_doc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def export_website_url_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("export_website_url_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def export_website_url_output(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("export_website_url_output")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.Role]:
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.Role], result)

    @builtins.property
    def security_policy(
        self,
    ) -> typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol]:
        result = self._values.get("security_policy")
        return typing.cast(typing.Optional[aws_cdk.aws_cloudfront.SecurityPolicyProtocol], result)

    @builtins.property
    def ssl_method(self) -> typing.Optional[aws_cdk.aws_cloudfront.SSLMethod]:
        result = self._values.get("ssl_method")
        return typing.cast(typing.Optional[aws_cdk.aws_cloudfront.SSLMethod], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SPADeployConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-spa-deploy.SPADeployment",
    jsii_struct_bases=[],
    name_mapping={"website_bucket": "websiteBucket"},
)
class SPADeployment:
    def __init__(self, *, website_bucket: aws_cdk.aws_s3.Bucket) -> None:
        '''
        :param website_bucket: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "website_bucket": website_bucket,
        }

    @builtins.property
    def website_bucket(self) -> aws_cdk.aws_s3.Bucket:
        result = self._values.get("website_bucket")
        assert result is not None, "Required property 'website_bucket' is missing"
        return typing.cast(aws_cdk.aws_s3.Bucket, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SPADeployment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-spa-deploy.SPADeploymentWithCloudFront",
    jsii_struct_bases=[SPADeployment],
    name_mapping={"website_bucket": "websiteBucket", "distribution": "distribution"},
)
class SPADeploymentWithCloudFront(SPADeployment):
    def __init__(
        self,
        *,
        website_bucket: aws_cdk.aws_s3.Bucket,
        distribution: aws_cdk.aws_cloudfront.CloudFrontWebDistribution,
    ) -> None:
        '''
        :param website_bucket: -
        :param distribution: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "website_bucket": website_bucket,
            "distribution": distribution,
        }

    @builtins.property
    def website_bucket(self) -> aws_cdk.aws_s3.Bucket:
        result = self._values.get("website_bucket")
        assert result is not None, "Required property 'website_bucket' is missing"
        return typing.cast(aws_cdk.aws_s3.Bucket, result)

    @builtins.property
    def distribution(self) -> aws_cdk.aws_cloudfront.CloudFrontWebDistribution:
        result = self._values.get("distribution")
        assert result is not None, "Required property 'distribution' is missing"
        return typing.cast(aws_cdk.aws_cloudfront.CloudFrontWebDistribution, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SPADeploymentWithCloudFront(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-spa-deploy.SPAGlobalConfig",
    jsii_struct_bases=[],
    name_mapping={
        "encrypt_bucket": "encryptBucket",
        "ip_filter": "ipFilter",
        "ip_list": "ipList",
        "role": "role",
    },
)
class SPAGlobalConfig:
    def __init__(
        self,
        *,
        encrypt_bucket: typing.Optional[builtins.bool] = None,
        ip_filter: typing.Optional[builtins.bool] = None,
        ip_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        role: typing.Optional[aws_cdk.aws_iam.Role] = None,
    ) -> None:
        '''
        :param encrypt_bucket: -
        :param ip_filter: -
        :param ip_list: -
        :param role: -
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if encrypt_bucket is not None:
            self._values["encrypt_bucket"] = encrypt_bucket
        if ip_filter is not None:
            self._values["ip_filter"] = ip_filter
        if ip_list is not None:
            self._values["ip_list"] = ip_list
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def encrypt_bucket(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("encrypt_bucket")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ip_filter(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("ip_filter")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ip_list(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("ip_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.Role]:
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.Role], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SPAGlobalConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HostedZoneConfig",
    "SPADeploy",
    "SPADeployConfig",
    "SPADeployment",
    "SPADeploymentWithCloudFront",
    "SPAGlobalConfig",
]

publication.publish()
