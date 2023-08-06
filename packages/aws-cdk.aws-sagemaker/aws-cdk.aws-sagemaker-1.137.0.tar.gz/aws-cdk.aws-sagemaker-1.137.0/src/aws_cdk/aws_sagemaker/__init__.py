'''
# Amazon SageMaker Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_sagemaker as sagemaker
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SageMaker](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SageMaker.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnApp(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnApp",
):
    '''A CloudFormation ``AWS::SageMaker::App``.

    :cloudformationResource: AWS::SageMaker::App
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_app = sagemaker.CfnApp(self, "MyCfnApp",
            app_name="appName",
            app_type="appType",
            domain_id="domainId",
            user_profile_name="userProfileName",
        
            # the properties below are optional
            resource_spec=sagemaker.CfnApp.ResourceSpecProperty(
                instance_type="instanceType",
                sage_maker_image_arn="sageMakerImageArn",
                sage_maker_image_version_arn="sageMakerImageVersionArn"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        app_name: builtins.str,
        app_type: builtins.str,
        domain_id: builtins.str,
        resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.ResourceSpecProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_profile_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SageMaker::App``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_name: ``AWS::SageMaker::App.AppName``.
        :param app_type: ``AWS::SageMaker::App.AppType``.
        :param domain_id: ``AWS::SageMaker::App.DomainId``.
        :param resource_spec: ``AWS::SageMaker::App.ResourceSpec``.
        :param tags: ``AWS::SageMaker::App.Tags``.
        :param user_profile_name: ``AWS::SageMaker::App.UserProfileName``.
        '''
        props = CfnAppProps(
            app_name=app_name,
            app_type=app_type,
            domain_id=domain_id,
            resource_spec=resource_spec,
            tags=tags,
            user_profile_name=user_profile_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appName")
    def app_name(self) -> builtins.str:
        '''``AWS::SageMaker::App.AppName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-appname
        '''
        return typing.cast(builtins.str, jsii.get(self, "appName"))

    @app_name.setter
    def app_name(self, value: builtins.str) -> None:
        jsii.set(self, "appName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appType")
    def app_type(self) -> builtins.str:
        '''``AWS::SageMaker::App.AppType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-apptype
        '''
        return typing.cast(builtins.str, jsii.get(self, "appType"))

    @app_type.setter
    def app_type(self, value: builtins.str) -> None:
        jsii.set(self, "appType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAppArn")
    def attr_app_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AppArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        '''``AWS::SageMaker::App.DomainId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-domainid
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: builtins.str) -> None:
        jsii.set(self, "domainId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceSpec")
    def resource_spec(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.ResourceSpecProperty"]]:
        '''``AWS::SageMaker::App.ResourceSpec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-resourcespec
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.ResourceSpecProperty"]], jsii.get(self, "resourceSpec"))

    @resource_spec.setter
    def resource_spec(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.ResourceSpecProperty"]],
    ) -> None:
        jsii.set(self, "resourceSpec", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::App.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userProfileName")
    def user_profile_name(self) -> builtins.str:
        '''``AWS::SageMaker::App.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-userprofilename
        '''
        return typing.cast(builtins.str, jsii.get(self, "userProfileName"))

    @user_profile_name.setter
    def user_profile_name(self, value: builtins.str) -> None:
        jsii.set(self, "userProfileName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnApp.ResourceSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "sage_maker_image_arn": "sageMakerImageArn",
            "sage_maker_image_version_arn": "sageMakerImageVersionArn",
        },
    )
    class ResourceSpecProperty:
        def __init__(
            self,
            *,
            instance_type: typing.Optional[builtins.str] = None,
            sage_maker_image_arn: typing.Optional[builtins.str] = None,
            sage_maker_image_version_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_type: ``CfnApp.ResourceSpecProperty.InstanceType``.
            :param sage_maker_image_arn: ``CfnApp.ResourceSpecProperty.SageMakerImageArn``.
            :param sage_maker_image_version_arn: ``CfnApp.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                resource_spec_property = sagemaker.CfnApp.ResourceSpecProperty(
                    instance_type="instanceType",
                    sage_maker_image_arn="sageMakerImageArn",
                    sage_maker_image_version_arn="sageMakerImageVersionArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if sage_maker_image_arn is not None:
                self._values["sage_maker_image_arn"] = sage_maker_image_arn
            if sage_maker_image_version_arn is not None:
                self._values["sage_maker_image_version_arn"] = sage_maker_image_version_arn

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.ResourceSpecProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.ResourceSpecProperty.SageMakerImageArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-sagemakerimagearn
            '''
            result = self._values.get("sage_maker_image_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_version_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-sagemakerimageversionarn
            '''
            result = self._values.get("sage_maker_image_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAppImageConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfig",
):
    '''A CloudFormation ``AWS::SageMaker::AppImageConfig``.

    :cloudformationResource: AWS::SageMaker::AppImageConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_app_image_config = sagemaker.CfnAppImageConfig(self, "MyCfnAppImageConfig",
            app_image_config_name="appImageConfigName",
        
            # the properties below are optional
            kernel_gateway_image_config=sagemaker.CfnAppImageConfig.KernelGatewayImageConfigProperty(
                kernel_specs=[sagemaker.CfnAppImageConfig.KernelSpecProperty(
                    name="name",
        
                    # the properties below are optional
                    display_name="displayName"
                )],
        
                # the properties below are optional
                file_system_config=sagemaker.CfnAppImageConfig.FileSystemConfigProperty(
                    default_gid=123,
                    default_uid=123,
                    mount_path="mountPath"
                )
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        app_image_config_name: builtins.str,
        kernel_gateway_image_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelGatewayImageConfigProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::AppImageConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_image_config_name: ``AWS::SageMaker::AppImageConfig.AppImageConfigName``.
        :param kernel_gateway_image_config: ``AWS::SageMaker::AppImageConfig.KernelGatewayImageConfig``.
        :param tags: ``AWS::SageMaker::AppImageConfig.Tags``.
        '''
        props = CfnAppImageConfigProps(
            app_image_config_name=app_image_config_name,
            kernel_gateway_image_config=kernel_gateway_image_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        '''``AWS::SageMaker::AppImageConfig.AppImageConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-appimageconfigname
        '''
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        jsii.set(self, "appImageConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAppImageConfigArn")
    def attr_app_image_config_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AppImageConfigArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppImageConfigArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kernelGatewayImageConfig")
    def kernel_gateway_image_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelGatewayImageConfigProperty"]]:
        '''``AWS::SageMaker::AppImageConfig.KernelGatewayImageConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelGatewayImageConfigProperty"]], jsii.get(self, "kernelGatewayImageConfig"))

    @kernel_gateway_image_config.setter
    def kernel_gateway_image_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelGatewayImageConfigProperty"]],
    ) -> None:
        jsii.set(self, "kernelGatewayImageConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::AppImageConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfig.FileSystemConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_gid": "defaultGid",
            "default_uid": "defaultUid",
            "mount_path": "mountPath",
        },
    )
    class FileSystemConfigProperty:
        def __init__(
            self,
            *,
            default_gid: typing.Optional[jsii.Number] = None,
            default_uid: typing.Optional[jsii.Number] = None,
            mount_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param default_gid: ``CfnAppImageConfig.FileSystemConfigProperty.DefaultGid``.
            :param default_uid: ``CfnAppImageConfig.FileSystemConfigProperty.DefaultUid``.
            :param mount_path: ``CfnAppImageConfig.FileSystemConfigProperty.MountPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                file_system_config_property = sagemaker.CfnAppImageConfig.FileSystemConfigProperty(
                    default_gid=123,
                    default_uid=123,
                    mount_path="mountPath"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_gid is not None:
                self._values["default_gid"] = default_gid
            if default_uid is not None:
                self._values["default_uid"] = default_uid
            if mount_path is not None:
                self._values["mount_path"] = mount_path

        @builtins.property
        def default_gid(self) -> typing.Optional[jsii.Number]:
            '''``CfnAppImageConfig.FileSystemConfigProperty.DefaultGid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-defaultgid
            '''
            result = self._values.get("default_gid")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def default_uid(self) -> typing.Optional[jsii.Number]:
            '''``CfnAppImageConfig.FileSystemConfigProperty.DefaultUid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-defaultuid
            '''
            result = self._values.get("default_uid")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_path(self) -> typing.Optional[builtins.str]:
            '''``CfnAppImageConfig.FileSystemConfigProperty.MountPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-mountpath
            '''
            result = self._values.get("mount_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileSystemConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfig.KernelGatewayImageConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "file_system_config": "fileSystemConfig",
            "kernel_specs": "kernelSpecs",
        },
    )
    class KernelGatewayImageConfigProperty:
        def __init__(
            self,
            *,
            file_system_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.FileSystemConfigProperty"]] = None,
            kernel_specs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelSpecProperty"]]],
        ) -> None:
            '''
            :param file_system_config: ``CfnAppImageConfig.KernelGatewayImageConfigProperty.FileSystemConfig``.
            :param kernel_specs: ``CfnAppImageConfig.KernelGatewayImageConfigProperty.KernelSpecs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                kernel_gateway_image_config_property = sagemaker.CfnAppImageConfig.KernelGatewayImageConfigProperty(
                    kernel_specs=[sagemaker.CfnAppImageConfig.KernelSpecProperty(
                        name="name",
                
                        # the properties below are optional
                        display_name="displayName"
                    )],
                
                    # the properties below are optional
                    file_system_config=sagemaker.CfnAppImageConfig.FileSystemConfigProperty(
                        default_gid=123,
                        default_uid=123,
                        mount_path="mountPath"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "kernel_specs": kernel_specs,
            }
            if file_system_config is not None:
                self._values["file_system_config"] = file_system_config

        @builtins.property
        def file_system_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.FileSystemConfigProperty"]]:
            '''``CfnAppImageConfig.KernelGatewayImageConfigProperty.FileSystemConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-filesystemconfig
            '''
            result = self._values.get("file_system_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.FileSystemConfigProperty"]], result)

        @builtins.property
        def kernel_specs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelSpecProperty"]]]:
            '''``CfnAppImageConfig.KernelGatewayImageConfigProperty.KernelSpecs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-kernelspecs
            '''
            result = self._values.get("kernel_specs")
            assert result is not None, "Required property 'kernel_specs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelSpecProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KernelGatewayImageConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfig.KernelSpecProperty",
        jsii_struct_bases=[],
        name_mapping={"display_name": "displayName", "name": "name"},
    )
    class KernelSpecProperty:
        def __init__(
            self,
            *,
            display_name: typing.Optional[builtins.str] = None,
            name: builtins.str,
        ) -> None:
            '''
            :param display_name: ``CfnAppImageConfig.KernelSpecProperty.DisplayName``.
            :param name: ``CfnAppImageConfig.KernelSpecProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                kernel_spec_property = sagemaker.CfnAppImageConfig.KernelSpecProperty(
                    name="name",
                
                    # the properties below are optional
                    display_name="displayName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if display_name is not None:
                self._values["display_name"] = display_name

        @builtins.property
        def display_name(self) -> typing.Optional[builtins.str]:
            '''``CfnAppImageConfig.KernelSpecProperty.DisplayName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html#cfn-sagemaker-appimageconfig-kernelspec-displayname
            '''
            result = self._values.get("display_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAppImageConfig.KernelSpecProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html#cfn-sagemaker-appimageconfig-kernelspec-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KernelSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "kernel_gateway_image_config": "kernelGatewayImageConfig",
        "tags": "tags",
    },
)
class CfnAppImageConfigProps:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        kernel_gateway_image_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAppImageConfig.KernelGatewayImageConfigProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::AppImageConfig``.

        :param app_image_config_name: ``AWS::SageMaker::AppImageConfig.AppImageConfigName``.
        :param kernel_gateway_image_config: ``AWS::SageMaker::AppImageConfig.KernelGatewayImageConfig``.
        :param tags: ``AWS::SageMaker::AppImageConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_app_image_config_props = sagemaker.CfnAppImageConfigProps(
                app_image_config_name="appImageConfigName",
            
                # the properties below are optional
                kernel_gateway_image_config=sagemaker.CfnAppImageConfig.KernelGatewayImageConfigProperty(
                    kernel_specs=[sagemaker.CfnAppImageConfig.KernelSpecProperty(
                        name="name",
            
                        # the properties below are optional
                        display_name="displayName"
                    )],
            
                    # the properties below are optional
                    file_system_config=sagemaker.CfnAppImageConfig.FileSystemConfigProperty(
                        default_gid=123,
                        default_uid=123,
                        mount_path="mountPath"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
        }
        if kernel_gateway_image_config is not None:
            self._values["kernel_gateway_image_config"] = kernel_gateway_image_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''``AWS::SageMaker::AppImageConfig.AppImageConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-appimageconfigname
        '''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kernel_gateway_image_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAppImageConfig.KernelGatewayImageConfigProperty]]:
        '''``AWS::SageMaker::AppImageConfig.KernelGatewayImageConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig
        '''
        result = self._values.get("kernel_gateway_image_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAppImageConfig.KernelGatewayImageConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::AppImageConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppImageConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_name": "appName",
        "app_type": "appType",
        "domain_id": "domainId",
        "resource_spec": "resourceSpec",
        "tags": "tags",
        "user_profile_name": "userProfileName",
    },
)
class CfnAppProps:
    def __init__(
        self,
        *,
        app_name: builtins.str,
        app_type: builtins.str,
        domain_id: builtins.str,
        resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.ResourceSpecProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_profile_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::App``.

        :param app_name: ``AWS::SageMaker::App.AppName``.
        :param app_type: ``AWS::SageMaker::App.AppType``.
        :param domain_id: ``AWS::SageMaker::App.DomainId``.
        :param resource_spec: ``AWS::SageMaker::App.ResourceSpec``.
        :param tags: ``AWS::SageMaker::App.Tags``.
        :param user_profile_name: ``AWS::SageMaker::App.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_app_props = sagemaker.CfnAppProps(
                app_name="appName",
                app_type="appType",
                domain_id="domainId",
                user_profile_name="userProfileName",
            
                # the properties below are optional
                resource_spec=sagemaker.CfnApp.ResourceSpecProperty(
                    instance_type="instanceType",
                    sage_maker_image_arn="sageMakerImageArn",
                    sage_maker_image_version_arn="sageMakerImageVersionArn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "app_name": app_name,
            "app_type": app_type,
            "domain_id": domain_id,
            "user_profile_name": user_profile_name,
        }
        if resource_spec is not None:
            self._values["resource_spec"] = resource_spec
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_name(self) -> builtins.str:
        '''``AWS::SageMaker::App.AppName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-appname
        '''
        result = self._values.get("app_name")
        assert result is not None, "Required property 'app_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_type(self) -> builtins.str:
        '''``AWS::SageMaker::App.AppType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-apptype
        '''
        result = self._values.get("app_type")
        assert result is not None, "Required property 'app_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''``AWS::SageMaker::App.DomainId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-domainid
        '''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_spec(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.ResourceSpecProperty]]:
        '''``AWS::SageMaker::App.ResourceSpec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-resourcespec
        '''
        result = self._values.get("resource_spec")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.ResourceSpecProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::App.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def user_profile_name(self) -> builtins.str:
        '''``AWS::SageMaker::App.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-userprofilename
        '''
        result = self._values.get("user_profile_name")
        assert result is not None, "Required property 'user_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCodeRepository(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepository",
):
    '''A CloudFormation ``AWS::SageMaker::CodeRepository``.

    :cloudformationResource: AWS::SageMaker::CodeRepository
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_code_repository = sagemaker.CfnCodeRepository(self, "MyCfnCodeRepository",
            git_config=sagemaker.CfnCodeRepository.GitConfigProperty(
                repository_url="repositoryUrl",
        
                # the properties below are optional
                branch="branch",
                secret_arn="secretArn"
            ),
        
            # the properties below are optional
            code_repository_name="codeRepositoryName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        code_repository_name: typing.Optional[builtins.str] = None,
        git_config: typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable],
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::CodeRepository``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param code_repository_name: ``AWS::SageMaker::CodeRepository.CodeRepositoryName``.
        :param git_config: ``AWS::SageMaker::CodeRepository.GitConfig``.
        :param tags: ``AWS::SageMaker::CodeRepository.Tags``.
        '''
        props = CfnCodeRepositoryProps(
            code_repository_name=code_repository_name, git_config=git_config, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCodeRepositoryName")
    def attr_code_repository_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: CodeRepositoryName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeRepositoryName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="codeRepositoryName")
    def code_repository_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::CodeRepository.CodeRepositoryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-coderepositoryname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeRepositoryName"))

    @code_repository_name.setter
    def code_repository_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "codeRepositoryName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gitConfig")
    def git_config(
        self,
    ) -> typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable]:
        '''``AWS::SageMaker::CodeRepository.GitConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-gitconfig
        '''
        return typing.cast(typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable], jsii.get(self, "gitConfig"))

    @git_config.setter
    def git_config(
        self,
        value: typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "gitConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::CodeRepository.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepository.GitConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "branch": "branch",
            "repository_url": "repositoryUrl",
            "secret_arn": "secretArn",
        },
    )
    class GitConfigProperty:
        def __init__(
            self,
            *,
            branch: typing.Optional[builtins.str] = None,
            repository_url: builtins.str,
            secret_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param branch: ``CfnCodeRepository.GitConfigProperty.Branch``.
            :param repository_url: ``CfnCodeRepository.GitConfigProperty.RepositoryUrl``.
            :param secret_arn: ``CfnCodeRepository.GitConfigProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                git_config_property = sagemaker.CfnCodeRepository.GitConfigProperty(
                    repository_url="repositoryUrl",
                
                    # the properties below are optional
                    branch="branch",
                    secret_arn="secretArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "repository_url": repository_url,
            }
            if branch is not None:
                self._values["branch"] = branch
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn

        @builtins.property
        def branch(self) -> typing.Optional[builtins.str]:
            '''``CfnCodeRepository.GitConfigProperty.Branch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-branch
            '''
            result = self._values.get("branch")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def repository_url(self) -> builtins.str:
            '''``CfnCodeRepository.GitConfigProperty.RepositoryUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-repositoryurl
            '''
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnCodeRepository.GitConfigProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GitConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "code_repository_name": "codeRepositoryName",
        "git_config": "gitConfig",
        "tags": "tags",
    },
)
class CfnCodeRepositoryProps:
    def __init__(
        self,
        *,
        code_repository_name: typing.Optional[builtins.str] = None,
        git_config: typing.Union[CfnCodeRepository.GitConfigProperty, aws_cdk.core.IResolvable],
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::CodeRepository``.

        :param code_repository_name: ``AWS::SageMaker::CodeRepository.CodeRepositoryName``.
        :param git_config: ``AWS::SageMaker::CodeRepository.GitConfig``.
        :param tags: ``AWS::SageMaker::CodeRepository.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_code_repository_props = sagemaker.CfnCodeRepositoryProps(
                git_config=sagemaker.CfnCodeRepository.GitConfigProperty(
                    repository_url="repositoryUrl",
            
                    # the properties below are optional
                    branch="branch",
                    secret_arn="secretArn"
                ),
            
                # the properties below are optional
                code_repository_name="codeRepositoryName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "git_config": git_config,
        }
        if code_repository_name is not None:
            self._values["code_repository_name"] = code_repository_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def code_repository_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::CodeRepository.CodeRepositoryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-coderepositoryname
        '''
        result = self._values.get("code_repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git_config(
        self,
    ) -> typing.Union[CfnCodeRepository.GitConfigProperty, aws_cdk.core.IResolvable]:
        '''``AWS::SageMaker::CodeRepository.GitConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-gitconfig
        '''
        result = self._values.get("git_config")
        assert result is not None, "Required property 'git_config' is missing"
        return typing.cast(typing.Union[CfnCodeRepository.GitConfigProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::CodeRepository.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDataQualityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition",
):
    '''A CloudFormation ``AWS::SageMaker::DataQualityJobDefinition``.

    :cloudformationResource: AWS::SageMaker::DataQualityJobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_data_quality_job_definition = sagemaker.CfnDataQualityJobDefinition(self, "MyCfnDataQualityJobDefinition",
            data_quality_app_specification=sagemaker.CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty(
                image_uri="imageUri",
        
                # the properties below are optional
                container_arguments=["containerArguments"],
                container_entrypoint=["containerEntrypoint"],
                environment={
                    "environment_key": "environment"
                },
                post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                record_preprocessor_source_uri="recordPreprocessorSourceUri"
            ),
            data_quality_job_input=sagemaker.CfnDataQualityJobDefinition.DataQualityJobInputProperty(
                endpoint_input=sagemaker.CfnDataQualityJobDefinition.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
        
                    # the properties below are optional
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode"
                )
            ),
            data_quality_job_output_config=sagemaker.CfnDataQualityJobDefinition.MonitoringOutputConfigProperty(
                monitoring_outputs=[sagemaker.CfnDataQualityJobDefinition.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnDataQualityJobDefinition.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
        
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )],
        
                # the properties below are optional
                kms_key_id="kmsKeyId"
            ),
            job_resources=sagemaker.CfnDataQualityJobDefinition.MonitoringResourcesProperty(
                cluster_config=sagemaker.CfnDataQualityJobDefinition.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
        
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            data_quality_baseline_config=sagemaker.CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty(
                baselining_job_name="baseliningJobName",
                constraints_resource=sagemaker.CfnDataQualityJobDefinition.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                ),
                statistics_resource=sagemaker.CfnDataQualityJobDefinition.StatisticsResourceProperty(
                    s3_uri="s3Uri"
                )
            ),
            job_definition_name="jobDefinitionName",
            network_config=sagemaker.CfnDataQualityJobDefinition.NetworkConfigProperty(
                enable_inter_container_traffic_encryption=False,
                enable_network_isolation=False,
                vpc_config=sagemaker.CfnDataQualityJobDefinition.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            ),
            stopping_condition=sagemaker.CfnDataQualityJobDefinition.StoppingConditionProperty(
                max_runtime_in_seconds=123
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"],
        data_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]] = None,
        data_quality_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"],
        data_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"],
        job_definition_name: typing.Optional[builtins.str] = None,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"],
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]] = None,
        role_arn: builtins.str,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::DataQualityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_quality_app_specification: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.
        :param data_quality_baseline_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.
        :param data_quality_job_input: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.
        :param data_quality_job_output_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.
        :param job_definition_name: ``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.
        :param job_resources: ``AWS::SageMaker::DataQualityJobDefinition.JobResources``.
        :param network_config: ``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.
        :param role_arn: ``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.
        :param stopping_condition: ``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::DataQualityJobDefinition.Tags``.
        '''
        props = CfnDataQualityJobDefinitionProps(
            data_quality_app_specification=data_quality_app_specification,
            data_quality_baseline_config=data_quality_baseline_config,
            data_quality_job_input=data_quality_job_input,
            data_quality_job_output_config=data_quality_job_output_config,
            job_definition_name=job_definition_name,
            job_resources=job_resources,
            network_config=network_config,
            role_arn=role_arn,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: JobDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobDefinitionArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataQualityAppSpecification")
    def data_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"], jsii.get(self, "dataQualityAppSpecification"))

    @data_quality_app_specification.setter
    def data_quality_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "dataQualityAppSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataQualityBaselineConfig")
    def data_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]], jsii.get(self, "dataQualityBaselineConfig"))

    @data_quality_baseline_config.setter
    def data_quality_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "dataQualityBaselineConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataQualityJobInput")
    def data_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"], jsii.get(self, "dataQualityJobInput"))

    @data_quality_job_input.setter
    def data_quality_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"],
    ) -> None:
        jsii.set(self, "dataQualityJobInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataQualityJobOutputConfig")
    def data_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"], jsii.get(self, "dataQualityJobOutputConfig"))

    @data_quality_job_output_config.setter
    def data_quality_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "dataQualityJobOutputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"]:
        '''``AWS::SageMaker::DataQualityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobresources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"], jsii.get(self, "jobResources"))

    @job_resources.setter
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]], jsii.get(self, "networkConfig"))

    @network_config.setter
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]], jsii.get(self, "stoppingCondition"))

    @stopping_condition.setter
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_kms_key_id": "volumeKmsKeyId",
            "volume_size_in_gb": "volumeSizeInGb",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
            volume_size_in_gb: jsii.Number,
        ) -> None:
            '''
            :param instance_count: ``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_kms_key_id: ``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.
            :param volume_size_in_gb: ``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                cluster_config_property = sagemaker.CfnDataQualityJobDefinition.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
                
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnDataQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                constraints_resource_property = sagemaker.CfnDataQualityJobDefinition.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html#cfn-sagemaker-dataqualityjobdefinition-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "environment": "environment",
            "image_uri": "imageUri",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class DataQualityAppSpecificationProperty:
        def __init__(
            self,
            *,
            container_arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            image_uri: builtins.str,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param container_arguments: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerEntrypoint``.
            :param environment: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.Environment``.
            :param image_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ImageUri``.
            :param post_analytics_processor_source_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param record_preprocessor_source_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                data_quality_app_specification_property = sagemaker.CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty(
                    image_uri="imageUri",
                
                    # the properties below are optional
                    container_arguments=["containerArguments"],
                    container_entrypoint=["containerEntrypoint"],
                    environment={
                        "environment_key": "environment"
                    },
                    post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                    record_preprocessor_source_uri="recordPreprocessorSourceUri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if environment is not None:
                self._values["environment"] = environment
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerArguments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-containerarguments
            '''
            result = self._values.get("container_arguments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerEntrypoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-containerentrypoint
            '''
            result = self._values.get("container_entrypoint")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-postanalyticsprocessorsourceuri
            '''
            result = self._values.get("post_analytics_processor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-recordpreprocessorsourceuri
            '''
            result = self._values.get("record_preprocessor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
            "statistics_resource": "statisticsResource",
        },
    )
    class DataQualityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ConstraintsResourceProperty"]] = None,
            statistics_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StatisticsResourceProperty"]] = None,
        ) -> None:
            '''
            :param baselining_job_name: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.ConstraintsResource``.
            :param statistics_resource: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.StatisticsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                data_quality_baseline_config_property = sagemaker.CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty(
                    baselining_job_name="baseliningJobName",
                    constraints_resource=sagemaker.CfnDataQualityJobDefinition.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    ),
                    statistics_resource=sagemaker.CfnDataQualityJobDefinition.StatisticsResourceProperty(
                        s3_uri="s3Uri"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource
            if statistics_resource is not None:
                self._values["statistics_resource"] = statistics_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.BaseliningJobName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-baseliningjobname
            '''
            result = self._values.get("baselining_job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ConstraintsResourceProperty"]]:
            '''``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ConstraintsResourceProperty"]], result)

        @builtins.property
        def statistics_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StatisticsResourceProperty"]]:
            '''``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.StatisticsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-statisticsresource
            '''
            result = self._values.get("statistics_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StatisticsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class DataQualityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EndpointInputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnDataQualityJobDefinition.DataQualityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                data_quality_job_input_property = sagemaker.CfnDataQualityJobDefinition.DataQualityJobInputProperty(
                    endpoint_input=sagemaker.CfnDataQualityJobDefinition.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
                
                        # the properties below are optional
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EndpointInputProperty"]:
            '''``CfnDataQualityJobDefinition.DataQualityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EndpointInputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnDataQualityJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnDataQualityJobDefinition.EndpointInputProperty.LocalPath``.
            :param s3_data_distribution_type: ``CfnDataQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnDataQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                endpoint_input_property = sagemaker.CfnDataQualityJobDefinition.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
                
                    # the properties below are optional
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_id": "kmsKeyId",
            "monitoring_outputs": "monitoringOutputs",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputProperty"]]],
        ) -> None:
            '''
            :param kms_key_id: ``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.
            :param monitoring_outputs: ``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_config_property = sagemaker.CfnDataQualityJobDefinition.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnDataQualityJobDefinition.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnDataQualityJobDefinition.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
                
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputProperty"]]]:
            '''``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnDataQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_property = sagemaker.CfnDataQualityJobDefinition.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnDataQualityJobDefinition.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.S3OutputProperty"]:
            '''``CfnDataQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnDataQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_resources_property = sagemaker.CfnDataQualityJobDefinition.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnDataQualityJobDefinition.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
                
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ClusterConfigProperty"]:
            '''``CfnDataQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html#cfn-sagemaker-dataqualityjobdefinition-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnDataQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                network_config_property = sagemaker.CfnDataQualityJobDefinition.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnDataQualityJobDefinition.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.VpcConfigProperty"]]:
            '''``CfnDataQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_upload_mode": "s3UploadMode",
            "s3_uri": "s3Uri",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
            s3_uri: builtins.str,
        ) -> None:
            '''
            :param local_path: ``CfnDataQualityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_upload_mode: ``CfnDataQualityJobDefinition.S3OutputProperty.S3UploadMode``.
            :param s3_uri: ``CfnDataQualityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                s3_output_property = sagemaker.CfnDataQualityJobDefinition.S3OutputProperty(
                    local_path="localPath",
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    s3_upload_mode="s3UploadMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.StatisticsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class StatisticsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnDataQualityJobDefinition.StatisticsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                statistics_resource_property = sagemaker.CfnDataQualityJobDefinition.StatisticsResourceProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.StatisticsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html#cfn-sagemaker-dataqualityjobdefinition-statisticsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnDataQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                stopping_condition_property = sagemaker.CfnDataQualityJobDefinition.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnDataQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnDataQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnDataQualityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                vpc_config_property = sagemaker.CfnDataQualityJobDefinition.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnDataQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html#cfn-sagemaker-dataqualityjobdefinition-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnDataQualityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html#cfn-sagemaker-dataqualityjobdefinition-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_quality_app_specification": "dataQualityAppSpecification",
        "data_quality_baseline_config": "dataQualityBaselineConfig",
        "data_quality_job_input": "dataQualityJobInput",
        "data_quality_job_output_config": "dataQualityJobOutputConfig",
        "job_definition_name": "jobDefinitionName",
        "job_resources": "jobResources",
        "network_config": "networkConfig",
        "role_arn": "roleArn",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnDataQualityJobDefinitionProps:
    def __init__(
        self,
        *,
        data_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty],
        data_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty]] = None,
        data_quality_job_input: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityJobInputProperty],
        data_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringOutputConfigProperty],
        job_definition_name: typing.Optional[builtins.str] = None,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringResourcesProperty],
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.NetworkConfigProperty]] = None,
        role_arn: builtins.str,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::DataQualityJobDefinition``.

        :param data_quality_app_specification: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.
        :param data_quality_baseline_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.
        :param data_quality_job_input: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.
        :param data_quality_job_output_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.
        :param job_definition_name: ``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.
        :param job_resources: ``AWS::SageMaker::DataQualityJobDefinition.JobResources``.
        :param network_config: ``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.
        :param role_arn: ``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.
        :param stopping_condition: ``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_data_quality_job_definition_props = sagemaker.CfnDataQualityJobDefinitionProps(
                data_quality_app_specification=sagemaker.CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty(
                    image_uri="imageUri",
            
                    # the properties below are optional
                    container_arguments=["containerArguments"],
                    container_entrypoint=["containerEntrypoint"],
                    environment={
                        "environment_key": "environment"
                    },
                    post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                    record_preprocessor_source_uri="recordPreprocessorSourceUri"
                ),
                data_quality_job_input=sagemaker.CfnDataQualityJobDefinition.DataQualityJobInputProperty(
                    endpoint_input=sagemaker.CfnDataQualityJobDefinition.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
            
                        # the properties below are optional
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode"
                    )
                ),
                data_quality_job_output_config=sagemaker.CfnDataQualityJobDefinition.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnDataQualityJobDefinition.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnDataQualityJobDefinition.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
            
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
            
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                ),
                job_resources=sagemaker.CfnDataQualityJobDefinition.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnDataQualityJobDefinition.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
            
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                data_quality_baseline_config=sagemaker.CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty(
                    baselining_job_name="baseliningJobName",
                    constraints_resource=sagemaker.CfnDataQualityJobDefinition.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    ),
                    statistics_resource=sagemaker.CfnDataQualityJobDefinition.StatisticsResourceProperty(
                        s3_uri="s3Uri"
                    )
                ),
                job_definition_name="jobDefinitionName",
                network_config=sagemaker.CfnDataQualityJobDefinition.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnDataQualityJobDefinition.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                ),
                stopping_condition=sagemaker.CfnDataQualityJobDefinition.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_quality_app_specification": data_quality_app_specification,
            "data_quality_job_input": data_quality_job_input,
            "data_quality_job_output_config": data_quality_job_output_config,
            "job_resources": job_resources,
            "role_arn": role_arn,
        }
        if data_quality_baseline_config is not None:
            self._values["data_quality_baseline_config"] = data_quality_baseline_config
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification
        '''
        result = self._values.get("data_quality_app_specification")
        assert result is not None, "Required property 'data_quality_app_specification' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty], result)

    @builtins.property
    def data_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig
        '''
        result = self._values.get("data_quality_baseline_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty]], result)

    @builtins.property
    def data_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityJobInputProperty]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput
        '''
        result = self._values.get("data_quality_job_input")
        assert result is not None, "Required property 'data_quality_job_input' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityJobInputProperty], result)

    @builtins.property
    def data_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringOutputConfigProperty]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig
        '''
        result = self._values.get("data_quality_job_output_config")
        assert result is not None, "Required property 'data_quality_job_output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringOutputConfigProperty], result)

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringResourcesProperty]:
        '''``AWS::SageMaker::DataQualityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobresources
        '''
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringResourcesProperty], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.NetworkConfigProperty]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.NetworkConfigProperty]], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.StoppingConditionProperty]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition
        '''
        result = self._values.get("stopping_condition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.StoppingConditionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataQualityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDevice(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDevice",
):
    '''A CloudFormation ``AWS::SageMaker::Device``.

    :cloudformationResource: AWS::SageMaker::Device
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_device = sagemaker.CfnDevice(self, "MyCfnDevice",
            device_fleet_name="deviceFleetName",
        
            # the properties below are optional
            device=sagemaker.CfnDevice.DeviceProperty(
                device_name="deviceName",
        
                # the properties below are optional
                description="description",
                iot_thing_name="iotThingName"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        device: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]] = None,
        device_fleet_name: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Device``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param device: ``AWS::SageMaker::Device.Device``.
        :param device_fleet_name: ``AWS::SageMaker::Device.DeviceFleetName``.
        :param tags: ``AWS::SageMaker::Device.Tags``.
        '''
        props = CfnDeviceProps(
            device=device, device_fleet_name=device_fleet_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="device")
    def device(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]]:
        '''``AWS::SageMaker::Device.Device``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-device
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]], jsii.get(self, "device"))

    @device.setter
    def device(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]],
    ) -> None:
        jsii.set(self, "device", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deviceFleetName")
    def device_fleet_name(self) -> builtins.str:
        '''``AWS::SageMaker::Device.DeviceFleetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-devicefleetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceFleetName"))

    @device_fleet_name.setter
    def device_fleet_name(self, value: builtins.str) -> None:
        jsii.set(self, "deviceFleetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Device.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDevice.DeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "description": "description",
            "device_name": "deviceName",
            "iot_thing_name": "iotThingName",
        },
    )
    class DeviceProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            device_name: builtins.str,
            iot_thing_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param description: ``CfnDevice.DeviceProperty.Description``.
            :param device_name: ``CfnDevice.DeviceProperty.DeviceName``.
            :param iot_thing_name: ``CfnDevice.DeviceProperty.IotThingName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                device_property = sagemaker.CfnDevice.DeviceProperty(
                    device_name="deviceName",
                
                    # the properties below are optional
                    description="description",
                    iot_thing_name="iotThingName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "device_name": device_name,
            }
            if description is not None:
                self._values["description"] = description
            if iot_thing_name is not None:
                self._values["iot_thing_name"] = iot_thing_name

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDevice.DeviceProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_name(self) -> builtins.str:
            '''``CfnDevice.DeviceProperty.DeviceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-devicename
            '''
            result = self._values.get("device_name")
            assert result is not None, "Required property 'device_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iot_thing_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDevice.DeviceProperty.IotThingName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-iotthingname
            '''
            result = self._values.get("iot_thing_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDeviceFleet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleet",
):
    '''A CloudFormation ``AWS::SageMaker::DeviceFleet``.

    :cloudformationResource: AWS::SageMaker::DeviceFleet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_device_fleet = sagemaker.CfnDeviceFleet(self, "MyCfnDeviceFleet",
            device_fleet_name="deviceFleetName",
            output_config=sagemaker.CfnDeviceFleet.EdgeOutputConfigProperty(
                s3_output_location="s3OutputLocation",
        
                # the properties below are optional
                kms_key_id="kmsKeyId"
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        device_fleet_name: builtins.str,
        output_config: typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"],
        role_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::DeviceFleet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::SageMaker::DeviceFleet.Description``.
        :param device_fleet_name: ``AWS::SageMaker::DeviceFleet.DeviceFleetName``.
        :param output_config: ``AWS::SageMaker::DeviceFleet.OutputConfig``.
        :param role_arn: ``AWS::SageMaker::DeviceFleet.RoleArn``.
        :param tags: ``AWS::SageMaker::DeviceFleet.Tags``.
        '''
        props = CfnDeviceFleetProps(
            description=description,
            device_fleet_name=device_fleet_name,
            output_config=output_config,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::DeviceFleet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deviceFleetName")
    def device_fleet_name(self) -> builtins.str:
        '''``AWS::SageMaker::DeviceFleet.DeviceFleetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-devicefleetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceFleetName"))

    @device_fleet_name.setter
    def device_fleet_name(self, value: builtins.str) -> None:
        jsii.set(self, "deviceFleetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outputConfig")
    def output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"]:
        '''``AWS::SageMaker::DeviceFleet.OutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-outputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"], jsii.get(self, "outputConfig"))

    @output_config.setter
    def output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "outputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::DeviceFleet.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::DeviceFleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleet.EdgeOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_id": "kmsKeyId",
            "s3_output_location": "s3OutputLocation",
        },
    )
    class EdgeOutputConfigProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            s3_output_location: builtins.str,
        ) -> None:
            '''
            :param kms_key_id: ``CfnDeviceFleet.EdgeOutputConfigProperty.KmsKeyId``.
            :param s3_output_location: ``CfnDeviceFleet.EdgeOutputConfigProperty.S3OutputLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                edge_output_config_property = sagemaker.CfnDeviceFleet.EdgeOutputConfigProperty(
                    s3_output_location="s3OutputLocation",
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output_location": s3_output_location,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDeviceFleet.EdgeOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html#cfn-sagemaker-devicefleet-edgeoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_output_location(self) -> builtins.str:
            '''``CfnDeviceFleet.EdgeOutputConfigProperty.S3OutputLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html#cfn-sagemaker-devicefleet-edgeoutputconfig-s3outputlocation
            '''
            result = self._values.get("s3_output_location")
            assert result is not None, "Required property 's3_output_location' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdgeOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "device_fleet_name": "deviceFleetName",
        "output_config": "outputConfig",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnDeviceFleetProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        device_fleet_name: builtins.str,
        output_config: typing.Union[aws_cdk.core.IResolvable, CfnDeviceFleet.EdgeOutputConfigProperty],
        role_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::DeviceFleet``.

        :param description: ``AWS::SageMaker::DeviceFleet.Description``.
        :param device_fleet_name: ``AWS::SageMaker::DeviceFleet.DeviceFleetName``.
        :param output_config: ``AWS::SageMaker::DeviceFleet.OutputConfig``.
        :param role_arn: ``AWS::SageMaker::DeviceFleet.RoleArn``.
        :param tags: ``AWS::SageMaker::DeviceFleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_device_fleet_props = sagemaker.CfnDeviceFleetProps(
                device_fleet_name="deviceFleetName",
                output_config=sagemaker.CfnDeviceFleet.EdgeOutputConfigProperty(
                    s3_output_location="s3OutputLocation",
            
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "device_fleet_name": device_fleet_name,
            "output_config": output_config,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::DeviceFleet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_fleet_name(self) -> builtins.str:
        '''``AWS::SageMaker::DeviceFleet.DeviceFleetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-devicefleetname
        '''
        result = self._values.get("device_fleet_name")
        assert result is not None, "Required property 'device_fleet_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDeviceFleet.EdgeOutputConfigProperty]:
        '''``AWS::SageMaker::DeviceFleet.OutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-outputconfig
        '''
        result = self._values.get("output_config")
        assert result is not None, "Required property 'output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDeviceFleet.EdgeOutputConfigProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::DeviceFleet.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::DeviceFleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "device": "device",
        "device_fleet_name": "deviceFleetName",
        "tags": "tags",
    },
)
class CfnDeviceProps:
    def __init__(
        self,
        *,
        device: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.DeviceProperty]] = None,
        device_fleet_name: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Device``.

        :param device: ``AWS::SageMaker::Device.Device``.
        :param device_fleet_name: ``AWS::SageMaker::Device.DeviceFleetName``.
        :param tags: ``AWS::SageMaker::Device.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_device_props = sagemaker.CfnDeviceProps(
                device_fleet_name="deviceFleetName",
            
                # the properties below are optional
                device=sagemaker.CfnDevice.DeviceProperty(
                    device_name="deviceName",
            
                    # the properties below are optional
                    description="description",
                    iot_thing_name="iotThingName"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "device_fleet_name": device_fleet_name,
        }
        if device is not None:
            self._values["device"] = device
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def device(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.DeviceProperty]]:
        '''``AWS::SageMaker::Device.Device``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-device
        '''
        result = self._values.get("device")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.DeviceProperty]], result)

    @builtins.property
    def device_fleet_name(self) -> builtins.str:
        '''``AWS::SageMaker::Device.DeviceFleetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-devicefleetname
        '''
        result = self._values.get("device_fleet_name")
        assert result is not None, "Required property 'device_fleet_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Device.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDomain(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDomain",
):
    '''A CloudFormation ``AWS::SageMaker::Domain``.

    :cloudformationResource: AWS::SageMaker::Domain
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_domain = sagemaker.CfnDomain(self, "MyCfnDomain",
            auth_mode="authMode",
            default_user_settings=sagemaker.CfnDomain.UserSettingsProperty(
                execution_role="executionRole",
                jupyter_server_app_settings=sagemaker.CfnDomain.JupyterServerAppSettingsProperty(
                    default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                        instance_type="instanceType",
                        sage_maker_image_arn="sageMakerImageArn",
                        sage_maker_image_version_arn="sageMakerImageVersionArn"
                    )
                ),
                kernel_gateway_app_settings=sagemaker.CfnDomain.KernelGatewayAppSettingsProperty(
                    custom_images=[sagemaker.CfnDomain.CustomImageProperty(
                        app_image_config_name="appImageConfigName",
                        image_name="imageName",
        
                        # the properties below are optional
                        image_version_number=123
                    )],
                    default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                        instance_type="instanceType",
                        sage_maker_image_arn="sageMakerImageArn",
                        sage_maker_image_version_arn="sageMakerImageVersionArn"
                    )
                ),
                security_groups=["securityGroups"],
                sharing_settings=sagemaker.CfnDomain.SharingSettingsProperty(
                    notebook_output_option="notebookOutputOption",
                    s3_kms_key_id="s3KmsKeyId",
                    s3_output_path="s3OutputPath"
                )
            ),
            domain_name="domainName",
            subnet_ids=["subnetIds"],
            vpc_id="vpcId",
        
            # the properties below are optional
            app_network_access_type="appNetworkAccessType",
            kms_key_id="kmsKeyId",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        app_network_access_type: typing.Optional[builtins.str] = None,
        auth_mode: builtins.str,
        default_user_settings: typing.Union[aws_cdk.core.IResolvable, "CfnDomain.UserSettingsProperty"],
        domain_name: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Domain``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_network_access_type: ``AWS::SageMaker::Domain.AppNetworkAccessType``.
        :param auth_mode: ``AWS::SageMaker::Domain.AuthMode``.
        :param default_user_settings: ``AWS::SageMaker::Domain.DefaultUserSettings``.
        :param domain_name: ``AWS::SageMaker::Domain.DomainName``.
        :param kms_key_id: ``AWS::SageMaker::Domain.KmsKeyId``.
        :param subnet_ids: ``AWS::SageMaker::Domain.SubnetIds``.
        :param tags: ``AWS::SageMaker::Domain.Tags``.
        :param vpc_id: ``AWS::SageMaker::Domain.VpcId``.
        '''
        props = CfnDomainProps(
            app_network_access_type=app_network_access_type,
            auth_mode=auth_mode,
            default_user_settings=default_user_settings,
            domain_name=domain_name,
            kms_key_id=kms_key_id,
            subnet_ids=subnet_ids,
            tags=tags,
            vpc_id=vpc_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appNetworkAccessType")
    def app_network_access_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Domain.AppNetworkAccessType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-appnetworkaccesstype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appNetworkAccessType"))

    @app_network_access_type.setter
    def app_network_access_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "appNetworkAccessType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDomainArn")
    def attr_domain_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHomeEfsFileSystemId")
    def attr_home_efs_file_system_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: HomeEfsFileSystemId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHomeEfsFileSystemId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSingleSignOnManagedApplicationInstanceId")
    def attr_single_sign_on_managed_application_instance_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SingleSignOnManagedApplicationInstanceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSingleSignOnManagedApplicationInstanceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: Url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="authMode")
    def auth_mode(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.AuthMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-authmode
        '''
        return typing.cast(builtins.str, jsii.get(self, "authMode"))

    @auth_mode.setter
    def auth_mode(self, value: builtins.str) -> None:
        jsii.set(self, "authMode", value)

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultUserSettings")
    def default_user_settings(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDomain.UserSettingsProperty"]:
        '''``AWS::SageMaker::Domain.DefaultUserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-defaultusersettings
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDomain.UserSettingsProperty"], jsii.get(self, "defaultUserSettings"))

    @default_user_settings.setter
    def default_user_settings(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDomain.UserSettingsProperty"],
    ) -> None:
        jsii.set(self, "defaultUserSettings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Domain.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::SageMaker::Domain.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "subnetIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-vpcid
        '''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        jsii.set(self, "vpcId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.CustomImageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_image_config_name": "appImageConfigName",
            "image_name": "imageName",
            "image_version_number": "imageVersionNumber",
        },
    )
    class CustomImageProperty:
        def __init__(
            self,
            *,
            app_image_config_name: builtins.str,
            image_name: builtins.str,
            image_version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param app_image_config_name: ``CfnDomain.CustomImageProperty.AppImageConfigName``.
            :param image_name: ``CfnDomain.CustomImageProperty.ImageName``.
            :param image_version_number: ``CfnDomain.CustomImageProperty.ImageVersionNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                custom_image_property = sagemaker.CfnDomain.CustomImageProperty(
                    app_image_config_name="appImageConfigName",
                    image_name="imageName",
                
                    # the properties below are optional
                    image_version_number=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_image_config_name": app_image_config_name,
                "image_name": image_name,
            }
            if image_version_number is not None:
                self._values["image_version_number"] = image_version_number

        @builtins.property
        def app_image_config_name(self) -> builtins.str:
            '''``CfnDomain.CustomImageProperty.AppImageConfigName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-appimageconfigname
            '''
            result = self._values.get("app_image_config_name")
            assert result is not None, "Required property 'app_image_config_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_name(self) -> builtins.str:
            '''``CfnDomain.CustomImageProperty.ImageName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-imagename
            '''
            result = self._values.get("image_name")
            assert result is not None, "Required property 'image_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_version_number(self) -> typing.Optional[jsii.Number]:
            '''``CfnDomain.CustomImageProperty.ImageVersionNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-imageversionnumber
            '''
            result = self._values.get("image_version_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomImageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.JupyterServerAppSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"default_resource_spec": "defaultResourceSpec"},
    )
    class JupyterServerAppSettingsProperty:
        def __init__(
            self,
            *,
            default_resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]] = None,
        ) -> None:
            '''
            :param default_resource_spec: ``CfnDomain.JupyterServerAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-jupyterserverappsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                jupyter_server_app_settings_property = sagemaker.CfnDomain.JupyterServerAppSettingsProperty(
                    default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                        instance_type="instanceType",
                        sage_maker_image_arn="sageMakerImageArn",
                        sage_maker_image_version_arn="sageMakerImageVersionArn"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_resource_spec is not None:
                self._values["default_resource_spec"] = default_resource_spec

        @builtins.property
        def default_resource_spec(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]]:
            '''``CfnDomain.JupyterServerAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-jupyterserverappsettings.html#cfn-sagemaker-domain-jupyterserverappsettings-defaultresourcespec
            '''
            result = self._values.get("default_resource_spec")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JupyterServerAppSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.KernelGatewayAppSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_images": "customImages",
            "default_resource_spec": "defaultResourceSpec",
        },
    )
    class KernelGatewayAppSettingsProperty:
        def __init__(
            self,
            *,
            custom_images: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.CustomImageProperty"]]]] = None,
            default_resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]] = None,
        ) -> None:
            '''
            :param custom_images: ``CfnDomain.KernelGatewayAppSettingsProperty.CustomImages``.
            :param default_resource_spec: ``CfnDomain.KernelGatewayAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                kernel_gateway_app_settings_property = sagemaker.CfnDomain.KernelGatewayAppSettingsProperty(
                    custom_images=[sagemaker.CfnDomain.CustomImageProperty(
                        app_image_config_name="appImageConfigName",
                        image_name="imageName",
                
                        # the properties below are optional
                        image_version_number=123
                    )],
                    default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                        instance_type="instanceType",
                        sage_maker_image_arn="sageMakerImageArn",
                        sage_maker_image_version_arn="sageMakerImageVersionArn"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_images is not None:
                self._values["custom_images"] = custom_images
            if default_resource_spec is not None:
                self._values["default_resource_spec"] = default_resource_spec

        @builtins.property
        def custom_images(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.CustomImageProperty"]]]]:
            '''``CfnDomain.KernelGatewayAppSettingsProperty.CustomImages``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html#cfn-sagemaker-domain-kernelgatewayappsettings-customimages
            '''
            result = self._values.get("custom_images")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.CustomImageProperty"]]]], result)

        @builtins.property
        def default_resource_spec(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]]:
            '''``CfnDomain.KernelGatewayAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html#cfn-sagemaker-domain-kernelgatewayappsettings-defaultresourcespec
            '''
            result = self._values.get("default_resource_spec")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KernelGatewayAppSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.ResourceSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "sage_maker_image_arn": "sageMakerImageArn",
            "sage_maker_image_version_arn": "sageMakerImageVersionArn",
        },
    )
    class ResourceSpecProperty:
        def __init__(
            self,
            *,
            instance_type: typing.Optional[builtins.str] = None,
            sage_maker_image_arn: typing.Optional[builtins.str] = None,
            sage_maker_image_version_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_type: ``CfnDomain.ResourceSpecProperty.InstanceType``.
            :param sage_maker_image_arn: ``CfnDomain.ResourceSpecProperty.SageMakerImageArn``.
            :param sage_maker_image_version_arn: ``CfnDomain.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                resource_spec_property = sagemaker.CfnDomain.ResourceSpecProperty(
                    instance_type="instanceType",
                    sage_maker_image_arn="sageMakerImageArn",
                    sage_maker_image_version_arn="sageMakerImageVersionArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if sage_maker_image_arn is not None:
                self._values["sage_maker_image_arn"] = sage_maker_image_arn
            if sage_maker_image_version_arn is not None:
                self._values["sage_maker_image_version_arn"] = sage_maker_image_version_arn

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.ResourceSpecProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.ResourceSpecProperty.SageMakerImageArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-sagemakerimagearn
            '''
            result = self._values.get("sage_maker_image_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_version_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-sagemakerimageversionarn
            '''
            result = self._values.get("sage_maker_image_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.SharingSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "notebook_output_option": "notebookOutputOption",
            "s3_kms_key_id": "s3KmsKeyId",
            "s3_output_path": "s3OutputPath",
        },
    )
    class SharingSettingsProperty:
        def __init__(
            self,
            *,
            notebook_output_option: typing.Optional[builtins.str] = None,
            s3_kms_key_id: typing.Optional[builtins.str] = None,
            s3_output_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param notebook_output_option: ``CfnDomain.SharingSettingsProperty.NotebookOutputOption``.
            :param s3_kms_key_id: ``CfnDomain.SharingSettingsProperty.S3KmsKeyId``.
            :param s3_output_path: ``CfnDomain.SharingSettingsProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                sharing_settings_property = sagemaker.CfnDomain.SharingSettingsProperty(
                    notebook_output_option="notebookOutputOption",
                    s3_kms_key_id="s3KmsKeyId",
                    s3_output_path="s3OutputPath"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if notebook_output_option is not None:
                self._values["notebook_output_option"] = notebook_output_option
            if s3_kms_key_id is not None:
                self._values["s3_kms_key_id"] = s3_kms_key_id
            if s3_output_path is not None:
                self._values["s3_output_path"] = s3_output_path

        @builtins.property
        def notebook_output_option(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.SharingSettingsProperty.NotebookOutputOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-notebookoutputoption
            '''
            result = self._values.get("notebook_output_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.SharingSettingsProperty.S3KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-s3kmskeyid
            '''
            result = self._values.get("s3_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_output_path(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.SharingSettingsProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-s3outputpath
            '''
            result = self._values.get("s3_output_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SharingSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.UserSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_role": "executionRole",
            "jupyter_server_app_settings": "jupyterServerAppSettings",
            "kernel_gateway_app_settings": "kernelGatewayAppSettings",
            "security_groups": "securityGroups",
            "sharing_settings": "sharingSettings",
        },
    )
    class UserSettingsProperty:
        def __init__(
            self,
            *,
            execution_role: typing.Optional[builtins.str] = None,
            jupyter_server_app_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.JupyterServerAppSettingsProperty"]] = None,
            kernel_gateway_app_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.KernelGatewayAppSettingsProperty"]] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            sharing_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.SharingSettingsProperty"]] = None,
        ) -> None:
            '''
            :param execution_role: ``CfnDomain.UserSettingsProperty.ExecutionRole``.
            :param jupyter_server_app_settings: ``CfnDomain.UserSettingsProperty.JupyterServerAppSettings``.
            :param kernel_gateway_app_settings: ``CfnDomain.UserSettingsProperty.KernelGatewayAppSettings``.
            :param security_groups: ``CfnDomain.UserSettingsProperty.SecurityGroups``.
            :param sharing_settings: ``CfnDomain.UserSettingsProperty.SharingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                user_settings_property = sagemaker.CfnDomain.UserSettingsProperty(
                    execution_role="executionRole",
                    jupyter_server_app_settings=sagemaker.CfnDomain.JupyterServerAppSettingsProperty(
                        default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                            instance_type="instanceType",
                            sage_maker_image_arn="sageMakerImageArn",
                            sage_maker_image_version_arn="sageMakerImageVersionArn"
                        )
                    ),
                    kernel_gateway_app_settings=sagemaker.CfnDomain.KernelGatewayAppSettingsProperty(
                        custom_images=[sagemaker.CfnDomain.CustomImageProperty(
                            app_image_config_name="appImageConfigName",
                            image_name="imageName",
                
                            # the properties below are optional
                            image_version_number=123
                        )],
                        default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                            instance_type="instanceType",
                            sage_maker_image_arn="sageMakerImageArn",
                            sage_maker_image_version_arn="sageMakerImageVersionArn"
                        )
                    ),
                    security_groups=["securityGroups"],
                    sharing_settings=sagemaker.CfnDomain.SharingSettingsProperty(
                        notebook_output_option="notebookOutputOption",
                        s3_kms_key_id="s3KmsKeyId",
                        s3_output_path="s3OutputPath"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if execution_role is not None:
                self._values["execution_role"] = execution_role
            if jupyter_server_app_settings is not None:
                self._values["jupyter_server_app_settings"] = jupyter_server_app_settings
            if kernel_gateway_app_settings is not None:
                self._values["kernel_gateway_app_settings"] = kernel_gateway_app_settings
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if sharing_settings is not None:
                self._values["sharing_settings"] = sharing_settings

        @builtins.property
        def execution_role(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.UserSettingsProperty.ExecutionRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-executionrole
            '''
            result = self._values.get("execution_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def jupyter_server_app_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.JupyterServerAppSettingsProperty"]]:
            '''``CfnDomain.UserSettingsProperty.JupyterServerAppSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-jupyterserverappsettings
            '''
            result = self._values.get("jupyter_server_app_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.JupyterServerAppSettingsProperty"]], result)

        @builtins.property
        def kernel_gateway_app_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.KernelGatewayAppSettingsProperty"]]:
            '''``CfnDomain.UserSettingsProperty.KernelGatewayAppSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-kernelgatewayappsettings
            '''
            result = self._values.get("kernel_gateway_app_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.KernelGatewayAppSettingsProperty"]], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDomain.UserSettingsProperty.SecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def sharing_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.SharingSettingsProperty"]]:
            '''``CfnDomain.UserSettingsProperty.SharingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-sharingsettings
            '''
            result = self._values.get("sharing_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.SharingSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_network_access_type": "appNetworkAccessType",
        "auth_mode": "authMode",
        "default_user_settings": "defaultUserSettings",
        "domain_name": "domainName",
        "kms_key_id": "kmsKeyId",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "vpc_id": "vpcId",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        app_network_access_type: typing.Optional[builtins.str] = None,
        auth_mode: builtins.str,
        default_user_settings: typing.Union[aws_cdk.core.IResolvable, CfnDomain.UserSettingsProperty],
        domain_name: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Domain``.

        :param app_network_access_type: ``AWS::SageMaker::Domain.AppNetworkAccessType``.
        :param auth_mode: ``AWS::SageMaker::Domain.AuthMode``.
        :param default_user_settings: ``AWS::SageMaker::Domain.DefaultUserSettings``.
        :param domain_name: ``AWS::SageMaker::Domain.DomainName``.
        :param kms_key_id: ``AWS::SageMaker::Domain.KmsKeyId``.
        :param subnet_ids: ``AWS::SageMaker::Domain.SubnetIds``.
        :param tags: ``AWS::SageMaker::Domain.Tags``.
        :param vpc_id: ``AWS::SageMaker::Domain.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_domain_props = sagemaker.CfnDomainProps(
                auth_mode="authMode",
                default_user_settings=sagemaker.CfnDomain.UserSettingsProperty(
                    execution_role="executionRole",
                    jupyter_server_app_settings=sagemaker.CfnDomain.JupyterServerAppSettingsProperty(
                        default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                            instance_type="instanceType",
                            sage_maker_image_arn="sageMakerImageArn",
                            sage_maker_image_version_arn="sageMakerImageVersionArn"
                        )
                    ),
                    kernel_gateway_app_settings=sagemaker.CfnDomain.KernelGatewayAppSettingsProperty(
                        custom_images=[sagemaker.CfnDomain.CustomImageProperty(
                            app_image_config_name="appImageConfigName",
                            image_name="imageName",
            
                            # the properties below are optional
                            image_version_number=123
                        )],
                        default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                            instance_type="instanceType",
                            sage_maker_image_arn="sageMakerImageArn",
                            sage_maker_image_version_arn="sageMakerImageVersionArn"
                        )
                    ),
                    security_groups=["securityGroups"],
                    sharing_settings=sagemaker.CfnDomain.SharingSettingsProperty(
                        notebook_output_option="notebookOutputOption",
                        s3_kms_key_id="s3KmsKeyId",
                        s3_output_path="s3OutputPath"
                    )
                ),
                domain_name="domainName",
                subnet_ids=["subnetIds"],
                vpc_id="vpcId",
            
                # the properties below are optional
                app_network_access_type="appNetworkAccessType",
                kms_key_id="kmsKeyId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "auth_mode": auth_mode,
            "default_user_settings": default_user_settings,
            "domain_name": domain_name,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
        }
        if app_network_access_type is not None:
            self._values["app_network_access_type"] = app_network_access_type
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_network_access_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Domain.AppNetworkAccessType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-appnetworkaccesstype
        '''
        result = self._values.get("app_network_access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_mode(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.AuthMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-authmode
        '''
        result = self._values.get("auth_mode")
        assert result is not None, "Required property 'auth_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_user_settings(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDomain.UserSettingsProperty]:
        '''``AWS::SageMaker::Domain.DefaultUserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-defaultusersettings
        '''
        result = self._values.get("default_user_settings")
        assert result is not None, "Required property 'default_user_settings' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDomain.UserSettingsProperty], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Domain.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::SageMaker::Domain.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEndpoint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint",
):
    '''A CloudFormation ``AWS::SageMaker::Endpoint``.

    :cloudformationResource: AWS::SageMaker::Endpoint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_endpoint = sagemaker.CfnEndpoint(self, "MyCfnEndpoint",
            endpoint_config_name="endpointConfigName",
        
            # the properties below are optional
            deployment_config=sagemaker.CfnEndpoint.DeploymentConfigProperty(
                blue_green_update_policy=sagemaker.CfnEndpoint.BlueGreenUpdatePolicyProperty(
                    traffic_routing_configuration=sagemaker.CfnEndpoint.TrafficRoutingConfigProperty(
                        type="type",
        
                        # the properties below are optional
                        canary_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                            type="type",
                            value=123
                        ),
                        linear_step_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                            type="type",
                            value=123
                        ),
                        wait_interval_in_seconds=123
                    ),
        
                    # the properties below are optional
                    maximum_execution_timeout_in_seconds=123,
                    termination_wait_in_seconds=123
                ),
        
                # the properties below are optional
                auto_rollback_configuration=sagemaker.CfnEndpoint.AutoRollbackConfigProperty(
                    alarms=[sagemaker.CfnEndpoint.AlarmProperty(
                        alarm_name="alarmName"
                    )]
                )
            ),
            endpoint_name="endpointName",
            exclude_retained_variant_properties=[sagemaker.CfnEndpoint.VariantPropertyProperty(
                variant_property_type="variantPropertyType"
            )],
            retain_all_variant_properties=False,
            retain_deployment_config=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        deployment_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]] = None,
        endpoint_config_name: builtins.str,
        endpoint_name: typing.Optional[builtins.str] = None,
        exclude_retained_variant_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]] = None,
        retain_all_variant_properties: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        retain_deployment_config: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Endpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param deployment_config: ``AWS::SageMaker::Endpoint.DeploymentConfig``.
        :param endpoint_config_name: ``AWS::SageMaker::Endpoint.EndpointConfigName``.
        :param endpoint_name: ``AWS::SageMaker::Endpoint.EndpointName``.
        :param exclude_retained_variant_properties: ``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.
        :param retain_all_variant_properties: ``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.
        :param retain_deployment_config: ``AWS::SageMaker::Endpoint.RetainDeploymentConfig``.
        :param tags: ``AWS::SageMaker::Endpoint.Tags``.
        '''
        props = CfnEndpointProps(
            deployment_config=deployment_config,
            endpoint_config_name=endpoint_config_name,
            endpoint_name=endpoint_name,
            exclude_retained_variant_properties=exclude_retained_variant_properties,
            retain_all_variant_properties=retain_all_variant_properties,
            retain_deployment_config=retain_deployment_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEndpointName")
    def attr_endpoint_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: EndpointName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]]:
        '''``AWS::SageMaker::Endpoint.DeploymentConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-deploymentconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]], jsii.get(self, "deploymentConfig"))

    @deployment_config.setter
    def deployment_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]],
    ) -> None:
        jsii.set(self, "deploymentConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> builtins.str:
        '''``AWS::SageMaker::Endpoint.EndpointConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointconfigname
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointConfigName"))

    @endpoint_config_name.setter
    def endpoint_config_name(self, value: builtins.str) -> None:
        jsii.set(self, "endpointConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Endpoint.EndpointName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointName"))

    @endpoint_name.setter
    def endpoint_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeRetainedVariantProperties")
    def exclude_retained_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]]:
        '''``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-excluderetainedvariantproperties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]], jsii.get(self, "excludeRetainedVariantProperties"))

    @exclude_retained_variant_properties.setter
    def exclude_retained_variant_properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]],
    ) -> None:
        jsii.set(self, "excludeRetainedVariantProperties", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="retainAllVariantProperties")
    def retain_all_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retainallvariantproperties
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "retainAllVariantProperties"))

    @retain_all_variant_properties.setter
    def retain_all_variant_properties(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "retainAllVariantProperties", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="retainDeploymentConfig")
    def retain_deployment_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Endpoint.RetainDeploymentConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retaindeploymentconfig
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "retainDeploymentConfig"))

    @retain_deployment_config.setter
    def retain_deployment_config(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "retainDeploymentConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Endpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.AlarmProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_name": "alarmName"},
    )
    class AlarmProperty:
        def __init__(self, *, alarm_name: builtins.str) -> None:
            '''
            :param alarm_name: ``CfnEndpoint.AlarmProperty.AlarmName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                alarm_property = sagemaker.CfnEndpoint.AlarmProperty(
                    alarm_name="alarmName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "alarm_name": alarm_name,
            }

        @builtins.property
        def alarm_name(self) -> builtins.str:
            '''``CfnEndpoint.AlarmProperty.AlarmName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html#cfn-sagemaker-endpoint-alarm-alarmname
            '''
            result = self._values.get("alarm_name")
            assert result is not None, "Required property 'alarm_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.AutoRollbackConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"alarms": "alarms"},
    )
    class AutoRollbackConfigProperty:
        def __init__(
            self,
            *,
            alarms: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AlarmProperty"]]],
        ) -> None:
            '''
            :param alarms: ``CfnEndpoint.AutoRollbackConfigProperty.Alarms``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                auto_rollback_config_property = sagemaker.CfnEndpoint.AutoRollbackConfigProperty(
                    alarms=[sagemaker.CfnEndpoint.AlarmProperty(
                        alarm_name="alarmName"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "alarms": alarms,
            }

        @builtins.property
        def alarms(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AlarmProperty"]]]:
            '''``CfnEndpoint.AutoRollbackConfigProperty.Alarms``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html#cfn-sagemaker-endpoint-autorollbackconfig-alarms
            '''
            result = self._values.get("alarms")
            assert result is not None, "Required property 'alarms' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AlarmProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoRollbackConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.BlueGreenUpdatePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maximum_execution_timeout_in_seconds": "maximumExecutionTimeoutInSeconds",
            "termination_wait_in_seconds": "terminationWaitInSeconds",
            "traffic_routing_configuration": "trafficRoutingConfiguration",
        },
    )
    class BlueGreenUpdatePolicyProperty:
        def __init__(
            self,
            *,
            maximum_execution_timeout_in_seconds: typing.Optional[jsii.Number] = None,
            termination_wait_in_seconds: typing.Optional[jsii.Number] = None,
            traffic_routing_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.TrafficRoutingConfigProperty"],
        ) -> None:
            '''
            :param maximum_execution_timeout_in_seconds: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.MaximumExecutionTimeoutInSeconds``.
            :param termination_wait_in_seconds: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.TerminationWaitInSeconds``.
            :param traffic_routing_configuration: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.TrafficRoutingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                blue_green_update_policy_property = sagemaker.CfnEndpoint.BlueGreenUpdatePolicyProperty(
                    traffic_routing_configuration=sagemaker.CfnEndpoint.TrafficRoutingConfigProperty(
                        type="type",
                
                        # the properties below are optional
                        canary_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                            type="type",
                            value=123
                        ),
                        linear_step_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                            type="type",
                            value=123
                        ),
                        wait_interval_in_seconds=123
                    ),
                
                    # the properties below are optional
                    maximum_execution_timeout_in_seconds=123,
                    termination_wait_in_seconds=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "traffic_routing_configuration": traffic_routing_configuration,
            }
            if maximum_execution_timeout_in_seconds is not None:
                self._values["maximum_execution_timeout_in_seconds"] = maximum_execution_timeout_in_seconds
            if termination_wait_in_seconds is not None:
                self._values["termination_wait_in_seconds"] = termination_wait_in_seconds

        @builtins.property
        def maximum_execution_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnEndpoint.BlueGreenUpdatePolicyProperty.MaximumExecutionTimeoutInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-maximumexecutiontimeoutinseconds
            '''
            result = self._values.get("maximum_execution_timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def termination_wait_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnEndpoint.BlueGreenUpdatePolicyProperty.TerminationWaitInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-terminationwaitinseconds
            '''
            result = self._values.get("termination_wait_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def traffic_routing_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.TrafficRoutingConfigProperty"]:
            '''``CfnEndpoint.BlueGreenUpdatePolicyProperty.TrafficRoutingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-trafficroutingconfiguration
            '''
            result = self._values.get("traffic_routing_configuration")
            assert result is not None, "Required property 'traffic_routing_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.TrafficRoutingConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlueGreenUpdatePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.CapacitySizeProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class CapacitySizeProperty:
        def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
            '''
            :param type: ``CfnEndpoint.CapacitySizeProperty.Type``.
            :param value: ``CfnEndpoint.CapacitySizeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                capacity_size_property = sagemaker.CfnEndpoint.CapacitySizeProperty(
                    type="type",
                    value=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnEndpoint.CapacitySizeProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html#cfn-sagemaker-endpoint-capacitysize-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''``CfnEndpoint.CapacitySizeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html#cfn-sagemaker-endpoint-capacitysize-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacitySizeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.DeploymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_rollback_configuration": "autoRollbackConfiguration",
            "blue_green_update_policy": "blueGreenUpdatePolicy",
        },
    )
    class DeploymentConfigProperty:
        def __init__(
            self,
            *,
            auto_rollback_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AutoRollbackConfigProperty"]] = None,
            blue_green_update_policy: typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.BlueGreenUpdatePolicyProperty"],
        ) -> None:
            '''
            :param auto_rollback_configuration: ``CfnEndpoint.DeploymentConfigProperty.AutoRollbackConfiguration``.
            :param blue_green_update_policy: ``CfnEndpoint.DeploymentConfigProperty.BlueGreenUpdatePolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                deployment_config_property = sagemaker.CfnEndpoint.DeploymentConfigProperty(
                    blue_green_update_policy=sagemaker.CfnEndpoint.BlueGreenUpdatePolicyProperty(
                        traffic_routing_configuration=sagemaker.CfnEndpoint.TrafficRoutingConfigProperty(
                            type="type",
                
                            # the properties below are optional
                            canary_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                                type="type",
                                value=123
                            ),
                            linear_step_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                                type="type",
                                value=123
                            ),
                            wait_interval_in_seconds=123
                        ),
                
                        # the properties below are optional
                        maximum_execution_timeout_in_seconds=123,
                        termination_wait_in_seconds=123
                    ),
                
                    # the properties below are optional
                    auto_rollback_configuration=sagemaker.CfnEndpoint.AutoRollbackConfigProperty(
                        alarms=[sagemaker.CfnEndpoint.AlarmProperty(
                            alarm_name="alarmName"
                        )]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "blue_green_update_policy": blue_green_update_policy,
            }
            if auto_rollback_configuration is not None:
                self._values["auto_rollback_configuration"] = auto_rollback_configuration

        @builtins.property
        def auto_rollback_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AutoRollbackConfigProperty"]]:
            '''``CfnEndpoint.DeploymentConfigProperty.AutoRollbackConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-autorollbackconfiguration
            '''
            result = self._values.get("auto_rollback_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AutoRollbackConfigProperty"]], result)

        @builtins.property
        def blue_green_update_policy(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.BlueGreenUpdatePolicyProperty"]:
            '''``CfnEndpoint.DeploymentConfigProperty.BlueGreenUpdatePolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-bluegreenupdatepolicy
            '''
            result = self._values.get("blue_green_update_policy")
            assert result is not None, "Required property 'blue_green_update_policy' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.BlueGreenUpdatePolicyProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.TrafficRoutingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "canary_size": "canarySize",
            "linear_step_size": "linearStepSize",
            "type": "type",
            "wait_interval_in_seconds": "waitIntervalInSeconds",
        },
    )
    class TrafficRoutingConfigProperty:
        def __init__(
            self,
            *,
            canary_size: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]] = None,
            linear_step_size: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]] = None,
            type: builtins.str,
            wait_interval_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param canary_size: ``CfnEndpoint.TrafficRoutingConfigProperty.CanarySize``.
            :param linear_step_size: ``CfnEndpoint.TrafficRoutingConfigProperty.LinearStepSize``.
            :param type: ``CfnEndpoint.TrafficRoutingConfigProperty.Type``.
            :param wait_interval_in_seconds: ``CfnEndpoint.TrafficRoutingConfigProperty.WaitIntervalInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                traffic_routing_config_property = sagemaker.CfnEndpoint.TrafficRoutingConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    canary_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                        type="type",
                        value=123
                    ),
                    linear_step_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                        type="type",
                        value=123
                    ),
                    wait_interval_in_seconds=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if canary_size is not None:
                self._values["canary_size"] = canary_size
            if linear_step_size is not None:
                self._values["linear_step_size"] = linear_step_size
            if wait_interval_in_seconds is not None:
                self._values["wait_interval_in_seconds"] = wait_interval_in_seconds

        @builtins.property
        def canary_size(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]]:
            '''``CfnEndpoint.TrafficRoutingConfigProperty.CanarySize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-canarysize
            '''
            result = self._values.get("canary_size")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]], result)

        @builtins.property
        def linear_step_size(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]]:
            '''``CfnEndpoint.TrafficRoutingConfigProperty.LinearStepSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-linearstepsize
            '''
            result = self._values.get("linear_step_size")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnEndpoint.TrafficRoutingConfigProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def wait_interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnEndpoint.TrafficRoutingConfigProperty.WaitIntervalInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-waitintervalinseconds
            '''
            result = self._values.get("wait_interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrafficRoutingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.VariantPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"variant_property_type": "variantPropertyType"},
    )
    class VariantPropertyProperty:
        def __init__(
            self,
            *,
            variant_property_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param variant_property_type: ``CfnEndpoint.VariantPropertyProperty.VariantPropertyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                variant_property_property = sagemaker.CfnEndpoint.VariantPropertyProperty(
                    variant_property_type="variantPropertyType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if variant_property_type is not None:
                self._values["variant_property_type"] = variant_property_type

        @builtins.property
        def variant_property_type(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpoint.VariantPropertyProperty.VariantPropertyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html#cfn-sagemaker-endpoint-variantproperty-variantpropertytype
            '''
            result = self._values.get("variant_property_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariantPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEndpointConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig",
):
    '''A CloudFormation ``AWS::SageMaker::EndpointConfig``.

    :cloudformationResource: AWS::SageMaker::EndpointConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_endpoint_config = sagemaker.CfnEndpointConfig(self, "MyCfnEndpointConfig",
            production_variants=[sagemaker.CfnEndpointConfig.ProductionVariantProperty(
                initial_variant_weight=123,
                model_name="modelName",
                variant_name="variantName",
        
                # the properties below are optional
                accelerator_type="acceleratorType",
                initial_instance_count=123,
                instance_type="instanceType",
                serverless_config=sagemaker.CfnEndpointConfig.ServerlessConfigProperty(
                    max_concurrency=123,
                    memory_size_in_mb=123
                )
            )],
        
            # the properties below are optional
            async_inference_config=sagemaker.CfnEndpointConfig.AsyncInferenceConfigProperty(
                output_config=sagemaker.CfnEndpointConfig.AsyncInferenceOutputConfigProperty(
                    s3_output_path="s3OutputPath",
        
                    # the properties below are optional
                    kms_key_id="kmsKeyId",
                    notification_config=sagemaker.CfnEndpointConfig.AsyncInferenceNotificationConfigProperty(
                        error_topic="errorTopic",
                        success_topic="successTopic"
                    )
                ),
        
                # the properties below are optional
                client_config=sagemaker.CfnEndpointConfig.AsyncInferenceClientConfigProperty(
                    max_concurrent_invocations_per_instance=123
                )
            ),
            data_capture_config=sagemaker.CfnEndpointConfig.DataCaptureConfigProperty(
                capture_options=[sagemaker.CfnEndpointConfig.CaptureOptionProperty(
                    capture_mode="captureMode"
                )],
                destination_s3_uri="destinationS3Uri",
                initial_sampling_percentage=123,
        
                # the properties below are optional
                capture_content_type_header=sagemaker.CfnEndpointConfig.CaptureContentTypeHeaderProperty(
                    csv_content_types=["csvContentTypes"],
                    json_content_types=["jsonContentTypes"]
                ),
                enable_capture=False,
                kms_key_id="kmsKeyId"
            ),
            endpoint_config_name="endpointConfigName",
            kms_key_id="kmsKeyId",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        async_inference_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceConfigProperty"]] = None,
        data_capture_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]] = None,
        endpoint_config_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        production_variants: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]],
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::EndpointConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param async_inference_config: ``AWS::SageMaker::EndpointConfig.AsyncInferenceConfig``.
        :param data_capture_config: ``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.
        :param endpoint_config_name: ``AWS::SageMaker::EndpointConfig.EndpointConfigName``.
        :param kms_key_id: ``AWS::SageMaker::EndpointConfig.KmsKeyId``.
        :param production_variants: ``AWS::SageMaker::EndpointConfig.ProductionVariants``.
        :param tags: ``AWS::SageMaker::EndpointConfig.Tags``.
        '''
        props = CfnEndpointConfigProps(
            async_inference_config=async_inference_config,
            data_capture_config=data_capture_config,
            endpoint_config_name=endpoint_config_name,
            kms_key_id=kms_key_id,
            production_variants=production_variants,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="asyncInferenceConfig")
    def async_inference_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceConfigProperty"]]:
        '''``AWS::SageMaker::EndpointConfig.AsyncInferenceConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceConfigProperty"]], jsii.get(self, "asyncInferenceConfig"))

    @async_inference_config.setter
    def async_inference_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceConfigProperty"]],
    ) -> None:
        jsii.set(self, "asyncInferenceConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEndpointConfigName")
    def attr_endpoint_config_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: EndpointConfigName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointConfigName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataCaptureConfig")
    def data_capture_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]]:
        '''``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]], jsii.get(self, "dataCaptureConfig"))

    @data_capture_config.setter
    def data_capture_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]],
    ) -> None:
        jsii.set(self, "dataCaptureConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::EndpointConfig.EndpointConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-endpointconfigname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointConfigName"))

    @endpoint_config_name.setter
    def endpoint_config_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::EndpointConfig.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="productionVariants")
    def production_variants(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]]:
        '''``AWS::SageMaker::EndpointConfig.ProductionVariants``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-productionvariants
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]], jsii.get(self, "productionVariants"))

    @production_variants.setter
    def production_variants(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]],
    ) -> None:
        jsii.set(self, "productionVariants", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::EndpointConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.AsyncInferenceClientConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_concurrent_invocations_per_instance": "maxConcurrentInvocationsPerInstance",
        },
    )
    class AsyncInferenceClientConfigProperty:
        def __init__(
            self,
            *,
            max_concurrent_invocations_per_instance: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param max_concurrent_invocations_per_instance: ``CfnEndpointConfig.AsyncInferenceClientConfigProperty.MaxConcurrentInvocationsPerInstance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                async_inference_client_config_property = sagemaker.CfnEndpointConfig.AsyncInferenceClientConfigProperty(
                    max_concurrent_invocations_per_instance=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if max_concurrent_invocations_per_instance is not None:
                self._values["max_concurrent_invocations_per_instance"] = max_concurrent_invocations_per_instance

        @builtins.property
        def max_concurrent_invocations_per_instance(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''``CfnEndpointConfig.AsyncInferenceClientConfigProperty.MaxConcurrentInvocationsPerInstance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceclientconfig-maxconcurrentinvocationsperinstance
            '''
            result = self._values.get("max_concurrent_invocations_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AsyncInferenceClientConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.AsyncInferenceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_config": "clientConfig",
            "output_config": "outputConfig",
        },
    )
    class AsyncInferenceConfigProperty:
        def __init__(
            self,
            *,
            client_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceClientConfigProperty"]] = None,
            output_config: typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceOutputConfigProperty"],
        ) -> None:
            '''
            :param client_config: ``CfnEndpointConfig.AsyncInferenceConfigProperty.ClientConfig``.
            :param output_config: ``CfnEndpointConfig.AsyncInferenceConfigProperty.OutputConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                async_inference_config_property = sagemaker.CfnEndpointConfig.AsyncInferenceConfigProperty(
                    output_config=sagemaker.CfnEndpointConfig.AsyncInferenceOutputConfigProperty(
                        s3_output_path="s3OutputPath",
                
                        # the properties below are optional
                        kms_key_id="kmsKeyId",
                        notification_config=sagemaker.CfnEndpointConfig.AsyncInferenceNotificationConfigProperty(
                            error_topic="errorTopic",
                            success_topic="successTopic"
                        )
                    ),
                
                    # the properties below are optional
                    client_config=sagemaker.CfnEndpointConfig.AsyncInferenceClientConfigProperty(
                        max_concurrent_invocations_per_instance=123
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "output_config": output_config,
            }
            if client_config is not None:
                self._values["client_config"] = client_config

        @builtins.property
        def client_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceClientConfigProperty"]]:
            '''``CfnEndpointConfig.AsyncInferenceConfigProperty.ClientConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceconfig-clientconfig
            '''
            result = self._values.get("client_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceClientConfigProperty"]], result)

        @builtins.property
        def output_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceOutputConfigProperty"]:
            '''``CfnEndpointConfig.AsyncInferenceConfigProperty.OutputConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceconfig-outputconfig
            '''
            result = self._values.get("output_config")
            assert result is not None, "Required property 'output_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceOutputConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AsyncInferenceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.AsyncInferenceNotificationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"error_topic": "errorTopic", "success_topic": "successTopic"},
    )
    class AsyncInferenceNotificationConfigProperty:
        def __init__(
            self,
            *,
            error_topic: typing.Optional[builtins.str] = None,
            success_topic: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param error_topic: ``CfnEndpointConfig.AsyncInferenceNotificationConfigProperty.ErrorTopic``.
            :param success_topic: ``CfnEndpointConfig.AsyncInferenceNotificationConfigProperty.SuccessTopic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                async_inference_notification_config_property = sagemaker.CfnEndpointConfig.AsyncInferenceNotificationConfigProperty(
                    error_topic="errorTopic",
                    success_topic="successTopic"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if error_topic is not None:
                self._values["error_topic"] = error_topic
            if success_topic is not None:
                self._values["success_topic"] = success_topic

        @builtins.property
        def error_topic(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpointConfig.AsyncInferenceNotificationConfigProperty.ErrorTopic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-errortopic
            '''
            result = self._values.get("error_topic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def success_topic(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpointConfig.AsyncInferenceNotificationConfigProperty.SuccessTopic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-successtopic
            '''
            result = self._values.get("success_topic")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AsyncInferenceNotificationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.AsyncInferenceOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_id": "kmsKeyId",
            "notification_config": "notificationConfig",
            "s3_output_path": "s3OutputPath",
        },
    )
    class AsyncInferenceOutputConfigProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            notification_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceNotificationConfigProperty"]] = None,
            s3_output_path: builtins.str,
        ) -> None:
            '''
            :param kms_key_id: ``CfnEndpointConfig.AsyncInferenceOutputConfigProperty.KmsKeyId``.
            :param notification_config: ``CfnEndpointConfig.AsyncInferenceOutputConfigProperty.NotificationConfig``.
            :param s3_output_path: ``CfnEndpointConfig.AsyncInferenceOutputConfigProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                async_inference_output_config_property = sagemaker.CfnEndpointConfig.AsyncInferenceOutputConfigProperty(
                    s3_output_path="s3OutputPath",
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId",
                    notification_config=sagemaker.CfnEndpointConfig.AsyncInferenceNotificationConfigProperty(
                        error_topic="errorTopic",
                        success_topic="successTopic"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output_path": s3_output_path,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if notification_config is not None:
                self._values["notification_config"] = notification_config

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpointConfig.AsyncInferenceOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def notification_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceNotificationConfigProperty"]]:
            '''``CfnEndpointConfig.AsyncInferenceOutputConfigProperty.NotificationConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-notificationconfig
            '''
            result = self._values.get("notification_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.AsyncInferenceNotificationConfigProperty"]], result)

        @builtins.property
        def s3_output_path(self) -> builtins.str:
            '''``CfnEndpointConfig.AsyncInferenceOutputConfigProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3outputpath
            '''
            result = self._values.get("s3_output_path")
            assert result is not None, "Required property 's3_output_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AsyncInferenceOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.CaptureContentTypeHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_content_types": "csvContentTypes",
            "json_content_types": "jsonContentTypes",
        },
    )
    class CaptureContentTypeHeaderProperty:
        def __init__(
            self,
            *,
            csv_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            json_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param csv_content_types: ``CfnEndpointConfig.CaptureContentTypeHeaderProperty.CsvContentTypes``.
            :param json_content_types: ``CfnEndpointConfig.CaptureContentTypeHeaderProperty.JsonContentTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                capture_content_type_header_property = sagemaker.CfnEndpointConfig.CaptureContentTypeHeaderProperty(
                    csv_content_types=["csvContentTypes"],
                    json_content_types=["jsonContentTypes"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if csv_content_types is not None:
                self._values["csv_content_types"] = csv_content_types
            if json_content_types is not None:
                self._values["json_content_types"] = json_content_types

        @builtins.property
        def csv_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnEndpointConfig.CaptureContentTypeHeaderProperty.CsvContentTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-csvcontenttypes
            '''
            result = self._values.get("csv_content_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def json_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnEndpointConfig.CaptureContentTypeHeaderProperty.JsonContentTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-jsoncontenttypes
            '''
            result = self._values.get("json_content_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptureContentTypeHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.CaptureOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"capture_mode": "captureMode"},
    )
    class CaptureOptionProperty:
        def __init__(self, *, capture_mode: builtins.str) -> None:
            '''
            :param capture_mode: ``CfnEndpointConfig.CaptureOptionProperty.CaptureMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                capture_option_property = sagemaker.CfnEndpointConfig.CaptureOptionProperty(
                    capture_mode="captureMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "capture_mode": capture_mode,
            }

        @builtins.property
        def capture_mode(self) -> builtins.str:
            '''``CfnEndpointConfig.CaptureOptionProperty.CaptureMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html#cfn-sagemaker-endpointconfig-captureoption-capturemode
            '''
            result = self._values.get("capture_mode")
            assert result is not None, "Required property 'capture_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptureOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.DataCaptureConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capture_content_type_header": "captureContentTypeHeader",
            "capture_options": "captureOptions",
            "destination_s3_uri": "destinationS3Uri",
            "enable_capture": "enableCapture",
            "initial_sampling_percentage": "initialSamplingPercentage",
            "kms_key_id": "kmsKeyId",
        },
    )
    class DataCaptureConfigProperty:
        def __init__(
            self,
            *,
            capture_content_type_header: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureContentTypeHeaderProperty"]] = None,
            capture_options: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureOptionProperty"]]],
            destination_s3_uri: builtins.str,
            enable_capture: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            initial_sampling_percentage: jsii.Number,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param capture_content_type_header: ``CfnEndpointConfig.DataCaptureConfigProperty.CaptureContentTypeHeader``.
            :param capture_options: ``CfnEndpointConfig.DataCaptureConfigProperty.CaptureOptions``.
            :param destination_s3_uri: ``CfnEndpointConfig.DataCaptureConfigProperty.DestinationS3Uri``.
            :param enable_capture: ``CfnEndpointConfig.DataCaptureConfigProperty.EnableCapture``.
            :param initial_sampling_percentage: ``CfnEndpointConfig.DataCaptureConfigProperty.InitialSamplingPercentage``.
            :param kms_key_id: ``CfnEndpointConfig.DataCaptureConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                data_capture_config_property = sagemaker.CfnEndpointConfig.DataCaptureConfigProperty(
                    capture_options=[sagemaker.CfnEndpointConfig.CaptureOptionProperty(
                        capture_mode="captureMode"
                    )],
                    destination_s3_uri="destinationS3Uri",
                    initial_sampling_percentage=123,
                
                    # the properties below are optional
                    capture_content_type_header=sagemaker.CfnEndpointConfig.CaptureContentTypeHeaderProperty(
                        csv_content_types=["csvContentTypes"],
                        json_content_types=["jsonContentTypes"]
                    ),
                    enable_capture=False,
                    kms_key_id="kmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "capture_options": capture_options,
                "destination_s3_uri": destination_s3_uri,
                "initial_sampling_percentage": initial_sampling_percentage,
            }
            if capture_content_type_header is not None:
                self._values["capture_content_type_header"] = capture_content_type_header
            if enable_capture is not None:
                self._values["enable_capture"] = enable_capture
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def capture_content_type_header(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureContentTypeHeaderProperty"]]:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.CaptureContentTypeHeader``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader
            '''
            result = self._values.get("capture_content_type_header")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureContentTypeHeaderProperty"]], result)

        @builtins.property
        def capture_options(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureOptionProperty"]]]:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.CaptureOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-captureoptions
            '''
            result = self._values.get("capture_options")
            assert result is not None, "Required property 'capture_options' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureOptionProperty"]]], result)

        @builtins.property
        def destination_s3_uri(self) -> builtins.str:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.DestinationS3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-destinations3uri
            '''
            result = self._values.get("destination_s3_uri")
            assert result is not None, "Required property 'destination_s3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enable_capture(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.EnableCapture``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-enablecapture
            '''
            result = self._values.get("enable_capture")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def initial_sampling_percentage(self) -> jsii.Number:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.InitialSamplingPercentage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-initialsamplingpercentage
            '''
            result = self._values.get("initial_sampling_percentage")
            assert result is not None, "Required property 'initial_sampling_percentage' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCaptureConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.ProductionVariantProperty",
        jsii_struct_bases=[],
        name_mapping={
            "accelerator_type": "acceleratorType",
            "initial_instance_count": "initialInstanceCount",
            "initial_variant_weight": "initialVariantWeight",
            "instance_type": "instanceType",
            "model_name": "modelName",
            "serverless_config": "serverlessConfig",
            "variant_name": "variantName",
        },
    )
    class ProductionVariantProperty:
        def __init__(
            self,
            *,
            accelerator_type: typing.Optional[builtins.str] = None,
            initial_instance_count: typing.Optional[jsii.Number] = None,
            initial_variant_weight: jsii.Number,
            instance_type: typing.Optional[builtins.str] = None,
            model_name: builtins.str,
            serverless_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ServerlessConfigProperty"]] = None,
            variant_name: builtins.str,
        ) -> None:
            '''
            :param accelerator_type: ``CfnEndpointConfig.ProductionVariantProperty.AcceleratorType``.
            :param initial_instance_count: ``CfnEndpointConfig.ProductionVariantProperty.InitialInstanceCount``.
            :param initial_variant_weight: ``CfnEndpointConfig.ProductionVariantProperty.InitialVariantWeight``.
            :param instance_type: ``CfnEndpointConfig.ProductionVariantProperty.InstanceType``.
            :param model_name: ``CfnEndpointConfig.ProductionVariantProperty.ModelName``.
            :param serverless_config: ``CfnEndpointConfig.ProductionVariantProperty.ServerlessConfig``.
            :param variant_name: ``CfnEndpointConfig.ProductionVariantProperty.VariantName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                production_variant_property = sagemaker.CfnEndpointConfig.ProductionVariantProperty(
                    initial_variant_weight=123,
                    model_name="modelName",
                    variant_name="variantName",
                
                    # the properties below are optional
                    accelerator_type="acceleratorType",
                    initial_instance_count=123,
                    instance_type="instanceType",
                    serverless_config=sagemaker.CfnEndpointConfig.ServerlessConfigProperty(
                        max_concurrency=123,
                        memory_size_in_mb=123
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "initial_variant_weight": initial_variant_weight,
                "model_name": model_name,
                "variant_name": variant_name,
            }
            if accelerator_type is not None:
                self._values["accelerator_type"] = accelerator_type
            if initial_instance_count is not None:
                self._values["initial_instance_count"] = initial_instance_count
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if serverless_config is not None:
                self._values["serverless_config"] = serverless_config

        @builtins.property
        def accelerator_type(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpointConfig.ProductionVariantProperty.AcceleratorType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-acceleratortype
            '''
            result = self._values.get("accelerator_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def initial_instance_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnEndpointConfig.ProductionVariantProperty.InitialInstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount
            '''
            result = self._values.get("initial_instance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def initial_variant_weight(self) -> jsii.Number:
            '''``CfnEndpointConfig.ProductionVariantProperty.InitialVariantWeight``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight
            '''
            result = self._values.get("initial_variant_weight")
            assert result is not None, "Required property 'initial_variant_weight' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpointConfig.ProductionVariantProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model_name(self) -> builtins.str:
            '''``CfnEndpointConfig.ProductionVariantProperty.ModelName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-modelname
            '''
            result = self._values.get("model_name")
            assert result is not None, "Required property 'model_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def serverless_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ServerlessConfigProperty"]]:
            '''``CfnEndpointConfig.ProductionVariantProperty.ServerlessConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig
            '''
            result = self._values.get("serverless_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ServerlessConfigProperty"]], result)

        @builtins.property
        def variant_name(self) -> builtins.str:
            '''``CfnEndpointConfig.ProductionVariantProperty.VariantName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-variantname
            '''
            result = self._values.get("variant_name")
            assert result is not None, "Required property 'variant_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProductionVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.ServerlessConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_concurrency": "maxConcurrency",
            "memory_size_in_mb": "memorySizeInMb",
        },
    )
    class ServerlessConfigProperty:
        def __init__(
            self,
            *,
            max_concurrency: jsii.Number,
            memory_size_in_mb: jsii.Number,
        ) -> None:
            '''
            :param max_concurrency: ``CfnEndpointConfig.ServerlessConfigProperty.MaxConcurrency``.
            :param memory_size_in_mb: ``CfnEndpointConfig.ServerlessConfigProperty.MemorySizeInMB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                serverless_config_property = sagemaker.CfnEndpointConfig.ServerlessConfigProperty(
                    max_concurrency=123,
                    memory_size_in_mb=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_concurrency": max_concurrency,
                "memory_size_in_mb": memory_size_in_mb,
            }

        @builtins.property
        def max_concurrency(self) -> jsii.Number:
            '''``CfnEndpointConfig.ServerlessConfigProperty.MaxConcurrency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig-maxconcurrency
            '''
            result = self._values.get("max_concurrency")
            assert result is not None, "Required property 'max_concurrency' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def memory_size_in_mb(self) -> jsii.Number:
            '''``CfnEndpointConfig.ServerlessConfigProperty.MemorySizeInMB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig-memorysizeinmb
            '''
            result = self._values.get("memory_size_in_mb")
            assert result is not None, "Required property 'memory_size_in_mb' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerlessConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "async_inference_config": "asyncInferenceConfig",
        "data_capture_config": "dataCaptureConfig",
        "endpoint_config_name": "endpointConfigName",
        "kms_key_id": "kmsKeyId",
        "production_variants": "productionVariants",
        "tags": "tags",
    },
)
class CfnEndpointConfigProps:
    def __init__(
        self,
        *,
        async_inference_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.AsyncInferenceConfigProperty]] = None,
        data_capture_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.DataCaptureConfigProperty]] = None,
        endpoint_config_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        production_variants: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.ProductionVariantProperty]]],
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::EndpointConfig``.

        :param async_inference_config: ``AWS::SageMaker::EndpointConfig.AsyncInferenceConfig``.
        :param data_capture_config: ``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.
        :param endpoint_config_name: ``AWS::SageMaker::EndpointConfig.EndpointConfigName``.
        :param kms_key_id: ``AWS::SageMaker::EndpointConfig.KmsKeyId``.
        :param production_variants: ``AWS::SageMaker::EndpointConfig.ProductionVariants``.
        :param tags: ``AWS::SageMaker::EndpointConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_endpoint_config_props = sagemaker.CfnEndpointConfigProps(
                production_variants=[sagemaker.CfnEndpointConfig.ProductionVariantProperty(
                    initial_variant_weight=123,
                    model_name="modelName",
                    variant_name="variantName",
            
                    # the properties below are optional
                    accelerator_type="acceleratorType",
                    initial_instance_count=123,
                    instance_type="instanceType",
                    serverless_config=sagemaker.CfnEndpointConfig.ServerlessConfigProperty(
                        max_concurrency=123,
                        memory_size_in_mb=123
                    )
                )],
            
                # the properties below are optional
                async_inference_config=sagemaker.CfnEndpointConfig.AsyncInferenceConfigProperty(
                    output_config=sagemaker.CfnEndpointConfig.AsyncInferenceOutputConfigProperty(
                        s3_output_path="s3OutputPath",
            
                        # the properties below are optional
                        kms_key_id="kmsKeyId",
                        notification_config=sagemaker.CfnEndpointConfig.AsyncInferenceNotificationConfigProperty(
                            error_topic="errorTopic",
                            success_topic="successTopic"
                        )
                    ),
            
                    # the properties below are optional
                    client_config=sagemaker.CfnEndpointConfig.AsyncInferenceClientConfigProperty(
                        max_concurrent_invocations_per_instance=123
                    )
                ),
                data_capture_config=sagemaker.CfnEndpointConfig.DataCaptureConfigProperty(
                    capture_options=[sagemaker.CfnEndpointConfig.CaptureOptionProperty(
                        capture_mode="captureMode"
                    )],
                    destination_s3_uri="destinationS3Uri",
                    initial_sampling_percentage=123,
            
                    # the properties below are optional
                    capture_content_type_header=sagemaker.CfnEndpointConfig.CaptureContentTypeHeaderProperty(
                        csv_content_types=["csvContentTypes"],
                        json_content_types=["jsonContentTypes"]
                    ),
                    enable_capture=False,
                    kms_key_id="kmsKeyId"
                ),
                endpoint_config_name="endpointConfigName",
                kms_key_id="kmsKeyId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "production_variants": production_variants,
        }
        if async_inference_config is not None:
            self._values["async_inference_config"] = async_inference_config
        if data_capture_config is not None:
            self._values["data_capture_config"] = data_capture_config
        if endpoint_config_name is not None:
            self._values["endpoint_config_name"] = endpoint_config_name
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def async_inference_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.AsyncInferenceConfigProperty]]:
        '''``AWS::SageMaker::EndpointConfig.AsyncInferenceConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceconfig
        '''
        result = self._values.get("async_inference_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.AsyncInferenceConfigProperty]], result)

    @builtins.property
    def data_capture_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.DataCaptureConfigProperty]]:
        '''``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig
        '''
        result = self._values.get("data_capture_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.DataCaptureConfigProperty]], result)

    @builtins.property
    def endpoint_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::EndpointConfig.EndpointConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-endpointconfigname
        '''
        result = self._values.get("endpoint_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::EndpointConfig.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def production_variants(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.ProductionVariantProperty]]]:
        '''``AWS::SageMaker::EndpointConfig.ProductionVariants``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-productionvariants
        '''
        result = self._values.get("production_variants")
        assert result is not None, "Required property 'production_variants' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.ProductionVariantProperty]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::EndpointConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_config": "deploymentConfig",
        "endpoint_config_name": "endpointConfigName",
        "endpoint_name": "endpointName",
        "exclude_retained_variant_properties": "excludeRetainedVariantProperties",
        "retain_all_variant_properties": "retainAllVariantProperties",
        "retain_deployment_config": "retainDeploymentConfig",
        "tags": "tags",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        deployment_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.DeploymentConfigProperty]] = None,
        endpoint_config_name: builtins.str,
        endpoint_name: typing.Optional[builtins.str] = None,
        exclude_retained_variant_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.VariantPropertyProperty]]]] = None,
        retain_all_variant_properties: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        retain_deployment_config: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Endpoint``.

        :param deployment_config: ``AWS::SageMaker::Endpoint.DeploymentConfig``.
        :param endpoint_config_name: ``AWS::SageMaker::Endpoint.EndpointConfigName``.
        :param endpoint_name: ``AWS::SageMaker::Endpoint.EndpointName``.
        :param exclude_retained_variant_properties: ``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.
        :param retain_all_variant_properties: ``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.
        :param retain_deployment_config: ``AWS::SageMaker::Endpoint.RetainDeploymentConfig``.
        :param tags: ``AWS::SageMaker::Endpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_endpoint_props = sagemaker.CfnEndpointProps(
                endpoint_config_name="endpointConfigName",
            
                # the properties below are optional
                deployment_config=sagemaker.CfnEndpoint.DeploymentConfigProperty(
                    blue_green_update_policy=sagemaker.CfnEndpoint.BlueGreenUpdatePolicyProperty(
                        traffic_routing_configuration=sagemaker.CfnEndpoint.TrafficRoutingConfigProperty(
                            type="type",
            
                            # the properties below are optional
                            canary_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                                type="type",
                                value=123
                            ),
                            linear_step_size=sagemaker.CfnEndpoint.CapacitySizeProperty(
                                type="type",
                                value=123
                            ),
                            wait_interval_in_seconds=123
                        ),
            
                        # the properties below are optional
                        maximum_execution_timeout_in_seconds=123,
                        termination_wait_in_seconds=123
                    ),
            
                    # the properties below are optional
                    auto_rollback_configuration=sagemaker.CfnEndpoint.AutoRollbackConfigProperty(
                        alarms=[sagemaker.CfnEndpoint.AlarmProperty(
                            alarm_name="alarmName"
                        )]
                    )
                ),
                endpoint_name="endpointName",
                exclude_retained_variant_properties=[sagemaker.CfnEndpoint.VariantPropertyProperty(
                    variant_property_type="variantPropertyType"
                )],
                retain_all_variant_properties=False,
                retain_deployment_config=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_config_name": endpoint_config_name,
        }
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if exclude_retained_variant_properties is not None:
            self._values["exclude_retained_variant_properties"] = exclude_retained_variant_properties
        if retain_all_variant_properties is not None:
            self._values["retain_all_variant_properties"] = retain_all_variant_properties
        if retain_deployment_config is not None:
            self._values["retain_deployment_config"] = retain_deployment_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def deployment_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.DeploymentConfigProperty]]:
        '''``AWS::SageMaker::Endpoint.DeploymentConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-deploymentconfig
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.DeploymentConfigProperty]], result)

    @builtins.property
    def endpoint_config_name(self) -> builtins.str:
        '''``AWS::SageMaker::Endpoint.EndpointConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointconfigname
        '''
        result = self._values.get("endpoint_config_name")
        assert result is not None, "Required property 'endpoint_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Endpoint.EndpointName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointname
        '''
        result = self._values.get("endpoint_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude_retained_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.VariantPropertyProperty]]]]:
        '''``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-excluderetainedvariantproperties
        '''
        result = self._values.get("exclude_retained_variant_properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.VariantPropertyProperty]]]], result)

    @builtins.property
    def retain_all_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retainallvariantproperties
        '''
        result = self._values.get("retain_all_variant_properties")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def retain_deployment_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Endpoint.RetainDeploymentConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retaindeploymentconfig
        '''
        result = self._values.get("retain_deployment_config")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Endpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFeatureGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnFeatureGroup",
):
    '''A CloudFormation ``AWS::SageMaker::FeatureGroup``.

    :cloudformationResource: AWS::SageMaker::FeatureGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        # offline_store_config is of type object
        # online_store_config is of type object
        
        cfn_feature_group = sagemaker.CfnFeatureGroup(self, "MyCfnFeatureGroup",
            event_time_feature_name="eventTimeFeatureName",
            feature_definitions=[sagemaker.CfnFeatureGroup.FeatureDefinitionProperty(
                feature_name="featureName",
                feature_type="featureType"
            )],
            feature_group_name="featureGroupName",
            record_identifier_feature_name="recordIdentifierFeatureName",
        
            # the properties below are optional
            description="description",
            offline_store_config=offline_store_config,
            online_store_config=online_store_config,
            role_arn="roleArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_time_feature_name: builtins.str,
        feature_definitions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFeatureGroup.FeatureDefinitionProperty"]]],
        feature_group_name: builtins.str,
        offline_store_config: typing.Any = None,
        online_store_config: typing.Any = None,
        record_identifier_feature_name: builtins.str,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::FeatureGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::SageMaker::FeatureGroup.Description``.
        :param event_time_feature_name: ``AWS::SageMaker::FeatureGroup.EventTimeFeatureName``.
        :param feature_definitions: ``AWS::SageMaker::FeatureGroup.FeatureDefinitions``.
        :param feature_group_name: ``AWS::SageMaker::FeatureGroup.FeatureGroupName``.
        :param offline_store_config: ``AWS::SageMaker::FeatureGroup.OfflineStoreConfig``.
        :param online_store_config: ``AWS::SageMaker::FeatureGroup.OnlineStoreConfig``.
        :param record_identifier_feature_name: ``AWS::SageMaker::FeatureGroup.RecordIdentifierFeatureName``.
        :param role_arn: ``AWS::SageMaker::FeatureGroup.RoleArn``.
        :param tags: ``AWS::SageMaker::FeatureGroup.Tags``.
        '''
        props = CfnFeatureGroupProps(
            description=description,
            event_time_feature_name=event_time_feature_name,
            feature_definitions=feature_definitions,
            feature_group_name=feature_group_name,
            offline_store_config=offline_store_config,
            online_store_config=online_store_config,
            record_identifier_feature_name=record_identifier_feature_name,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::FeatureGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventTimeFeatureName")
    def event_time_feature_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.EventTimeFeatureName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-eventtimefeaturename
        '''
        return typing.cast(builtins.str, jsii.get(self, "eventTimeFeatureName"))

    @event_time_feature_name.setter
    def event_time_feature_name(self, value: builtins.str) -> None:
        jsii.set(self, "eventTimeFeatureName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="featureDefinitions")
    def feature_definitions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFeatureGroup.FeatureDefinitionProperty"]]]:
        '''``AWS::SageMaker::FeatureGroup.FeatureDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuredefinitions
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFeatureGroup.FeatureDefinitionProperty"]]], jsii.get(self, "featureDefinitions"))

    @feature_definitions.setter
    def feature_definitions(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFeatureGroup.FeatureDefinitionProperty"]]],
    ) -> None:
        jsii.set(self, "featureDefinitions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="featureGroupName")
    def feature_group_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.FeatureGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuregroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "featureGroupName"))

    @feature_group_name.setter
    def feature_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "featureGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="offlineStoreConfig")
    def offline_store_config(self) -> typing.Any:
        '''``AWS::SageMaker::FeatureGroup.OfflineStoreConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-offlinestoreconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "offlineStoreConfig"))

    @offline_store_config.setter
    def offline_store_config(self, value: typing.Any) -> None:
        jsii.set(self, "offlineStoreConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onlineStoreConfig")
    def online_store_config(self) -> typing.Any:
        '''``AWS::SageMaker::FeatureGroup.OnlineStoreConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-onlinestoreconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "onlineStoreConfig"))

    @online_store_config.setter
    def online_store_config(self, value: typing.Any) -> None:
        jsii.set(self, "onlineStoreConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recordIdentifierFeatureName")
    def record_identifier_feature_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.RecordIdentifierFeatureName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-recordidentifierfeaturename
        '''
        return typing.cast(builtins.str, jsii.get(self, "recordIdentifierFeatureName"))

    @record_identifier_feature_name.setter
    def record_identifier_feature_name(self, value: builtins.str) -> None:
        jsii.set(self, "recordIdentifierFeatureName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::FeatureGroup.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::FeatureGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnFeatureGroup.FeatureDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"feature_name": "featureName", "feature_type": "featureType"},
    )
    class FeatureDefinitionProperty:
        def __init__(
            self,
            *,
            feature_name: builtins.str,
            feature_type: builtins.str,
        ) -> None:
            '''
            :param feature_name: ``CfnFeatureGroup.FeatureDefinitionProperty.FeatureName``.
            :param feature_type: ``CfnFeatureGroup.FeatureDefinitionProperty.FeatureType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                feature_definition_property = sagemaker.CfnFeatureGroup.FeatureDefinitionProperty(
                    feature_name="featureName",
                    feature_type="featureType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "feature_name": feature_name,
                "feature_type": feature_type,
            }

        @builtins.property
        def feature_name(self) -> builtins.str:
            '''``CfnFeatureGroup.FeatureDefinitionProperty.FeatureName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html#cfn-sagemaker-featuregroup-featuredefinition-featurename
            '''
            result = self._values.get("feature_name")
            assert result is not None, "Required property 'feature_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def feature_type(self) -> builtins.str:
            '''``CfnFeatureGroup.FeatureDefinitionProperty.FeatureType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html#cfn-sagemaker-featuregroup-featuredefinition-featuretype
            '''
            result = self._values.get("feature_type")
            assert result is not None, "Required property 'feature_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FeatureDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnFeatureGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "event_time_feature_name": "eventTimeFeatureName",
        "feature_definitions": "featureDefinitions",
        "feature_group_name": "featureGroupName",
        "offline_store_config": "offlineStoreConfig",
        "online_store_config": "onlineStoreConfig",
        "record_identifier_feature_name": "recordIdentifierFeatureName",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnFeatureGroupProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        event_time_feature_name: builtins.str,
        feature_definitions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnFeatureGroup.FeatureDefinitionProperty]]],
        feature_group_name: builtins.str,
        offline_store_config: typing.Any = None,
        online_store_config: typing.Any = None,
        record_identifier_feature_name: builtins.str,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::FeatureGroup``.

        :param description: ``AWS::SageMaker::FeatureGroup.Description``.
        :param event_time_feature_name: ``AWS::SageMaker::FeatureGroup.EventTimeFeatureName``.
        :param feature_definitions: ``AWS::SageMaker::FeatureGroup.FeatureDefinitions``.
        :param feature_group_name: ``AWS::SageMaker::FeatureGroup.FeatureGroupName``.
        :param offline_store_config: ``AWS::SageMaker::FeatureGroup.OfflineStoreConfig``.
        :param online_store_config: ``AWS::SageMaker::FeatureGroup.OnlineStoreConfig``.
        :param record_identifier_feature_name: ``AWS::SageMaker::FeatureGroup.RecordIdentifierFeatureName``.
        :param role_arn: ``AWS::SageMaker::FeatureGroup.RoleArn``.
        :param tags: ``AWS::SageMaker::FeatureGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            # offline_store_config is of type object
            # online_store_config is of type object
            
            cfn_feature_group_props = sagemaker.CfnFeatureGroupProps(
                event_time_feature_name="eventTimeFeatureName",
                feature_definitions=[sagemaker.CfnFeatureGroup.FeatureDefinitionProperty(
                    feature_name="featureName",
                    feature_type="featureType"
                )],
                feature_group_name="featureGroupName",
                record_identifier_feature_name="recordIdentifierFeatureName",
            
                # the properties below are optional
                description="description",
                offline_store_config=offline_store_config,
                online_store_config=online_store_config,
                role_arn="roleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "event_time_feature_name": event_time_feature_name,
            "feature_definitions": feature_definitions,
            "feature_group_name": feature_group_name,
            "record_identifier_feature_name": record_identifier_feature_name,
        }
        if description is not None:
            self._values["description"] = description
        if offline_store_config is not None:
            self._values["offline_store_config"] = offline_store_config
        if online_store_config is not None:
            self._values["online_store_config"] = online_store_config
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::FeatureGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_time_feature_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.EventTimeFeatureName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-eventtimefeaturename
        '''
        result = self._values.get("event_time_feature_name")
        assert result is not None, "Required property 'event_time_feature_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def feature_definitions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnFeatureGroup.FeatureDefinitionProperty]]]:
        '''``AWS::SageMaker::FeatureGroup.FeatureDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuredefinitions
        '''
        result = self._values.get("feature_definitions")
        assert result is not None, "Required property 'feature_definitions' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnFeatureGroup.FeatureDefinitionProperty]]], result)

    @builtins.property
    def feature_group_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.FeatureGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuregroupname
        '''
        result = self._values.get("feature_group_name")
        assert result is not None, "Required property 'feature_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def offline_store_config(self) -> typing.Any:
        '''``AWS::SageMaker::FeatureGroup.OfflineStoreConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-offlinestoreconfig
        '''
        result = self._values.get("offline_store_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def online_store_config(self) -> typing.Any:
        '''``AWS::SageMaker::FeatureGroup.OnlineStoreConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-onlinestoreconfig
        '''
        result = self._values.get("online_store_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def record_identifier_feature_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.RecordIdentifierFeatureName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-recordidentifierfeaturename
        '''
        result = self._values.get("record_identifier_feature_name")
        assert result is not None, "Required property 'record_identifier_feature_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::FeatureGroup.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::FeatureGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFeatureGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnImage(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnImage",
):
    '''A CloudFormation ``AWS::SageMaker::Image``.

    :cloudformationResource: AWS::SageMaker::Image
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_image = sagemaker.CfnImage(self, "MyCfnImage",
            image_name="imageName",
            image_role_arn="imageRoleArn",
        
            # the properties below are optional
            image_description="imageDescription",
            image_display_name="imageDisplayName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        image_description: typing.Optional[builtins.str] = None,
        image_display_name: typing.Optional[builtins.str] = None,
        image_name: builtins.str,
        image_role_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Image``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param image_description: ``AWS::SageMaker::Image.ImageDescription``.
        :param image_display_name: ``AWS::SageMaker::Image.ImageDisplayName``.
        :param image_name: ``AWS::SageMaker::Image.ImageName``.
        :param image_role_arn: ``AWS::SageMaker::Image.ImageRoleArn``.
        :param tags: ``AWS::SageMaker::Image.Tags``.
        '''
        props = CfnImageProps(
            image_description=image_description,
            image_display_name=image_display_name,
            image_name=image_name,
            image_role_arn=image_role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrImageArn")
    def attr_image_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ImageArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageDescription")
    def image_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Image.ImageDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageDescription"))

    @image_description.setter
    def image_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "imageDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageDisplayName")
    def image_display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Image.ImageDisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedisplayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageDisplayName"))

    @image_display_name.setter
    def image_display_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "imageDisplayName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        '''``AWS::SageMaker::Image.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagename
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        jsii.set(self, "imageName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageRoleArn")
    def image_role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Image.ImageRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagerolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageRoleArn"))

    @image_role_arn.setter
    def image_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "imageRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnImageProps",
    jsii_struct_bases=[],
    name_mapping={
        "image_description": "imageDescription",
        "image_display_name": "imageDisplayName",
        "image_name": "imageName",
        "image_role_arn": "imageRoleArn",
        "tags": "tags",
    },
)
class CfnImageProps:
    def __init__(
        self,
        *,
        image_description: typing.Optional[builtins.str] = None,
        image_display_name: typing.Optional[builtins.str] = None,
        image_name: builtins.str,
        image_role_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Image``.

        :param image_description: ``AWS::SageMaker::Image.ImageDescription``.
        :param image_display_name: ``AWS::SageMaker::Image.ImageDisplayName``.
        :param image_name: ``AWS::SageMaker::Image.ImageName``.
        :param image_role_arn: ``AWS::SageMaker::Image.ImageRoleArn``.
        :param tags: ``AWS::SageMaker::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_image_props = sagemaker.CfnImageProps(
                image_name="imageName",
                image_role_arn="imageRoleArn",
            
                # the properties below are optional
                image_description="imageDescription",
                image_display_name="imageDisplayName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "image_name": image_name,
            "image_role_arn": image_role_arn,
        }
        if image_description is not None:
            self._values["image_description"] = image_description
        if image_display_name is not None:
            self._values["image_display_name"] = image_display_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def image_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Image.ImageDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedescription
        '''
        result = self._values.get("image_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Image.ImageDisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedisplayname
        '''
        result = self._values.get("image_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''``AWS::SageMaker::Image.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagename
        '''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Image.ImageRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagerolearn
        '''
        result = self._values.get("image_role_arn")
        assert result is not None, "Required property 'image_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnImageVersion(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnImageVersion",
):
    '''A CloudFormation ``AWS::SageMaker::ImageVersion``.

    :cloudformationResource: AWS::SageMaker::ImageVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_image_version = sagemaker.CfnImageVersion(self, "MyCfnImageVersion",
            base_image="baseImage",
            image_name="imageName"
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        base_image: builtins.str,
        image_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ImageVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param base_image: ``AWS::SageMaker::ImageVersion.BaseImage``.
        :param image_name: ``AWS::SageMaker::ImageVersion.ImageName``.
        '''
        props = CfnImageVersionProps(base_image=base_image, image_name=image_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrContainerImage")
    def attr_container_image(self) -> builtins.str:
        '''
        :cloudformationAttribute: ContainerImage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContainerImage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrImageArn")
    def attr_image_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ImageArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrImageVersionArn")
    def attr_image_version_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ImageVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageVersionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> jsii.Number:
        '''
        :cloudformationAttribute: Version
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="baseImage")
    def base_image(self) -> builtins.str:
        '''``AWS::SageMaker::ImageVersion.BaseImage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-baseimage
        '''
        return typing.cast(builtins.str, jsii.get(self, "baseImage"))

    @base_image.setter
    def base_image(self, value: builtins.str) -> None:
        jsii.set(self, "baseImage", value)

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        '''``AWS::SageMaker::ImageVersion.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-imagename
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        jsii.set(self, "imageName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnImageVersionProps",
    jsii_struct_bases=[],
    name_mapping={"base_image": "baseImage", "image_name": "imageName"},
)
class CfnImageVersionProps:
    def __init__(self, *, base_image: builtins.str, image_name: builtins.str) -> None:
        '''Properties for defining a ``AWS::SageMaker::ImageVersion``.

        :param base_image: ``AWS::SageMaker::ImageVersion.BaseImage``.
        :param image_name: ``AWS::SageMaker::ImageVersion.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_image_version_props = sagemaker.CfnImageVersionProps(
                base_image="baseImage",
                image_name="imageName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "base_image": base_image,
            "image_name": image_name,
        }

    @builtins.property
    def base_image(self) -> builtins.str:
        '''``AWS::SageMaker::ImageVersion.BaseImage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-baseimage
        '''
        result = self._values.get("base_image")
        assert result is not None, "Required property 'base_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''``AWS::SageMaker::ImageVersion.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-imagename
        '''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModel",
):
    '''A CloudFormation ``AWS::SageMaker::Model``.

    :cloudformationResource: AWS::SageMaker::Model
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        # environment is of type object
        
        cfn_model = sagemaker.CfnModel(self, "MyCfnModel",
            execution_role_arn="executionRoleArn",
        
            # the properties below are optional
            containers=[sagemaker.CfnModel.ContainerDefinitionProperty(
                container_hostname="containerHostname",
                environment=environment,
                image="image",
                image_config=sagemaker.CfnModel.ImageConfigProperty(
                    repository_access_mode="repositoryAccessMode",
        
                    # the properties below are optional
                    repository_auth_config=sagemaker.CfnModel.RepositoryAuthConfigProperty(
                        repository_credentials_provider_arn="repositoryCredentialsProviderArn"
                    )
                ),
                inference_specification_name="inferenceSpecificationName",
                mode="mode",
                model_data_url="modelDataUrl",
                model_package_name="modelPackageName",
                multi_model_config=sagemaker.CfnModel.MultiModelConfigProperty(
                    model_cache_setting="modelCacheSetting"
                )
            )],
            enable_network_isolation=False,
            inference_execution_config=sagemaker.CfnModel.InferenceExecutionConfigProperty(
                mode="mode"
            ),
            model_name="modelName",
            primary_container=sagemaker.CfnModel.ContainerDefinitionProperty(
                container_hostname="containerHostname",
                environment=environment,
                image="image",
                image_config=sagemaker.CfnModel.ImageConfigProperty(
                    repository_access_mode="repositoryAccessMode",
        
                    # the properties below are optional
                    repository_auth_config=sagemaker.CfnModel.RepositoryAuthConfigProperty(
                        repository_credentials_provider_arn="repositoryCredentialsProviderArn"
                    )
                ),
                inference_specification_name="inferenceSpecificationName",
                mode="mode",
                model_data_url="modelDataUrl",
                model_package_name="modelPackageName",
                multi_model_config=sagemaker.CfnModel.MultiModelConfigProperty(
                    model_cache_setting="modelCacheSetting"
                )
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_config=sagemaker.CfnModel.VpcConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnets=["subnets"]
            )
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        containers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]] = None,
        enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        execution_role_arn: builtins.str,
        inference_execution_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.InferenceExecutionConfigProperty"]] = None,
        model_name: typing.Optional[builtins.str] = None,
        primary_container: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Model``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param containers: ``AWS::SageMaker::Model.Containers``.
        :param enable_network_isolation: ``AWS::SageMaker::Model.EnableNetworkIsolation``.
        :param execution_role_arn: ``AWS::SageMaker::Model.ExecutionRoleArn``.
        :param inference_execution_config: ``AWS::SageMaker::Model.InferenceExecutionConfig``.
        :param model_name: ``AWS::SageMaker::Model.ModelName``.
        :param primary_container: ``AWS::SageMaker::Model.PrimaryContainer``.
        :param tags: ``AWS::SageMaker::Model.Tags``.
        :param vpc_config: ``AWS::SageMaker::Model.VpcConfig``.
        '''
        props = CfnModelProps(
            containers=containers,
            enable_network_isolation=enable_network_isolation,
            execution_role_arn=execution_role_arn,
            inference_execution_config=inference_execution_config,
            model_name=model_name,
            primary_container=primary_container,
            tags=tags,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModelName")
    def attr_model_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModelName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModelName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]]:
        '''``AWS::SageMaker::Model.Containers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-containers
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]], jsii.get(self, "containers"))

    @containers.setter
    def containers(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]],
    ) -> None:
        jsii.set(self, "containers", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableNetworkIsolation")
    def enable_network_isolation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Model.EnableNetworkIsolation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-enablenetworkisolation
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enableNetworkIsolation"))

    @enable_network_isolation.setter
    def enable_network_isolation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enableNetworkIsolation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Model.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-executionrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inferenceExecutionConfig")
    def inference_execution_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.InferenceExecutionConfigProperty"]]:
        '''``AWS::SageMaker::Model.InferenceExecutionConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-inferenceexecutionconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.InferenceExecutionConfigProperty"]], jsii.get(self, "inferenceExecutionConfig"))

    @inference_execution_config.setter
    def inference_execution_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.InferenceExecutionConfigProperty"]],
    ) -> None:
        jsii.set(self, "inferenceExecutionConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Model.ModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-modelname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "modelName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="primaryContainer")
    def primary_container(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]:
        '''``AWS::SageMaker::Model.PrimaryContainer``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-primarycontainer
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]], jsii.get(self, "primaryContainer"))

    @primary_container.setter
    def primary_container(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]],
    ) -> None:
        jsii.set(self, "primaryContainer", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Model.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]]:
        '''``AWS::SageMaker::Model.VpcConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-vpcconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]],
    ) -> None:
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.ContainerDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_hostname": "containerHostname",
            "environment": "environment",
            "image": "image",
            "image_config": "imageConfig",
            "inference_specification_name": "inferenceSpecificationName",
            "mode": "mode",
            "model_data_url": "modelDataUrl",
            "model_package_name": "modelPackageName",
            "multi_model_config": "multiModelConfig",
        },
    )
    class ContainerDefinitionProperty:
        def __init__(
            self,
            *,
            container_hostname: typing.Optional[builtins.str] = None,
            environment: typing.Any = None,
            image: typing.Optional[builtins.str] = None,
            image_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ImageConfigProperty"]] = None,
            inference_specification_name: typing.Optional[builtins.str] = None,
            mode: typing.Optional[builtins.str] = None,
            model_data_url: typing.Optional[builtins.str] = None,
            model_package_name: typing.Optional[builtins.str] = None,
            multi_model_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.MultiModelConfigProperty"]] = None,
        ) -> None:
            '''
            :param container_hostname: ``CfnModel.ContainerDefinitionProperty.ContainerHostname``.
            :param environment: ``CfnModel.ContainerDefinitionProperty.Environment``.
            :param image: ``CfnModel.ContainerDefinitionProperty.Image``.
            :param image_config: ``CfnModel.ContainerDefinitionProperty.ImageConfig``.
            :param inference_specification_name: ``CfnModel.ContainerDefinitionProperty.InferenceSpecificationName``.
            :param mode: ``CfnModel.ContainerDefinitionProperty.Mode``.
            :param model_data_url: ``CfnModel.ContainerDefinitionProperty.ModelDataUrl``.
            :param model_package_name: ``CfnModel.ContainerDefinitionProperty.ModelPackageName``.
            :param multi_model_config: ``CfnModel.ContainerDefinitionProperty.MultiModelConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                # environment is of type object
                
                container_definition_property = sagemaker.CfnModel.ContainerDefinitionProperty(
                    container_hostname="containerHostname",
                    environment=environment,
                    image="image",
                    image_config=sagemaker.CfnModel.ImageConfigProperty(
                        repository_access_mode="repositoryAccessMode",
                
                        # the properties below are optional
                        repository_auth_config=sagemaker.CfnModel.RepositoryAuthConfigProperty(
                            repository_credentials_provider_arn="repositoryCredentialsProviderArn"
                        )
                    ),
                    inference_specification_name="inferenceSpecificationName",
                    mode="mode",
                    model_data_url="modelDataUrl",
                    model_package_name="modelPackageName",
                    multi_model_config=sagemaker.CfnModel.MultiModelConfigProperty(
                        model_cache_setting="modelCacheSetting"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if container_hostname is not None:
                self._values["container_hostname"] = container_hostname
            if environment is not None:
                self._values["environment"] = environment
            if image is not None:
                self._values["image"] = image
            if image_config is not None:
                self._values["image_config"] = image_config
            if inference_specification_name is not None:
                self._values["inference_specification_name"] = inference_specification_name
            if mode is not None:
                self._values["mode"] = mode
            if model_data_url is not None:
                self._values["model_data_url"] = model_data_url
            if model_package_name is not None:
                self._values["model_package_name"] = model_package_name
            if multi_model_config is not None:
                self._values["multi_model_config"] = multi_model_config

        @builtins.property
        def container_hostname(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.ContainerHostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-containerhostname
            '''
            result = self._values.get("container_hostname")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def environment(self) -> typing.Any:
            '''``CfnModel.ContainerDefinitionProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Any, result)

        @builtins.property
        def image(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.Image``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-image
            '''
            result = self._values.get("image")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ImageConfigProperty"]]:
            '''``CfnModel.ContainerDefinitionProperty.ImageConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-imageconfig
            '''
            result = self._values.get("image_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ImageConfigProperty"]], result)

        @builtins.property
        def inference_specification_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.InferenceSpecificationName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-inferencespecificationname
            '''
            result = self._values.get("inference_specification_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model_data_url(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.ModelDataUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modeldataurl
            '''
            result = self._values.get("model_data_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model_package_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.ModelPackageName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modelpackagename
            '''
            result = self._values.get("model_package_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def multi_model_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.MultiModelConfigProperty"]]:
            '''``CfnModel.ContainerDefinitionProperty.MultiModelConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-multimodelconfig
            '''
            result = self._values.get("multi_model_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.MultiModelConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.ImageConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "repository_access_mode": "repositoryAccessMode",
            "repository_auth_config": "repositoryAuthConfig",
        },
    )
    class ImageConfigProperty:
        def __init__(
            self,
            *,
            repository_access_mode: builtins.str,
            repository_auth_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.RepositoryAuthConfigProperty"]] = None,
        ) -> None:
            '''
            :param repository_access_mode: ``CfnModel.ImageConfigProperty.RepositoryAccessMode``.
            :param repository_auth_config: ``CfnModel.ImageConfigProperty.RepositoryAuthConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                image_config_property = sagemaker.CfnModel.ImageConfigProperty(
                    repository_access_mode="repositoryAccessMode",
                
                    # the properties below are optional
                    repository_auth_config=sagemaker.CfnModel.RepositoryAuthConfigProperty(
                        repository_credentials_provider_arn="repositoryCredentialsProviderArn"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "repository_access_mode": repository_access_mode,
            }
            if repository_auth_config is not None:
                self._values["repository_auth_config"] = repository_auth_config

        @builtins.property
        def repository_access_mode(self) -> builtins.str:
            '''``CfnModel.ImageConfigProperty.RepositoryAccessMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html#cfn-sagemaker-model-containerdefinition-imageconfig-repositoryaccessmode
            '''
            result = self._values.get("repository_access_mode")
            assert result is not None, "Required property 'repository_access_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def repository_auth_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.RepositoryAuthConfigProperty"]]:
            '''``CfnModel.ImageConfigProperty.RepositoryAuthConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html#cfn-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig
            '''
            result = self._values.get("repository_auth_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.RepositoryAuthConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.InferenceExecutionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode"},
    )
    class InferenceExecutionConfigProperty:
        def __init__(self, *, mode: builtins.str) -> None:
            '''
            :param mode: ``CfnModel.InferenceExecutionConfigProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                inference_execution_config_property = sagemaker.CfnModel.InferenceExecutionConfigProperty(
                    mode="mode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "mode": mode,
            }

        @builtins.property
        def mode(self) -> builtins.str:
            '''``CfnModel.InferenceExecutionConfigProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html#cfn-sagemaker-model-inferenceexecutionconfig-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InferenceExecutionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.MultiModelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"model_cache_setting": "modelCacheSetting"},
    )
    class MultiModelConfigProperty:
        def __init__(
            self,
            *,
            model_cache_setting: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param model_cache_setting: ``CfnModel.MultiModelConfigProperty.ModelCacheSetting``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                multi_model_config_property = sagemaker.CfnModel.MultiModelConfigProperty(
                    model_cache_setting="modelCacheSetting"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if model_cache_setting is not None:
                self._values["model_cache_setting"] = model_cache_setting

        @builtins.property
        def model_cache_setting(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.MultiModelConfigProperty.ModelCacheSetting``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html#cfn-sagemaker-model-containerdefinition-multimodelconfig-modelcachesetting
            '''
            result = self._values.get("model_cache_setting")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiModelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.RepositoryAuthConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "repository_credentials_provider_arn": "repositoryCredentialsProviderArn",
        },
    )
    class RepositoryAuthConfigProperty:
        def __init__(
            self,
            *,
            repository_credentials_provider_arn: builtins.str,
        ) -> None:
            '''
            :param repository_credentials_provider_arn: ``CfnModel.RepositoryAuthConfigProperty.RepositoryCredentialsProviderArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                repository_auth_config_property = sagemaker.CfnModel.RepositoryAuthConfigProperty(
                    repository_credentials_provider_arn="repositoryCredentialsProviderArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "repository_credentials_provider_arn": repository_credentials_provider_arn,
            }

        @builtins.property
        def repository_credentials_provider_arn(self) -> builtins.str:
            '''``CfnModel.RepositoryAuthConfigProperty.RepositoryCredentialsProviderArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig.html#cfn-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig-repositorycredentialsproviderarn
            '''
            result = self._values.get("repository_credentials_provider_arn")
            assert result is not None, "Required property 'repository_credentials_provider_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepositoryAuthConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnModel.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModel.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                vpc_config_property = sagemaker.CfnModel.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnModel.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html#cfn-sagemaker-model-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnModel.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html#cfn-sagemaker-model-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelBiasJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition",
):
    '''A CloudFormation ``AWS::SageMaker::ModelBiasJobDefinition``.

    :cloudformationResource: AWS::SageMaker::ModelBiasJobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_model_bias_job_definition = sagemaker.CfnModelBiasJobDefinition(self, "MyCfnModelBiasJobDefinition",
            job_resources=sagemaker.CfnModelBiasJobDefinition.MonitoringResourcesProperty(
                cluster_config=sagemaker.CfnModelBiasJobDefinition.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
        
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            ),
            model_bias_app_specification=sagemaker.CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty(
                config_uri="configUri",
                image_uri="imageUri",
        
                # the properties below are optional
                environment={
                    "environment_key": "environment"
                }
            ),
            model_bias_job_input=sagemaker.CfnModelBiasJobDefinition.ModelBiasJobInputProperty(
                endpoint_input=sagemaker.CfnModelBiasJobDefinition.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
        
                    # the properties below are optional
                    end_time_offset="endTimeOffset",
                    features_attribute="featuresAttribute",
                    inference_attribute="inferenceAttribute",
                    probability_attribute="probabilityAttribute",
                    probability_threshold_attribute=123,
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode",
                    start_time_offset="startTimeOffset"
                ),
                ground_truth_s3_input=sagemaker.CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty(
                    s3_uri="s3Uri"
                )
            ),
            model_bias_job_output_config=sagemaker.CfnModelBiasJobDefinition.MonitoringOutputConfigProperty(
                monitoring_outputs=[sagemaker.CfnModelBiasJobDefinition.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnModelBiasJobDefinition.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
        
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )],
        
                # the properties below are optional
                kms_key_id="kmsKeyId"
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            job_definition_name="jobDefinitionName",
            model_bias_baseline_config=sagemaker.CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty(
                baselining_job_name="baseliningJobName",
                constraints_resource=sagemaker.CfnModelBiasJobDefinition.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                )
            ),
            network_config=sagemaker.CfnModelBiasJobDefinition.NetworkConfigProperty(
                enable_inter_container_traffic_encryption=False,
                enable_network_isolation=False,
                vpc_config=sagemaker.CfnModelBiasJobDefinition.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            ),
            stopping_condition=sagemaker.CfnModelBiasJobDefinition.StoppingConditionProperty(
                max_runtime_in_seconds=123
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_definition_name: typing.Optional[builtins.str] = None,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"],
        model_bias_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"],
        model_bias_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]] = None,
        model_bias_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"],
        model_bias_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"],
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]] = None,
        role_arn: builtins.str,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ModelBiasJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_definition_name: ``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.
        :param job_resources: ``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.
        :param model_bias_app_specification: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.
        :param model_bias_baseline_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.
        :param model_bias_job_input: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.
        :param model_bias_job_output_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.
        :param network_config: ``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.
        :param role_arn: ``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.
        :param stopping_condition: ``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelBiasJobDefinition.Tags``.
        '''
        props = CfnModelBiasJobDefinitionProps(
            job_definition_name=job_definition_name,
            job_resources=job_resources,
            model_bias_app_specification=model_bias_app_specification,
            model_bias_baseline_config=model_bias_baseline_config,
            model_bias_job_input=model_bias_job_input,
            model_bias_job_output_config=model_bias_job_output_config,
            network_config=network_config,
            role_arn=role_arn,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: JobDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobDefinitionArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"], jsii.get(self, "jobResources"))

    @job_resources.setter
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelBiasAppSpecification")
    def model_bias_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"], jsii.get(self, "modelBiasAppSpecification"))

    @model_bias_app_specification.setter
    def model_bias_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelBiasAppSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelBiasBaselineConfig")
    def model_bias_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]], jsii.get(self, "modelBiasBaselineConfig"))

    @model_bias_baseline_config.setter
    def model_bias_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelBiasBaselineConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelBiasJobInput")
    def model_bias_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"], jsii.get(self, "modelBiasJobInput"))

    @model_bias_job_input.setter
    def model_bias_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelBiasJobInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelBiasJobOutputConfig")
    def model_bias_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"], jsii.get(self, "modelBiasJobOutputConfig"))

    @model_bias_job_output_config.setter
    def model_bias_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelBiasJobOutputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]], jsii.get(self, "networkConfig"))

    @network_config.setter
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]], jsii.get(self, "stoppingCondition"))

    @stopping_condition.setter
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_kms_key_id": "volumeKmsKeyId",
            "volume_size_in_gb": "volumeSizeInGb",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
            volume_size_in_gb: jsii.Number,
        ) -> None:
            '''
            :param instance_count: ``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_kms_key_id: ``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.
            :param volume_size_in_gb: ``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                cluster_config_property = sagemaker.CfnModelBiasJobDefinition.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
                
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnModelBiasJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                constraints_resource_property = sagemaker.CfnModelBiasJobDefinition.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html#cfn-sagemaker-modelbiasjobdefinition-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "end_time_offset": "endTimeOffset",
            "features_attribute": "featuresAttribute",
            "inference_attribute": "inferenceAttribute",
            "local_path": "localPath",
            "probability_attribute": "probabilityAttribute",
            "probability_threshold_attribute": "probabilityThresholdAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
            "start_time_offset": "startTimeOffset",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            end_time_offset: typing.Optional[builtins.str] = None,
            features_attribute: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            local_path: builtins.str,
            probability_attribute: typing.Optional[builtins.str] = None,
            probability_threshold_attribute: typing.Optional[jsii.Number] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
            start_time_offset: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnModelBiasJobDefinition.EndpointInputProperty.EndpointName``.
            :param end_time_offset: ``CfnModelBiasJobDefinition.EndpointInputProperty.EndTimeOffset``.
            :param features_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.FeaturesAttribute``.
            :param inference_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param local_path: ``CfnModelBiasJobDefinition.EndpointInputProperty.LocalPath``.
            :param probability_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param probability_threshold_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.
            :param s3_data_distribution_type: ``CfnModelBiasJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelBiasJobDefinition.EndpointInputProperty.S3InputMode``.
            :param start_time_offset: ``CfnModelBiasJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                endpoint_input_property = sagemaker.CfnModelBiasJobDefinition.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
                
                    # the properties below are optional
                    end_time_offset="endTimeOffset",
                    features_attribute="featuresAttribute",
                    inference_attribute="inferenceAttribute",
                    probability_attribute="probabilityAttribute",
                    probability_threshold_attribute=123,
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode",
                    start_time_offset="startTimeOffset"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if end_time_offset is not None:
                self._values["end_time_offset"] = end_time_offset
            if features_attribute is not None:
                self._values["features_attribute"] = features_attribute
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if probability_threshold_attribute is not None:
                self._values["probability_threshold_attribute"] = probability_threshold_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode
            if start_time_offset is not None:
                self._values["start_time_offset"] = start_time_offset

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.EndTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-endtimeoffset
            '''
            result = self._values.get("end_time_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def features_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.FeaturesAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-featuresattribute
            '''
            result = self._values.get("features_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-inferenceattribute
            '''
            result = self._values.get("inference_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-probabilityattribute
            '''
            result = self._values.get("probability_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def probability_threshold_attribute(self) -> typing.Optional[jsii.Number]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-probabilitythresholdattribute
            '''
            result = self._values.get("probability_threshold_attribute")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_time_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-starttimeoffset
            '''
            result = self._values.get("start_time_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "config_uri": "configUri",
            "environment": "environment",
            "image_uri": "imageUri",
        },
    )
    class ModelBiasAppSpecificationProperty:
        def __init__(
            self,
            *,
            config_uri: builtins.str,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            image_uri: builtins.str,
        ) -> None:
            '''
            :param config_uri: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ConfigUri``.
            :param environment: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.Environment``.
            :param image_uri: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_bias_app_specification_property = sagemaker.CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty(
                    config_uri="configUri",
                    image_uri="imageUri",
                
                    # the properties below are optional
                    environment={
                        "environment_key": "environment"
                    }
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "config_uri": config_uri,
                "image_uri": image_uri,
            }
            if environment is not None:
                self._values["environment"] = environment

        @builtins.property
        def config_uri(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ConfigUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-configuri
            '''
            result = self._values.get("config_uri")
            assert result is not None, "Required property 'config_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelBiasBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            '''
            :param baselining_job_name: ``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_bias_baseline_config_property = sagemaker.CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty(
                    baselining_job_name="baseliningJobName",
                    constraints_resource=sagemaker.CfnModelBiasJobDefinition.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.BaseliningJobName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig-baseliningjobname
            '''
            result = self._values.get("baselining_job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ConstraintsResourceProperty"]]:
            '''``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ConstraintsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_input": "endpointInput",
            "ground_truth_s3_input": "groundTruthS3Input",
        },
    )
    class ModelBiasJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EndpointInputProperty"],
            ground_truth_s3_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.EndpointInput``.
            :param ground_truth_s3_input: ``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.GroundTruthS3Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_bias_job_input_property = sagemaker.CfnModelBiasJobDefinition.ModelBiasJobInputProperty(
                    endpoint_input=sagemaker.CfnModelBiasJobDefinition.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
                
                        # the properties below are optional
                        end_time_offset="endTimeOffset",
                        features_attribute="featuresAttribute",
                        inference_attribute="inferenceAttribute",
                        probability_attribute="probabilityAttribute",
                        probability_threshold_attribute=123,
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode",
                        start_time_offset="startTimeOffset"
                    ),
                    ground_truth_s3_input=sagemaker.CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty(
                        s3_uri="s3Uri"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
                "ground_truth_s3_input": ground_truth_s3_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EndpointInputProperty"]:
            '''``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EndpointInputProperty"], result)

        @builtins.property
        def ground_truth_s3_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty"]:
            '''``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.GroundTruthS3Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-groundtruths3input
            '''
            result = self._values.get("ground_truth_s3_input")
            assert result is not None, "Required property 'ground_truth_s3_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class MonitoringGroundTruthS3InputProperty:
        def __init__(self, *, s3_uri: builtins.str) -> None:
            '''
            :param s3_uri: ``CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_ground_truth_s3_input_property = sagemaker.CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_uri": s3_uri,
            }

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html#cfn-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringGroundTruthS3InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_id": "kmsKeyId",
            "monitoring_outputs": "monitoringOutputs",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputProperty"]]],
        ) -> None:
            '''
            :param kms_key_id: ``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.
            :param monitoring_outputs: ``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_config_property = sagemaker.CfnModelBiasJobDefinition.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnModelBiasJobDefinition.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnModelBiasJobDefinition.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
                
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputProperty"]]]:
            '''``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnModelBiasJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_property = sagemaker.CfnModelBiasJobDefinition.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnModelBiasJobDefinition.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.S3OutputProperty"]:
            '''``CfnModelBiasJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnModelBiasJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_resources_property = sagemaker.CfnModelBiasJobDefinition.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnModelBiasJobDefinition.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
                
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ClusterConfigProperty"]:
            '''``CfnModelBiasJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html#cfn-sagemaker-modelbiasjobdefinition-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelBiasJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                network_config_property = sagemaker.CfnModelBiasJobDefinition.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnModelBiasJobDefinition.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.VpcConfigProperty"]]:
            '''``CfnModelBiasJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_upload_mode": "s3UploadMode",
            "s3_uri": "s3Uri",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
            s3_uri: builtins.str,
        ) -> None:
            '''
            :param local_path: ``CfnModelBiasJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_upload_mode: ``CfnModelBiasJobDefinition.S3OutputProperty.S3UploadMode``.
            :param s3_uri: ``CfnModelBiasJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                s3_output_property = sagemaker.CfnModelBiasJobDefinition.S3OutputProperty(
                    local_path="localPath",
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    s3_upload_mode="s3UploadMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnModelBiasJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                stopping_condition_property = sagemaker.CfnModelBiasJobDefinition.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnModelBiasJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnModelBiasJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelBiasJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                vpc_config_property = sagemaker.CfnModelBiasJobDefinition.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnModelBiasJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnModelBiasJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_definition_name": "jobDefinitionName",
        "job_resources": "jobResources",
        "model_bias_app_specification": "modelBiasAppSpecification",
        "model_bias_baseline_config": "modelBiasBaselineConfig",
        "model_bias_job_input": "modelBiasJobInput",
        "model_bias_job_output_config": "modelBiasJobOutputConfig",
        "network_config": "networkConfig",
        "role_arn": "roleArn",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelBiasJobDefinitionProps:
    def __init__(
        self,
        *,
        job_definition_name: typing.Optional[builtins.str] = None,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringResourcesProperty],
        model_bias_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty],
        model_bias_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty]] = None,
        model_bias_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasJobInputProperty],
        model_bias_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringOutputConfigProperty],
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.NetworkConfigProperty]] = None,
        role_arn: builtins.str,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::ModelBiasJobDefinition``.

        :param job_definition_name: ``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.
        :param job_resources: ``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.
        :param model_bias_app_specification: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.
        :param model_bias_baseline_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.
        :param model_bias_job_input: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.
        :param model_bias_job_output_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.
        :param network_config: ``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.
        :param role_arn: ``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.
        :param stopping_condition: ``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_model_bias_job_definition_props = sagemaker.CfnModelBiasJobDefinitionProps(
                job_resources=sagemaker.CfnModelBiasJobDefinition.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnModelBiasJobDefinition.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
            
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                ),
                model_bias_app_specification=sagemaker.CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty(
                    config_uri="configUri",
                    image_uri="imageUri",
            
                    # the properties below are optional
                    environment={
                        "environment_key": "environment"
                    }
                ),
                model_bias_job_input=sagemaker.CfnModelBiasJobDefinition.ModelBiasJobInputProperty(
                    endpoint_input=sagemaker.CfnModelBiasJobDefinition.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
            
                        # the properties below are optional
                        end_time_offset="endTimeOffset",
                        features_attribute="featuresAttribute",
                        inference_attribute="inferenceAttribute",
                        probability_attribute="probabilityAttribute",
                        probability_threshold_attribute=123,
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode",
                        start_time_offset="startTimeOffset"
                    ),
                    ground_truth_s3_input=sagemaker.CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty(
                        s3_uri="s3Uri"
                    )
                ),
                model_bias_job_output_config=sagemaker.CfnModelBiasJobDefinition.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnModelBiasJobDefinition.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnModelBiasJobDefinition.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
            
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
            
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                job_definition_name="jobDefinitionName",
                model_bias_baseline_config=sagemaker.CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty(
                    baselining_job_name="baseliningJobName",
                    constraints_resource=sagemaker.CfnModelBiasJobDefinition.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    )
                ),
                network_config=sagemaker.CfnModelBiasJobDefinition.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnModelBiasJobDefinition.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                ),
                stopping_condition=sagemaker.CfnModelBiasJobDefinition.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_bias_app_specification": model_bias_app_specification,
            "model_bias_job_input": model_bias_job_input,
            "model_bias_job_output_config": model_bias_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_bias_baseline_config is not None:
            self._values["model_bias_baseline_config"] = model_bias_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringResourcesProperty]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources
        '''
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringResourcesProperty], result)

    @builtins.property
    def model_bias_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification
        '''
        result = self._values.get("model_bias_app_specification")
        assert result is not None, "Required property 'model_bias_app_specification' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty], result)

    @builtins.property
    def model_bias_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig
        '''
        result = self._values.get("model_bias_baseline_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty]], result)

    @builtins.property
    def model_bias_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasJobInputProperty]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput
        '''
        result = self._values.get("model_bias_job_input")
        assert result is not None, "Required property 'model_bias_job_input' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasJobInputProperty], result)

    @builtins.property
    def model_bias_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringOutputConfigProperty]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig
        '''
        result = self._values.get("model_bias_job_output_config")
        assert result is not None, "Required property 'model_bias_job_output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringOutputConfigProperty], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.NetworkConfigProperty]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.NetworkConfigProperty]], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.StoppingConditionProperty]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition
        '''
        result = self._values.get("stopping_condition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.StoppingConditionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelBiasJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelExplainabilityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition",
):
    '''A CloudFormation ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

    :cloudformationResource: AWS::SageMaker::ModelExplainabilityJobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_model_explainability_job_definition = sagemaker.CfnModelExplainabilityJobDefinition(self, "MyCfnModelExplainabilityJobDefinition",
            job_resources=sagemaker.CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty(
                cluster_config=sagemaker.CfnModelExplainabilityJobDefinition.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
        
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            ),
            model_explainability_app_specification=sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty(
                config_uri="configUri",
                image_uri="imageUri",
        
                # the properties below are optional
                environment={
                    "environment_key": "environment"
                }
            ),
            model_explainability_job_input=sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty(
                endpoint_input=sagemaker.CfnModelExplainabilityJobDefinition.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
        
                    # the properties below are optional
                    features_attribute="featuresAttribute",
                    inference_attribute="inferenceAttribute",
                    probability_attribute="probabilityAttribute",
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode"
                )
            ),
            model_explainability_job_output_config=sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty(
                monitoring_outputs=[sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnModelExplainabilityJobDefinition.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
        
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )],
        
                # the properties below are optional
                kms_key_id="kmsKeyId"
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            job_definition_name="jobDefinitionName",
            model_explainability_baseline_config=sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty(
                baselining_job_name="baseliningJobName",
                constraints_resource=sagemaker.CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                )
            ),
            network_config=sagemaker.CfnModelExplainabilityJobDefinition.NetworkConfigProperty(
                enable_inter_container_traffic_encryption=False,
                enable_network_isolation=False,
                vpc_config=sagemaker.CfnModelExplainabilityJobDefinition.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            ),
            stopping_condition=sagemaker.CfnModelExplainabilityJobDefinition.StoppingConditionProperty(
                max_runtime_in_seconds=123
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_definition_name: typing.Optional[builtins.str] = None,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"],
        model_explainability_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"],
        model_explainability_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]] = None,
        model_explainability_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"],
        model_explainability_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"],
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]] = None,
        role_arn: builtins.str,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_definition_name: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.
        :param job_resources: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.
        :param model_explainability_app_specification: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.
        :param model_explainability_baseline_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.
        :param model_explainability_job_input: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.
        :param model_explainability_job_output_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.
        :param network_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.
        :param role_arn: ``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.
        :param stopping_condition: ``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.
        '''
        props = CfnModelExplainabilityJobDefinitionProps(
            job_definition_name=job_definition_name,
            job_resources=job_resources,
            model_explainability_app_specification=model_explainability_app_specification,
            model_explainability_baseline_config=model_explainability_baseline_config,
            model_explainability_job_input=model_explainability_job_input,
            model_explainability_job_output_config=model_explainability_job_output_config,
            network_config=network_config,
            role_arn=role_arn,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: JobDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobDefinitionArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"], jsii.get(self, "jobResources"))

    @job_resources.setter
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelExplainabilityAppSpecification")
    def model_explainability_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"], jsii.get(self, "modelExplainabilityAppSpecification"))

    @model_explainability_app_specification.setter
    def model_explainability_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityAppSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelExplainabilityBaselineConfig")
    def model_explainability_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]], jsii.get(self, "modelExplainabilityBaselineConfig"))

    @model_explainability_baseline_config.setter
    def model_explainability_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelExplainabilityBaselineConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelExplainabilityJobInput")
    def model_explainability_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"], jsii.get(self, "modelExplainabilityJobInput"))

    @model_explainability_job_input.setter
    def model_explainability_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityJobInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelExplainabilityJobOutputConfig")
    def model_explainability_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"], jsii.get(self, "modelExplainabilityJobOutputConfig"))

    @model_explainability_job_output_config.setter
    def model_explainability_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityJobOutputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]], jsii.get(self, "networkConfig"))

    @network_config.setter
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]], jsii.get(self, "stoppingCondition"))

    @stopping_condition.setter
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_kms_key_id": "volumeKmsKeyId",
            "volume_size_in_gb": "volumeSizeInGb",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
            volume_size_in_gb: jsii.Number,
        ) -> None:
            '''
            :param instance_count: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_kms_key_id: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.
            :param volume_size_in_gb: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                cluster_config_property = sagemaker.CfnModelExplainabilityJobDefinition.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
                
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                constraints_resource_property = sagemaker.CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html#cfn-sagemaker-modelexplainabilityjobdefinition-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "features_attribute": "featuresAttribute",
            "inference_attribute": "inferenceAttribute",
            "local_path": "localPath",
            "probability_attribute": "probabilityAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            features_attribute: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            local_path: builtins.str,
            probability_attribute: typing.Optional[builtins.str] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.EndpointName``.
            :param features_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.FeaturesAttribute``.
            :param inference_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param local_path: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.LocalPath``.
            :param probability_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param s3_data_distribution_type: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                endpoint_input_property = sagemaker.CfnModelExplainabilityJobDefinition.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
                
                    # the properties below are optional
                    features_attribute="featuresAttribute",
                    inference_attribute="inferenceAttribute",
                    probability_attribute="probabilityAttribute",
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if features_attribute is not None:
                self._values["features_attribute"] = features_attribute
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def features_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.FeaturesAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-featuresattribute
            '''
            result = self._values.get("features_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-inferenceattribute
            '''
            result = self._values.get("inference_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-probabilityattribute
            '''
            result = self._values.get("probability_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "config_uri": "configUri",
            "environment": "environment",
            "image_uri": "imageUri",
        },
    )
    class ModelExplainabilityAppSpecificationProperty:
        def __init__(
            self,
            *,
            config_uri: builtins.str,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            image_uri: builtins.str,
        ) -> None:
            '''
            :param config_uri: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ConfigUri``.
            :param environment: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.Environment``.
            :param image_uri: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_explainability_app_specification_property = sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty(
                    config_uri="configUri",
                    image_uri="imageUri",
                
                    # the properties below are optional
                    environment={
                        "environment_key": "environment"
                    }
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "config_uri": config_uri,
                "image_uri": image_uri,
            }
            if environment is not None:
                self._values["environment"] = environment

        @builtins.property
        def config_uri(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ConfigUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-configuri
            '''
            result = self._values.get("config_uri")
            assert result is not None, "Required property 'config_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelExplainabilityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            '''
            :param baselining_job_name: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_explainability_baseline_config_property = sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty(
                    baselining_job_name="baseliningJobName",
                    constraints_resource=sagemaker.CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.BaseliningJobName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig-baseliningjobname
            '''
            result = self._values.get("baselining_job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty"]]:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class ModelExplainabilityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EndpointInputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_explainability_job_input_property = sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty(
                    endpoint_input=sagemaker.CfnModelExplainabilityJobDefinition.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
                
                        # the properties below are optional
                        features_attribute="featuresAttribute",
                        inference_attribute="inferenceAttribute",
                        probability_attribute="probabilityAttribute",
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EndpointInputProperty"]:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EndpointInputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_id": "kmsKeyId",
            "monitoring_outputs": "monitoringOutputs",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputProperty"]]],
        ) -> None:
            '''
            :param kms_key_id: ``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.
            :param monitoring_outputs: ``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_config_property = sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnModelExplainabilityJobDefinition.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
                
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputProperty"]]]:
            '''``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnModelExplainabilityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_property = sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnModelExplainabilityJobDefinition.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.S3OutputProperty"]:
            '''``CfnModelExplainabilityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_resources_property = sagemaker.CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnModelExplainabilityJobDefinition.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
                
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ClusterConfigProperty"]:
            '''``CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                network_config_property = sagemaker.CfnModelExplainabilityJobDefinition.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnModelExplainabilityJobDefinition.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.VpcConfigProperty"]]:
            '''``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_upload_mode": "s3UploadMode",
            "s3_uri": "s3Uri",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
            s3_uri: builtins.str,
        ) -> None:
            '''
            :param local_path: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_upload_mode: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3UploadMode``.
            :param s3_uri: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                s3_output_property = sagemaker.CfnModelExplainabilityJobDefinition.S3OutputProperty(
                    local_path="localPath",
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    s3_upload_mode="s3UploadMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnModelExplainabilityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                stopping_condition_property = sagemaker.CfnModelExplainabilityJobDefinition.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnModelExplainabilityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnModelExplainabilityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelExplainabilityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                vpc_config_property = sagemaker.CfnModelExplainabilityJobDefinition.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_definition_name": "jobDefinitionName",
        "job_resources": "jobResources",
        "model_explainability_app_specification": "modelExplainabilityAppSpecification",
        "model_explainability_baseline_config": "modelExplainabilityBaselineConfig",
        "model_explainability_job_input": "modelExplainabilityJobInput",
        "model_explainability_job_output_config": "modelExplainabilityJobOutputConfig",
        "network_config": "networkConfig",
        "role_arn": "roleArn",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelExplainabilityJobDefinitionProps:
    def __init__(
        self,
        *,
        job_definition_name: typing.Optional[builtins.str] = None,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty],
        model_explainability_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty],
        model_explainability_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty]] = None,
        model_explainability_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty],
        model_explainability_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty],
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.NetworkConfigProperty]] = None,
        role_arn: builtins.str,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

        :param job_definition_name: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.
        :param job_resources: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.
        :param model_explainability_app_specification: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.
        :param model_explainability_baseline_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.
        :param model_explainability_job_input: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.
        :param model_explainability_job_output_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.
        :param network_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.
        :param role_arn: ``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.
        :param stopping_condition: ``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_model_explainability_job_definition_props = sagemaker.CfnModelExplainabilityJobDefinitionProps(
                job_resources=sagemaker.CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnModelExplainabilityJobDefinition.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
            
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                ),
                model_explainability_app_specification=sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty(
                    config_uri="configUri",
                    image_uri="imageUri",
            
                    # the properties below are optional
                    environment={
                        "environment_key": "environment"
                    }
                ),
                model_explainability_job_input=sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty(
                    endpoint_input=sagemaker.CfnModelExplainabilityJobDefinition.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
            
                        # the properties below are optional
                        features_attribute="featuresAttribute",
                        inference_attribute="inferenceAttribute",
                        probability_attribute="probabilityAttribute",
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode"
                    )
                ),
                model_explainability_job_output_config=sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnModelExplainabilityJobDefinition.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
            
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
            
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                job_definition_name="jobDefinitionName",
                model_explainability_baseline_config=sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty(
                    baselining_job_name="baseliningJobName",
                    constraints_resource=sagemaker.CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    )
                ),
                network_config=sagemaker.CfnModelExplainabilityJobDefinition.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnModelExplainabilityJobDefinition.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                ),
                stopping_condition=sagemaker.CfnModelExplainabilityJobDefinition.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_explainability_app_specification": model_explainability_app_specification,
            "model_explainability_job_input": model_explainability_job_input,
            "model_explainability_job_output_config": model_explainability_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_explainability_baseline_config is not None:
            self._values["model_explainability_baseline_config"] = model_explainability_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
        '''
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty], result)

    @builtins.property
    def model_explainability_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
        '''
        result = self._values.get("model_explainability_app_specification")
        assert result is not None, "Required property 'model_explainability_app_specification' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty], result)

    @builtins.property
    def model_explainability_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
        '''
        result = self._values.get("model_explainability_baseline_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty]], result)

    @builtins.property
    def model_explainability_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
        '''
        result = self._values.get("model_explainability_job_input")
        assert result is not None, "Required property 'model_explainability_job_input' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty], result)

    @builtins.property
    def model_explainability_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
        '''
        result = self._values.get("model_explainability_job_output_config")
        assert result is not None, "Required property 'model_explainability_job_output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.NetworkConfigProperty]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.NetworkConfigProperty]], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.StoppingConditionProperty]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
        '''
        result = self._values.get("stopping_condition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.StoppingConditionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelExplainabilityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelPackageGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelPackageGroup",
):
    '''A CloudFormation ``AWS::SageMaker::ModelPackageGroup``.

    :cloudformationResource: AWS::SageMaker::ModelPackageGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        # model_package_group_policy is of type object
        
        cfn_model_package_group = sagemaker.CfnModelPackageGroup(self, "MyCfnModelPackageGroup",
            model_package_group_name="modelPackageGroupName",
        
            # the properties below are optional
            model_package_group_description="modelPackageGroupDescription",
            model_package_group_policy=model_package_group_policy,
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        model_package_group_description: typing.Optional[builtins.str] = None,
        model_package_group_name: builtins.str,
        model_package_group_policy: typing.Any = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ModelPackageGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param model_package_group_description: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.
        :param model_package_group_name: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.
        :param model_package_group_policy: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.
        :param tags: ``AWS::SageMaker::ModelPackageGroup.Tags``.
        '''
        props = CfnModelPackageGroupProps(
            model_package_group_description=model_package_group_description,
            model_package_group_name=model_package_group_name,
            model_package_group_policy=model_package_group_policy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModelPackageGroupArn")
    def attr_model_package_group_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModelPackageGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModelPackageGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModelPackageGroupStatus")
    def attr_model_package_group_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModelPackageGroupStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModelPackageGroupStatus"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelPackageGroupDescription")
    def model_package_group_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelPackageGroupDescription"))

    @model_package_group_description.setter
    def model_package_group_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "modelPackageGroupDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelPackageGroupName")
    def model_package_group_name(self) -> builtins.str:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelPackageGroupName"))

    @model_package_group_name.setter
    def model_package_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "modelPackageGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelPackageGroupPolicy")
    def model_package_group_policy(self) -> typing.Any:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        '''
        return typing.cast(typing.Any, jsii.get(self, "modelPackageGroupPolicy"))

    @model_package_group_policy.setter
    def model_package_group_policy(self, value: typing.Any) -> None:
        jsii.set(self, "modelPackageGroupPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::ModelPackageGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelPackageGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "model_package_group_description": "modelPackageGroupDescription",
        "model_package_group_name": "modelPackageGroupName",
        "model_package_group_policy": "modelPackageGroupPolicy",
        "tags": "tags",
    },
)
class CfnModelPackageGroupProps:
    def __init__(
        self,
        *,
        model_package_group_description: typing.Optional[builtins.str] = None,
        model_package_group_name: builtins.str,
        model_package_group_policy: typing.Any = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::ModelPackageGroup``.

        :param model_package_group_description: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.
        :param model_package_group_name: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.
        :param model_package_group_policy: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.
        :param tags: ``AWS::SageMaker::ModelPackageGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            # model_package_group_policy is of type object
            
            cfn_model_package_group_props = sagemaker.CfnModelPackageGroupProps(
                model_package_group_name="modelPackageGroupName",
            
                # the properties below are optional
                model_package_group_description="modelPackageGroupDescription",
                model_package_group_policy=model_package_group_policy,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "model_package_group_name": model_package_group_name,
        }
        if model_package_group_description is not None:
            self._values["model_package_group_description"] = model_package_group_description
        if model_package_group_policy is not None:
            self._values["model_package_group_policy"] = model_package_group_policy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def model_package_group_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        '''
        result = self._values.get("model_package_group_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_package_group_name(self) -> builtins.str:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        '''
        result = self._values.get("model_package_group_name")
        assert result is not None, "Required property 'model_package_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_package_group_policy(self) -> typing.Any:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        '''
        result = self._values.get("model_package_group_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::ModelPackageGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelPackageGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "containers": "containers",
        "enable_network_isolation": "enableNetworkIsolation",
        "execution_role_arn": "executionRoleArn",
        "inference_execution_config": "inferenceExecutionConfig",
        "model_name": "modelName",
        "primary_container": "primaryContainer",
        "tags": "tags",
        "vpc_config": "vpcConfig",
    },
)
class CfnModelProps:
    def __init__(
        self,
        *,
        containers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]]] = None,
        enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        execution_role_arn: builtins.str,
        inference_execution_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.InferenceExecutionConfigProperty]] = None,
        model_name: typing.Optional[builtins.str] = None,
        primary_container: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.VpcConfigProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Model``.

        :param containers: ``AWS::SageMaker::Model.Containers``.
        :param enable_network_isolation: ``AWS::SageMaker::Model.EnableNetworkIsolation``.
        :param execution_role_arn: ``AWS::SageMaker::Model.ExecutionRoleArn``.
        :param inference_execution_config: ``AWS::SageMaker::Model.InferenceExecutionConfig``.
        :param model_name: ``AWS::SageMaker::Model.ModelName``.
        :param primary_container: ``AWS::SageMaker::Model.PrimaryContainer``.
        :param tags: ``AWS::SageMaker::Model.Tags``.
        :param vpc_config: ``AWS::SageMaker::Model.VpcConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            # environment is of type object
            
            cfn_model_props = sagemaker.CfnModelProps(
                execution_role_arn="executionRoleArn",
            
                # the properties below are optional
                containers=[sagemaker.CfnModel.ContainerDefinitionProperty(
                    container_hostname="containerHostname",
                    environment=environment,
                    image="image",
                    image_config=sagemaker.CfnModel.ImageConfigProperty(
                        repository_access_mode="repositoryAccessMode",
            
                        # the properties below are optional
                        repository_auth_config=sagemaker.CfnModel.RepositoryAuthConfigProperty(
                            repository_credentials_provider_arn="repositoryCredentialsProviderArn"
                        )
                    ),
                    inference_specification_name="inferenceSpecificationName",
                    mode="mode",
                    model_data_url="modelDataUrl",
                    model_package_name="modelPackageName",
                    multi_model_config=sagemaker.CfnModel.MultiModelConfigProperty(
                        model_cache_setting="modelCacheSetting"
                    )
                )],
                enable_network_isolation=False,
                inference_execution_config=sagemaker.CfnModel.InferenceExecutionConfigProperty(
                    mode="mode"
                ),
                model_name="modelName",
                primary_container=sagemaker.CfnModel.ContainerDefinitionProperty(
                    container_hostname="containerHostname",
                    environment=environment,
                    image="image",
                    image_config=sagemaker.CfnModel.ImageConfigProperty(
                        repository_access_mode="repositoryAccessMode",
            
                        # the properties below are optional
                        repository_auth_config=sagemaker.CfnModel.RepositoryAuthConfigProperty(
                            repository_credentials_provider_arn="repositoryCredentialsProviderArn"
                        )
                    ),
                    inference_specification_name="inferenceSpecificationName",
                    mode="mode",
                    model_data_url="modelDataUrl",
                    model_package_name="modelPackageName",
                    multi_model_config=sagemaker.CfnModel.MultiModelConfigProperty(
                        model_cache_setting="modelCacheSetting"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_config=sagemaker.CfnModel.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "execution_role_arn": execution_role_arn,
        }
        if containers is not None:
            self._values["containers"] = containers
        if enable_network_isolation is not None:
            self._values["enable_network_isolation"] = enable_network_isolation
        if inference_execution_config is not None:
            self._values["inference_execution_config"] = inference_execution_config
        if model_name is not None:
            self._values["model_name"] = model_name
        if primary_container is not None:
            self._values["primary_container"] = primary_container
        if tags is not None:
            self._values["tags"] = tags
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def containers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]]]:
        '''``AWS::SageMaker::Model.Containers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-containers
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]]], result)

    @builtins.property
    def enable_network_isolation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Model.EnableNetworkIsolation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-enablenetworkisolation
        '''
        result = self._values.get("enable_network_isolation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Model.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def inference_execution_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.InferenceExecutionConfigProperty]]:
        '''``AWS::SageMaker::Model.InferenceExecutionConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-inferenceexecutionconfig
        '''
        result = self._values.get("inference_execution_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.InferenceExecutionConfigProperty]], result)

    @builtins.property
    def model_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Model.ModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-modelname
        '''
        result = self._values.get("model_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_container(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]:
        '''``AWS::SageMaker::Model.PrimaryContainer``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-primarycontainer
        '''
        result = self._values.get("primary_container")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Model.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.VpcConfigProperty]]:
        '''``AWS::SageMaker::Model.VpcConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelQualityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition",
):
    '''A CloudFormation ``AWS::SageMaker::ModelQualityJobDefinition``.

    :cloudformationResource: AWS::SageMaker::ModelQualityJobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_model_quality_job_definition = sagemaker.CfnModelQualityJobDefinition(self, "MyCfnModelQualityJobDefinition",
            job_resources=sagemaker.CfnModelQualityJobDefinition.MonitoringResourcesProperty(
                cluster_config=sagemaker.CfnModelQualityJobDefinition.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
        
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            ),
            model_quality_app_specification=sagemaker.CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty(
                image_uri="imageUri",
                problem_type="problemType",
        
                # the properties below are optional
                container_arguments=["containerArguments"],
                container_entrypoint=["containerEntrypoint"],
                environment={
                    "environment_key": "environment"
                },
                post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                record_preprocessor_source_uri="recordPreprocessorSourceUri"
            ),
            model_quality_job_input=sagemaker.CfnModelQualityJobDefinition.ModelQualityJobInputProperty(
                endpoint_input=sagemaker.CfnModelQualityJobDefinition.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
        
                    # the properties below are optional
                    end_time_offset="endTimeOffset",
                    inference_attribute="inferenceAttribute",
                    probability_attribute="probabilityAttribute",
                    probability_threshold_attribute=123,
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode",
                    start_time_offset="startTimeOffset"
                ),
                ground_truth_s3_input=sagemaker.CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty(
                    s3_uri="s3Uri"
                )
            ),
            model_quality_job_output_config=sagemaker.CfnModelQualityJobDefinition.MonitoringOutputConfigProperty(
                monitoring_outputs=[sagemaker.CfnModelQualityJobDefinition.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnModelQualityJobDefinition.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
        
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )],
        
                # the properties below are optional
                kms_key_id="kmsKeyId"
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            job_definition_name="jobDefinitionName",
            model_quality_baseline_config=sagemaker.CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty(
                baselining_job_name="baseliningJobName",
                constraints_resource=sagemaker.CfnModelQualityJobDefinition.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                )
            ),
            network_config=sagemaker.CfnModelQualityJobDefinition.NetworkConfigProperty(
                enable_inter_container_traffic_encryption=False,
                enable_network_isolation=False,
                vpc_config=sagemaker.CfnModelQualityJobDefinition.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            ),
            stopping_condition=sagemaker.CfnModelQualityJobDefinition.StoppingConditionProperty(
                max_runtime_in_seconds=123
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_definition_name: typing.Optional[builtins.str] = None,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"],
        model_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"],
        model_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]] = None,
        model_quality_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"],
        model_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"],
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]] = None,
        role_arn: builtins.str,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ModelQualityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_definition_name: ``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.
        :param job_resources: ``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.
        :param model_quality_app_specification: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.
        :param model_quality_baseline_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.
        :param model_quality_job_input: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.
        :param model_quality_job_output_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.
        :param network_config: ``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.
        :param role_arn: ``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.
        :param stopping_condition: ``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelQualityJobDefinition.Tags``.
        '''
        props = CfnModelQualityJobDefinitionProps(
            job_definition_name=job_definition_name,
            job_resources=job_resources,
            model_quality_app_specification=model_quality_app_specification,
            model_quality_baseline_config=model_quality_baseline_config,
            model_quality_job_input=model_quality_job_input,
            model_quality_job_output_config=model_quality_job_output_config,
            network_config=network_config,
            role_arn=role_arn,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: JobDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobDefinitionArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobresources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"], jsii.get(self, "jobResources"))

    @job_resources.setter
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelQualityAppSpecification")
    def model_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"], jsii.get(self, "modelQualityAppSpecification"))

    @model_quality_app_specification.setter
    def model_quality_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelQualityAppSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelQualityBaselineConfig")
    def model_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]], jsii.get(self, "modelQualityBaselineConfig"))

    @model_quality_baseline_config.setter
    def model_quality_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelQualityBaselineConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelQualityJobInput")
    def model_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"], jsii.get(self, "modelQualityJobInput"))

    @model_quality_job_input.setter
    def model_quality_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelQualityJobInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelQualityJobOutputConfig")
    def model_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjoboutputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"], jsii.get(self, "modelQualityJobOutputConfig"))

    @model_quality_job_output_config.setter
    def model_quality_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelQualityJobOutputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]], jsii.get(self, "networkConfig"))

    @network_config.setter
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]], jsii.get(self, "stoppingCondition"))

    @stopping_condition.setter
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_kms_key_id": "volumeKmsKeyId",
            "volume_size_in_gb": "volumeSizeInGb",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
            volume_size_in_gb: jsii.Number,
        ) -> None:
            '''
            :param instance_count: ``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_kms_key_id: ``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.
            :param volume_size_in_gb: ``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                cluster_config_property = sagemaker.CfnModelQualityJobDefinition.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
                
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnModelQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                constraints_resource_property = sagemaker.CfnModelQualityJobDefinition.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html#cfn-sagemaker-modelqualityjobdefinition-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "end_time_offset": "endTimeOffset",
            "inference_attribute": "inferenceAttribute",
            "local_path": "localPath",
            "probability_attribute": "probabilityAttribute",
            "probability_threshold_attribute": "probabilityThresholdAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
            "start_time_offset": "startTimeOffset",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            end_time_offset: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            local_path: builtins.str,
            probability_attribute: typing.Optional[builtins.str] = None,
            probability_threshold_attribute: typing.Optional[jsii.Number] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
            start_time_offset: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnModelQualityJobDefinition.EndpointInputProperty.EndpointName``.
            :param end_time_offset: ``CfnModelQualityJobDefinition.EndpointInputProperty.EndTimeOffset``.
            :param inference_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param local_path: ``CfnModelQualityJobDefinition.EndpointInputProperty.LocalPath``.
            :param probability_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param probability_threshold_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.
            :param s3_data_distribution_type: ``CfnModelQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelQualityJobDefinition.EndpointInputProperty.S3InputMode``.
            :param start_time_offset: ``CfnModelQualityJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                endpoint_input_property = sagemaker.CfnModelQualityJobDefinition.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
                
                    # the properties below are optional
                    end_time_offset="endTimeOffset",
                    inference_attribute="inferenceAttribute",
                    probability_attribute="probabilityAttribute",
                    probability_threshold_attribute=123,
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode",
                    start_time_offset="startTimeOffset"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if end_time_offset is not None:
                self._values["end_time_offset"] = end_time_offset
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if probability_threshold_attribute is not None:
                self._values["probability_threshold_attribute"] = probability_threshold_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode
            if start_time_offset is not None:
                self._values["start_time_offset"] = start_time_offset

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.EndTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-endtimeoffset
            '''
            result = self._values.get("end_time_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-inferenceattribute
            '''
            result = self._values.get("inference_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-probabilityattribute
            '''
            result = self._values.get("probability_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def probability_threshold_attribute(self) -> typing.Optional[jsii.Number]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-probabilitythresholdattribute
            '''
            result = self._values.get("probability_threshold_attribute")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_time_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-starttimeoffset
            '''
            result = self._values.get("start_time_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "environment": "environment",
            "image_uri": "imageUri",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "problem_type": "problemType",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class ModelQualityAppSpecificationProperty:
        def __init__(
            self,
            *,
            container_arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            image_uri: builtins.str,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            problem_type: builtins.str,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param container_arguments: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerEntrypoint``.
            :param environment: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.Environment``.
            :param image_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ImageUri``.
            :param post_analytics_processor_source_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param problem_type: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ProblemType``.
            :param record_preprocessor_source_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_quality_app_specification_property = sagemaker.CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty(
                    image_uri="imageUri",
                    problem_type="problemType",
                
                    # the properties below are optional
                    container_arguments=["containerArguments"],
                    container_entrypoint=["containerEntrypoint"],
                    environment={
                        "environment_key": "environment"
                    },
                    post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                    record_preprocessor_source_uri="recordPreprocessorSourceUri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
                "problem_type": problem_type,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if environment is not None:
                self._values["environment"] = environment
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerArguments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-containerarguments
            '''
            result = self._values.get("container_arguments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerEntrypoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-containerentrypoint
            '''
            result = self._values.get("container_entrypoint")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-postanalyticsprocessorsourceuri
            '''
            result = self._values.get("post_analytics_processor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def problem_type(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ProblemType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-problemtype
            '''
            result = self._values.get("problem_type")
            assert result is not None, "Required property 'problem_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-recordpreprocessorsourceuri
            '''
            result = self._values.get("record_preprocessor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelQualityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            '''
            :param baselining_job_name: ``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_quality_baseline_config_property = sagemaker.CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty(
                    baselining_job_name="baseliningJobName",
                    constraints_resource=sagemaker.CfnModelQualityJobDefinition.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.BaseliningJobName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-baseliningjobname
            '''
            result = self._values.get("baselining_job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ConstraintsResourceProperty"]]:
            '''``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ConstraintsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_input": "endpointInput",
            "ground_truth_s3_input": "groundTruthS3Input",
        },
    )
    class ModelQualityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EndpointInputProperty"],
            ground_truth_s3_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.EndpointInput``.
            :param ground_truth_s3_input: ``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.GroundTruthS3Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                model_quality_job_input_property = sagemaker.CfnModelQualityJobDefinition.ModelQualityJobInputProperty(
                    endpoint_input=sagemaker.CfnModelQualityJobDefinition.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
                
                        # the properties below are optional
                        end_time_offset="endTimeOffset",
                        inference_attribute="inferenceAttribute",
                        probability_attribute="probabilityAttribute",
                        probability_threshold_attribute=123,
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode",
                        start_time_offset="startTimeOffset"
                    ),
                    ground_truth_s3_input=sagemaker.CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty(
                        s3_uri="s3Uri"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
                "ground_truth_s3_input": ground_truth_s3_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EndpointInputProperty"]:
            '''``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EndpointInputProperty"], result)

        @builtins.property
        def ground_truth_s3_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty"]:
            '''``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.GroundTruthS3Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-groundtruths3input
            '''
            result = self._values.get("ground_truth_s3_input")
            assert result is not None, "Required property 'ground_truth_s3_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class MonitoringGroundTruthS3InputProperty:
        def __init__(self, *, s3_uri: builtins.str) -> None:
            '''
            :param s3_uri: ``CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_ground_truth_s3_input_property = sagemaker.CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_uri": s3_uri,
            }

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html#cfn-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringGroundTruthS3InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_id": "kmsKeyId",
            "monitoring_outputs": "monitoringOutputs",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputProperty"]]],
        ) -> None:
            '''
            :param kms_key_id: ``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.
            :param monitoring_outputs: ``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_config_property = sagemaker.CfnModelQualityJobDefinition.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnModelQualityJobDefinition.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnModelQualityJobDefinition.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
                
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputProperty"]]]:
            '''``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnModelQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_property = sagemaker.CfnModelQualityJobDefinition.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnModelQualityJobDefinition.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.S3OutputProperty"]:
            '''``CfnModelQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnModelQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_resources_property = sagemaker.CfnModelQualityJobDefinition.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnModelQualityJobDefinition.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
                
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ClusterConfigProperty"]:
            '''``CfnModelQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html#cfn-sagemaker-modelqualityjobdefinition-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                network_config_property = sagemaker.CfnModelQualityJobDefinition.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnModelQualityJobDefinition.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.VpcConfigProperty"]]:
            '''``CfnModelQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_upload_mode": "s3UploadMode",
            "s3_uri": "s3Uri",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
            s3_uri: builtins.str,
        ) -> None:
            '''
            :param local_path: ``CfnModelQualityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_upload_mode: ``CfnModelQualityJobDefinition.S3OutputProperty.S3UploadMode``.
            :param s3_uri: ``CfnModelQualityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                s3_output_property = sagemaker.CfnModelQualityJobDefinition.S3OutputProperty(
                    local_path="localPath",
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    s3_upload_mode="s3UploadMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnModelQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                stopping_condition_property = sagemaker.CfnModelQualityJobDefinition.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnModelQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnModelQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelQualityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                vpc_config_property = sagemaker.CfnModelQualityJobDefinition.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnModelQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html#cfn-sagemaker-modelqualityjobdefinition-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnModelQualityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html#cfn-sagemaker-modelqualityjobdefinition-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_definition_name": "jobDefinitionName",
        "job_resources": "jobResources",
        "model_quality_app_specification": "modelQualityAppSpecification",
        "model_quality_baseline_config": "modelQualityBaselineConfig",
        "model_quality_job_input": "modelQualityJobInput",
        "model_quality_job_output_config": "modelQualityJobOutputConfig",
        "network_config": "networkConfig",
        "role_arn": "roleArn",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelQualityJobDefinitionProps:
    def __init__(
        self,
        *,
        job_definition_name: typing.Optional[builtins.str] = None,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringResourcesProperty],
        model_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty],
        model_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty]] = None,
        model_quality_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityJobInputProperty],
        model_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringOutputConfigProperty],
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.NetworkConfigProperty]] = None,
        role_arn: builtins.str,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::ModelQualityJobDefinition``.

        :param job_definition_name: ``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.
        :param job_resources: ``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.
        :param model_quality_app_specification: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.
        :param model_quality_baseline_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.
        :param model_quality_job_input: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.
        :param model_quality_job_output_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.
        :param network_config: ``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.
        :param role_arn: ``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.
        :param stopping_condition: ``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_model_quality_job_definition_props = sagemaker.CfnModelQualityJobDefinitionProps(
                job_resources=sagemaker.CfnModelQualityJobDefinition.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnModelQualityJobDefinition.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
            
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                ),
                model_quality_app_specification=sagemaker.CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty(
                    image_uri="imageUri",
                    problem_type="problemType",
            
                    # the properties below are optional
                    container_arguments=["containerArguments"],
                    container_entrypoint=["containerEntrypoint"],
                    environment={
                        "environment_key": "environment"
                    },
                    post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                    record_preprocessor_source_uri="recordPreprocessorSourceUri"
                ),
                model_quality_job_input=sagemaker.CfnModelQualityJobDefinition.ModelQualityJobInputProperty(
                    endpoint_input=sagemaker.CfnModelQualityJobDefinition.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
            
                        # the properties below are optional
                        end_time_offset="endTimeOffset",
                        inference_attribute="inferenceAttribute",
                        probability_attribute="probabilityAttribute",
                        probability_threshold_attribute=123,
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode",
                        start_time_offset="startTimeOffset"
                    ),
                    ground_truth_s3_input=sagemaker.CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty(
                        s3_uri="s3Uri"
                    )
                ),
                model_quality_job_output_config=sagemaker.CfnModelQualityJobDefinition.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnModelQualityJobDefinition.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnModelQualityJobDefinition.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
            
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
            
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                job_definition_name="jobDefinitionName",
                model_quality_baseline_config=sagemaker.CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty(
                    baselining_job_name="baseliningJobName",
                    constraints_resource=sagemaker.CfnModelQualityJobDefinition.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    )
                ),
                network_config=sagemaker.CfnModelQualityJobDefinition.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnModelQualityJobDefinition.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                ),
                stopping_condition=sagemaker.CfnModelQualityJobDefinition.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_quality_app_specification": model_quality_app_specification,
            "model_quality_job_input": model_quality_job_input,
            "model_quality_job_output_config": model_quality_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_quality_baseline_config is not None:
            self._values["model_quality_baseline_config"] = model_quality_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringResourcesProperty]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobresources
        '''
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringResourcesProperty], result)

    @builtins.property
    def model_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification
        '''
        result = self._values.get("model_quality_app_specification")
        assert result is not None, "Required property 'model_quality_app_specification' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty], result)

    @builtins.property
    def model_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig
        '''
        result = self._values.get("model_quality_baseline_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty]], result)

    @builtins.property
    def model_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityJobInputProperty]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput
        '''
        result = self._values.get("model_quality_job_input")
        assert result is not None, "Required property 'model_quality_job_input' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityJobInputProperty], result)

    @builtins.property
    def model_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringOutputConfigProperty]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjoboutputconfig
        '''
        result = self._values.get("model_quality_job_output_config")
        assert result is not None, "Required property 'model_quality_job_output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringOutputConfigProperty], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.NetworkConfigProperty]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.NetworkConfigProperty]], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.StoppingConditionProperty]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition
        '''
        result = self._values.get("stopping_condition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.StoppingConditionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelQualityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMonitoringSchedule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule",
):
    '''A CloudFormation ``AWS::SageMaker::MonitoringSchedule``.

    :cloudformationResource: AWS::SageMaker::MonitoringSchedule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_monitoring_schedule = sagemaker.CfnMonitoringSchedule(self, "MyCfnMonitoringSchedule",
            monitoring_schedule_config=sagemaker.CfnMonitoringSchedule.MonitoringScheduleConfigProperty(
                monitoring_job_definition=sagemaker.CfnMonitoringSchedule.MonitoringJobDefinitionProperty(
                    monitoring_app_specification=sagemaker.CfnMonitoringSchedule.MonitoringAppSpecificationProperty(
                        image_uri="imageUri",
        
                        # the properties below are optional
                        container_arguments=["containerArguments"],
                        container_entrypoint=["containerEntrypoint"],
                        post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                        record_preprocessor_source_uri="recordPreprocessorSourceUri"
                    ),
                    monitoring_inputs=[sagemaker.CfnMonitoringSchedule.MonitoringInputProperty(
                        endpoint_input=sagemaker.CfnMonitoringSchedule.EndpointInputProperty(
                            endpoint_name="endpointName",
                            local_path="localPath",
        
                            # the properties below are optional
                            s3_data_distribution_type="s3DataDistributionType",
                            s3_input_mode="s3InputMode"
                        )
                    )],
                    monitoring_output_config=sagemaker.CfnMonitoringSchedule.MonitoringOutputConfigProperty(
                        monitoring_outputs=[sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty(
                            s3_output=sagemaker.CfnMonitoringSchedule.S3OutputProperty(
                                local_path="localPath",
                                s3_uri="s3Uri",
        
                                # the properties below are optional
                                s3_upload_mode="s3UploadMode"
                            )
                        )],
        
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    ),
                    monitoring_resources=sagemaker.CfnMonitoringSchedule.MonitoringResourcesProperty(
                        cluster_config=sagemaker.CfnMonitoringSchedule.ClusterConfigProperty(
                            instance_count=123,
                            instance_type="instanceType",
                            volume_size_in_gb=123,
        
                            # the properties below are optional
                            volume_kms_key_id="volumeKmsKeyId"
                        )
                    ),
                    role_arn="roleArn",
        
                    # the properties below are optional
                    baseline_config=sagemaker.CfnMonitoringSchedule.BaselineConfigProperty(
                        constraints_resource=sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty(
                            s3_uri="s3Uri"
                        ),
                        statistics_resource=sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty(
                            s3_uri="s3Uri"
                        )
                    ),
                    environment={
                        "environment_key": "environment"
                    },
                    network_config=sagemaker.CfnMonitoringSchedule.NetworkConfigProperty(
                        enable_inter_container_traffic_encryption=False,
                        enable_network_isolation=False,
                        vpc_config=sagemaker.CfnMonitoringSchedule.VpcConfigProperty(
                            security_group_ids=["securityGroupIds"],
                            subnets=["subnets"]
                        )
                    ),
                    stopping_condition=sagemaker.CfnMonitoringSchedule.StoppingConditionProperty(
                        max_runtime_in_seconds=123
                    )
                ),
                monitoring_job_definition_name="monitoringJobDefinitionName",
                monitoring_type="monitoringType",
                schedule_config=sagemaker.CfnMonitoringSchedule.ScheduleConfigProperty(
                    schedule_expression="scheduleExpression"
                )
            ),
            monitoring_schedule_name="monitoringScheduleName",
        
            # the properties below are optional
            endpoint_name="endpointName",
            failure_reason="failureReason",
            last_monitoring_execution_summary=sagemaker.CfnMonitoringSchedule.MonitoringExecutionSummaryProperty(
                creation_time="creationTime",
                last_modified_time="lastModifiedTime",
                monitoring_execution_status="monitoringExecutionStatus",
                monitoring_schedule_name="monitoringScheduleName",
                scheduled_time="scheduledTime",
        
                # the properties below are optional
                endpoint_name="endpointName",
                failure_reason="failureReason",
                processing_job_arn="processingJobArn"
            ),
            monitoring_schedule_status="monitoringScheduleStatus",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        endpoint_name: typing.Optional[builtins.str] = None,
        failure_reason: typing.Optional[builtins.str] = None,
        last_monitoring_execution_summary: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]] = None,
        monitoring_schedule_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"],
        monitoring_schedule_name: builtins.str,
        monitoring_schedule_status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::MonitoringSchedule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_name: ``AWS::SageMaker::MonitoringSchedule.EndpointName``.
        :param failure_reason: ``AWS::SageMaker::MonitoringSchedule.FailureReason``.
        :param last_monitoring_execution_summary: ``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.
        :param monitoring_schedule_config: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.
        :param monitoring_schedule_name: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.
        :param monitoring_schedule_status: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.
        :param tags: ``AWS::SageMaker::MonitoringSchedule.Tags``.
        '''
        props = CfnMonitoringScheduleProps(
            endpoint_name=endpoint_name,
            failure_reason=failure_reason,
            last_monitoring_execution_summary=last_monitoring_execution_summary,
            monitoring_schedule_config=monitoring_schedule_config,
            monitoring_schedule_name=monitoring_schedule_name,
            monitoring_schedule_status=monitoring_schedule_status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMonitoringScheduleArn")
    def attr_monitoring_schedule_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: MonitoringScheduleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMonitoringScheduleArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.EndpointName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-endpointname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointName"))

    @endpoint_name.setter
    def endpoint_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="failureReason")
    def failure_reason(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.FailureReason``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-failurereason
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failureReason"))

    @failure_reason.setter
    def failure_reason(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "failureReason", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lastMonitoringExecutionSummary")
    def last_monitoring_execution_summary(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]]:
        '''``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-lastmonitoringexecutionsummary
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]], jsii.get(self, "lastMonitoringExecutionSummary"))

    @last_monitoring_execution_summary.setter
    def last_monitoring_execution_summary(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]],
    ) -> None:
        jsii.set(self, "lastMonitoringExecutionSummary", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="monitoringScheduleConfig")
    def monitoring_schedule_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"]:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"], jsii.get(self, "monitoringScheduleConfig"))

    @monitoring_schedule_config.setter
    def monitoring_schedule_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"],
    ) -> None:
        jsii.set(self, "monitoringScheduleConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="monitoringScheduleName")
    def monitoring_schedule_name(self) -> builtins.str:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulename
        '''
        return typing.cast(builtins.str, jsii.get(self, "monitoringScheduleName"))

    @monitoring_schedule_name.setter
    def monitoring_schedule_name(self, value: builtins.str) -> None:
        jsii.set(self, "monitoringScheduleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="monitoringScheduleStatus")
    def monitoring_schedule_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulestatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitoringScheduleStatus"))

    @monitoring_schedule_status.setter
    def monitoring_schedule_status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "monitoringScheduleStatus", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::MonitoringSchedule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.BaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "constraints_resource": "constraintsResource",
            "statistics_resource": "statisticsResource",
        },
    )
    class BaselineConfigProperty:
        def __init__(
            self,
            *,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ConstraintsResourceProperty"]] = None,
            statistics_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StatisticsResourceProperty"]] = None,
        ) -> None:
            '''
            :param constraints_resource: ``CfnMonitoringSchedule.BaselineConfigProperty.ConstraintsResource``.
            :param statistics_resource: ``CfnMonitoringSchedule.BaselineConfigProperty.StatisticsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                baseline_config_property = sagemaker.CfnMonitoringSchedule.BaselineConfigProperty(
                    constraints_resource=sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty(
                        s3_uri="s3Uri"
                    ),
                    statistics_resource=sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty(
                        s3_uri="s3Uri"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource
            if statistics_resource is not None:
                self._values["statistics_resource"] = statistics_resource

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ConstraintsResourceProperty"]]:
            '''``CfnMonitoringSchedule.BaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html#cfn-sagemaker-monitoringschedule-baselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ConstraintsResourceProperty"]], result)

        @builtins.property
        def statistics_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StatisticsResourceProperty"]]:
            '''``CfnMonitoringSchedule.BaselineConfigProperty.StatisticsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html#cfn-sagemaker-monitoringschedule-baselineconfig-statisticsresource
            '''
            result = self._values.get("statistics_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StatisticsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_kms_key_id": "volumeKmsKeyId",
            "volume_size_in_gb": "volumeSizeInGb",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
            volume_size_in_gb: jsii.Number,
        ) -> None:
            '''
            :param instance_count: ``CfnMonitoringSchedule.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnMonitoringSchedule.ClusterConfigProperty.InstanceType``.
            :param volume_kms_key_id: ``CfnMonitoringSchedule.ClusterConfigProperty.VolumeKmsKeyId``.
            :param volume_size_in_gb: ``CfnMonitoringSchedule.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                cluster_config_property = sagemaker.CfnMonitoringSchedule.ClusterConfigProperty(
                    instance_count=123,
                    instance_type="instanceType",
                    volume_size_in_gb=123,
                
                    # the properties below are optional
                    volume_kms_key_id="volumeKmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnMonitoringSchedule.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnMonitoringSchedule.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnMonitoringSchedule.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnMonitoringSchedule.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                constraints_resource_property = sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html#cfn-sagemaker-monitoringschedule-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnMonitoringSchedule.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnMonitoringSchedule.EndpointInputProperty.LocalPath``.
            :param s3_data_distribution_type: ``CfnMonitoringSchedule.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnMonitoringSchedule.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                endpoint_input_property = sagemaker.CfnMonitoringSchedule.EndpointInputProperty(
                    endpoint_name="endpointName",
                    local_path="localPath",
                
                    # the properties below are optional
                    s3_data_distribution_type="s3DataDistributionType",
                    s3_input_mode="s3InputMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnMonitoringSchedule.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnMonitoringSchedule.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "image_uri": "imageUri",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class MonitoringAppSpecificationProperty:
        def __init__(
            self,
            *,
            container_arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
            image_uri: builtins.str,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param container_arguments: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerEntrypoint``.
            :param image_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ImageUri``.
            :param post_analytics_processor_source_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param record_preprocessor_source_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_app_specification_property = sagemaker.CfnMonitoringSchedule.MonitoringAppSpecificationProperty(
                    image_uri="imageUri",
                
                    # the properties below are optional
                    container_arguments=["containerArguments"],
                    container_entrypoint=["containerEntrypoint"],
                    post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                    record_preprocessor_source_uri="recordPreprocessorSourceUri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerArguments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerarguments
            '''
            result = self._values.get("container_arguments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerEntrypoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerentrypoint
            '''
            result = self._values.get("container_entrypoint")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-postanalyticsprocessorsourceuri
            '''
            result = self._values.get("post_analytics_processor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-recordpreprocessorsourceuri
            '''
            result = self._values.get("record_preprocessor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringExecutionSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "creation_time": "creationTime",
            "endpoint_name": "endpointName",
            "failure_reason": "failureReason",
            "last_modified_time": "lastModifiedTime",
            "monitoring_execution_status": "monitoringExecutionStatus",
            "monitoring_schedule_name": "monitoringScheduleName",
            "processing_job_arn": "processingJobArn",
            "scheduled_time": "scheduledTime",
        },
    )
    class MonitoringExecutionSummaryProperty:
        def __init__(
            self,
            *,
            creation_time: builtins.str,
            endpoint_name: typing.Optional[builtins.str] = None,
            failure_reason: typing.Optional[builtins.str] = None,
            last_modified_time: builtins.str,
            monitoring_execution_status: builtins.str,
            monitoring_schedule_name: builtins.str,
            processing_job_arn: typing.Optional[builtins.str] = None,
            scheduled_time: builtins.str,
        ) -> None:
            '''
            :param creation_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.CreationTime``.
            :param endpoint_name: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.EndpointName``.
            :param failure_reason: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.FailureReason``.
            :param last_modified_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.LastModifiedTime``.
            :param monitoring_execution_status: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringExecutionStatus``.
            :param monitoring_schedule_name: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringScheduleName``.
            :param processing_job_arn: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ProcessingJobArn``.
            :param scheduled_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ScheduledTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_execution_summary_property = sagemaker.CfnMonitoringSchedule.MonitoringExecutionSummaryProperty(
                    creation_time="creationTime",
                    last_modified_time="lastModifiedTime",
                    monitoring_execution_status="monitoringExecutionStatus",
                    monitoring_schedule_name="monitoringScheduleName",
                    scheduled_time="scheduledTime",
                
                    # the properties below are optional
                    endpoint_name="endpointName",
                    failure_reason="failureReason",
                    processing_job_arn="processingJobArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "creation_time": creation_time,
                "last_modified_time": last_modified_time,
                "monitoring_execution_status": monitoring_execution_status,
                "monitoring_schedule_name": monitoring_schedule_name,
                "scheduled_time": scheduled_time,
            }
            if endpoint_name is not None:
                self._values["endpoint_name"] = endpoint_name
            if failure_reason is not None:
                self._values["failure_reason"] = failure_reason
            if processing_job_arn is not None:
                self._values["processing_job_arn"] = processing_job_arn

        @builtins.property
        def creation_time(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.CreationTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-creationtime
            '''
            result = self._values.get("creation_time")
            assert result is not None, "Required property 'creation_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoint_name(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-endpointname
            '''
            result = self._values.get("endpoint_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def failure_reason(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.FailureReason``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-failurereason
            '''
            result = self._values.get("failure_reason")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_modified_time(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.LastModifiedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-lastmodifiedtime
            '''
            result = self._values.get("last_modified_time")
            assert result is not None, "Required property 'last_modified_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def monitoring_execution_status(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringExecutionStatus``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-monitoringexecutionstatus
            '''
            result = self._values.get("monitoring_execution_status")
            assert result is not None, "Required property 'monitoring_execution_status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def monitoring_schedule_name(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringScheduleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-monitoringschedulename
            '''
            result = self._values.get("monitoring_schedule_name")
            assert result is not None, "Required property 'monitoring_schedule_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def processing_job_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ProcessingJobArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-processingjobarn
            '''
            result = self._values.get("processing_job_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scheduled_time(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ScheduledTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-scheduledtime
            '''
            result = self._values.get("scheduled_time")
            assert result is not None, "Required property 'scheduled_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringExecutionSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class MonitoringInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EndpointInputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnMonitoringSchedule.MonitoringInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_input_property = sagemaker.CfnMonitoringSchedule.MonitoringInputProperty(
                    endpoint_input=sagemaker.CfnMonitoringSchedule.EndpointInputProperty(
                        endpoint_name="endpointName",
                        local_path="localPath",
                
                        # the properties below are optional
                        s3_data_distribution_type="s3DataDistributionType",
                        s3_input_mode="s3InputMode"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EndpointInputProperty"]:
            '''``CfnMonitoringSchedule.MonitoringInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html#cfn-sagemaker-monitoringschedule-monitoringinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EndpointInputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringJobDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baseline_config": "baselineConfig",
            "environment": "environment",
            "monitoring_app_specification": "monitoringAppSpecification",
            "monitoring_inputs": "monitoringInputs",
            "monitoring_output_config": "monitoringOutputConfig",
            "monitoring_resources": "monitoringResources",
            "network_config": "networkConfig",
            "role_arn": "roleArn",
            "stopping_condition": "stoppingCondition",
        },
    )
    class MonitoringJobDefinitionProperty:
        def __init__(
            self,
            *,
            baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.BaselineConfigProperty"]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            monitoring_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringAppSpecificationProperty"],
            monitoring_inputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputProperty"]]],
            monitoring_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputConfigProperty"],
            monitoring_resources: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringResourcesProperty"],
            network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.NetworkConfigProperty"]] = None,
            role_arn: builtins.str,
            stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StoppingConditionProperty"]] = None,
        ) -> None:
            '''
            :param baseline_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.BaselineConfig``.
            :param environment: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.Environment``.
            :param monitoring_app_specification: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringAppSpecification``.
            :param monitoring_inputs: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringInputs``.
            :param monitoring_output_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringOutputConfig``.
            :param monitoring_resources: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringResources``.
            :param network_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.NetworkConfig``.
            :param role_arn: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.RoleArn``.
            :param stopping_condition: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.StoppingCondition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_job_definition_property = sagemaker.CfnMonitoringSchedule.MonitoringJobDefinitionProperty(
                    monitoring_app_specification=sagemaker.CfnMonitoringSchedule.MonitoringAppSpecificationProperty(
                        image_uri="imageUri",
                
                        # the properties below are optional
                        container_arguments=["containerArguments"],
                        container_entrypoint=["containerEntrypoint"],
                        post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                        record_preprocessor_source_uri="recordPreprocessorSourceUri"
                    ),
                    monitoring_inputs=[sagemaker.CfnMonitoringSchedule.MonitoringInputProperty(
                        endpoint_input=sagemaker.CfnMonitoringSchedule.EndpointInputProperty(
                            endpoint_name="endpointName",
                            local_path="localPath",
                
                            # the properties below are optional
                            s3_data_distribution_type="s3DataDistributionType",
                            s3_input_mode="s3InputMode"
                        )
                    )],
                    monitoring_output_config=sagemaker.CfnMonitoringSchedule.MonitoringOutputConfigProperty(
                        monitoring_outputs=[sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty(
                            s3_output=sagemaker.CfnMonitoringSchedule.S3OutputProperty(
                                local_path="localPath",
                                s3_uri="s3Uri",
                
                                # the properties below are optional
                                s3_upload_mode="s3UploadMode"
                            )
                        )],
                
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    ),
                    monitoring_resources=sagemaker.CfnMonitoringSchedule.MonitoringResourcesProperty(
                        cluster_config=sagemaker.CfnMonitoringSchedule.ClusterConfigProperty(
                            instance_count=123,
                            instance_type="instanceType",
                            volume_size_in_gb=123,
                
                            # the properties below are optional
                            volume_kms_key_id="volumeKmsKeyId"
                        )
                    ),
                    role_arn="roleArn",
                
                    # the properties below are optional
                    baseline_config=sagemaker.CfnMonitoringSchedule.BaselineConfigProperty(
                        constraints_resource=sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty(
                            s3_uri="s3Uri"
                        ),
                        statistics_resource=sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty(
                            s3_uri="s3Uri"
                        )
                    ),
                    environment={
                        "environment_key": "environment"
                    },
                    network_config=sagemaker.CfnMonitoringSchedule.NetworkConfigProperty(
                        enable_inter_container_traffic_encryption=False,
                        enable_network_isolation=False,
                        vpc_config=sagemaker.CfnMonitoringSchedule.VpcConfigProperty(
                            security_group_ids=["securityGroupIds"],
                            subnets=["subnets"]
                        )
                    ),
                    stopping_condition=sagemaker.CfnMonitoringSchedule.StoppingConditionProperty(
                        max_runtime_in_seconds=123
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_app_specification": monitoring_app_specification,
                "monitoring_inputs": monitoring_inputs,
                "monitoring_output_config": monitoring_output_config,
                "monitoring_resources": monitoring_resources,
                "role_arn": role_arn,
            }
            if baseline_config is not None:
                self._values["baseline_config"] = baseline_config
            if environment is not None:
                self._values["environment"] = environment
            if network_config is not None:
                self._values["network_config"] = network_config
            if stopping_condition is not None:
                self._values["stopping_condition"] = stopping_condition

        @builtins.property
        def baseline_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.BaselineConfigProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.BaselineConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-baselineconfig
            '''
            result = self._values.get("baseline_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.BaselineConfigProperty"]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def monitoring_app_specification(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringAppSpecificationProperty"]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringAppSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringappspecification
            '''
            result = self._values.get("monitoring_app_specification")
            assert result is not None, "Required property 'monitoring_app_specification' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringAppSpecificationProperty"], result)

        @builtins.property
        def monitoring_inputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputProperty"]]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringInputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringinputs
            '''
            result = self._values.get("monitoring_inputs")
            assert result is not None, "Required property 'monitoring_inputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputProperty"]]], result)

        @builtins.property
        def monitoring_output_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputConfigProperty"]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringOutputConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringoutputconfig
            '''
            result = self._values.get("monitoring_output_config")
            assert result is not None, "Required property 'monitoring_output_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputConfigProperty"], result)

        @builtins.property
        def monitoring_resources(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringResourcesProperty"]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringResources``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringresources
            '''
            result = self._values.get("monitoring_resources")
            assert result is not None, "Required property 'monitoring_resources' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringResourcesProperty"], result)

        @builtins.property
        def network_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.NetworkConfigProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.NetworkConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-networkconfig
            '''
            result = self._values.get("network_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.NetworkConfigProperty"]], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def stopping_condition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StoppingConditionProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.StoppingCondition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-stoppingcondition
            '''
            result = self._values.get("stopping_condition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StoppingConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringJobDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_id": "kmsKeyId",
            "monitoring_outputs": "monitoringOutputs",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputProperty"]]],
        ) -> None:
            '''
            :param kms_key_id: ``CfnMonitoringSchedule.MonitoringOutputConfigProperty.KmsKeyId``.
            :param monitoring_outputs: ``CfnMonitoringSchedule.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_config_property = sagemaker.CfnMonitoringSchedule.MonitoringOutputConfigProperty(
                    monitoring_outputs=[sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty(
                        s3_output=sagemaker.CfnMonitoringSchedule.S3OutputProperty(
                            local_path="localPath",
                            s3_uri="s3Uri",
                
                            # the properties below are optional
                            s3_upload_mode="s3UploadMode"
                        )
                    )],
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html#cfn-sagemaker-monitoringschedule-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputProperty"]]]:
            '''``CfnMonitoringSchedule.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html#cfn-sagemaker-monitoringschedule-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnMonitoringSchedule.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_output_property = sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty(
                    s3_output=sagemaker.CfnMonitoringSchedule.S3OutputProperty(
                        local_path="localPath",
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        s3_upload_mode="s3UploadMode"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.S3OutputProperty"]:
            '''``CfnMonitoringSchedule.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html#cfn-sagemaker-monitoringschedule-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnMonitoringSchedule.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_resources_property = sagemaker.CfnMonitoringSchedule.MonitoringResourcesProperty(
                    cluster_config=sagemaker.CfnMonitoringSchedule.ClusterConfigProperty(
                        instance_count=123,
                        instance_type="instanceType",
                        volume_size_in_gb=123,
                
                        # the properties below are optional
                        volume_kms_key_id="volumeKmsKeyId"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ClusterConfigProperty"]:
            '''``CfnMonitoringSchedule.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html#cfn-sagemaker-monitoringschedule-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringScheduleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_job_definition": "monitoringJobDefinition",
            "monitoring_job_definition_name": "monitoringJobDefinitionName",
            "monitoring_type": "monitoringType",
            "schedule_config": "scheduleConfig",
        },
    )
    class MonitoringScheduleConfigProperty:
        def __init__(
            self,
            *,
            monitoring_job_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringJobDefinitionProperty"]] = None,
            monitoring_job_definition_name: typing.Optional[builtins.str] = None,
            monitoring_type: typing.Optional[builtins.str] = None,
            schedule_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ScheduleConfigProperty"]] = None,
        ) -> None:
            '''
            :param monitoring_job_definition: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinition``.
            :param monitoring_job_definition_name: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinitionName``.
            :param monitoring_type: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringType``.
            :param schedule_config: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.ScheduleConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                monitoring_schedule_config_property = sagemaker.CfnMonitoringSchedule.MonitoringScheduleConfigProperty(
                    monitoring_job_definition=sagemaker.CfnMonitoringSchedule.MonitoringJobDefinitionProperty(
                        monitoring_app_specification=sagemaker.CfnMonitoringSchedule.MonitoringAppSpecificationProperty(
                            image_uri="imageUri",
                
                            # the properties below are optional
                            container_arguments=["containerArguments"],
                            container_entrypoint=["containerEntrypoint"],
                            post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                            record_preprocessor_source_uri="recordPreprocessorSourceUri"
                        ),
                        monitoring_inputs=[sagemaker.CfnMonitoringSchedule.MonitoringInputProperty(
                            endpoint_input=sagemaker.CfnMonitoringSchedule.EndpointInputProperty(
                                endpoint_name="endpointName",
                                local_path="localPath",
                
                                # the properties below are optional
                                s3_data_distribution_type="s3DataDistributionType",
                                s3_input_mode="s3InputMode"
                            )
                        )],
                        monitoring_output_config=sagemaker.CfnMonitoringSchedule.MonitoringOutputConfigProperty(
                            monitoring_outputs=[sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty(
                                s3_output=sagemaker.CfnMonitoringSchedule.S3OutputProperty(
                                    local_path="localPath",
                                    s3_uri="s3Uri",
                
                                    # the properties below are optional
                                    s3_upload_mode="s3UploadMode"
                                )
                            )],
                
                            # the properties below are optional
                            kms_key_id="kmsKeyId"
                        ),
                        monitoring_resources=sagemaker.CfnMonitoringSchedule.MonitoringResourcesProperty(
                            cluster_config=sagemaker.CfnMonitoringSchedule.ClusterConfigProperty(
                                instance_count=123,
                                instance_type="instanceType",
                                volume_size_in_gb=123,
                
                                # the properties below are optional
                                volume_kms_key_id="volumeKmsKeyId"
                            )
                        ),
                        role_arn="roleArn",
                
                        # the properties below are optional
                        baseline_config=sagemaker.CfnMonitoringSchedule.BaselineConfigProperty(
                            constraints_resource=sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty(
                                s3_uri="s3Uri"
                            ),
                            statistics_resource=sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty(
                                s3_uri="s3Uri"
                            )
                        ),
                        environment={
                            "environment_key": "environment"
                        },
                        network_config=sagemaker.CfnMonitoringSchedule.NetworkConfigProperty(
                            enable_inter_container_traffic_encryption=False,
                            enable_network_isolation=False,
                            vpc_config=sagemaker.CfnMonitoringSchedule.VpcConfigProperty(
                                security_group_ids=["securityGroupIds"],
                                subnets=["subnets"]
                            )
                        ),
                        stopping_condition=sagemaker.CfnMonitoringSchedule.StoppingConditionProperty(
                            max_runtime_in_seconds=123
                        )
                    ),
                    monitoring_job_definition_name="monitoringJobDefinitionName",
                    monitoring_type="monitoringType",
                    schedule_config=sagemaker.CfnMonitoringSchedule.ScheduleConfigProperty(
                        schedule_expression="scheduleExpression"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if monitoring_job_definition is not None:
                self._values["monitoring_job_definition"] = monitoring_job_definition
            if monitoring_job_definition_name is not None:
                self._values["monitoring_job_definition_name"] = monitoring_job_definition_name
            if monitoring_type is not None:
                self._values["monitoring_type"] = monitoring_type
            if schedule_config is not None:
                self._values["schedule_config"] = schedule_config

        @builtins.property
        def monitoring_job_definition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringJobDefinitionProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinition
            '''
            result = self._values.get("monitoring_job_definition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringJobDefinitionProperty"]], result)

        @builtins.property
        def monitoring_job_definition_name(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinitionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinitionname
            '''
            result = self._values.get("monitoring_job_definition_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def monitoring_type(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringtype
            '''
            result = self._values.get("monitoring_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schedule_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ScheduleConfigProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.ScheduleConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-scheduleconfig
            '''
            result = self._values.get("schedule_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ScheduleConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringScheduleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnMonitoringSchedule.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnMonitoringSchedule.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnMonitoringSchedule.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                network_config_property = sagemaker.CfnMonitoringSchedule.NetworkConfigProperty(
                    enable_inter_container_traffic_encryption=False,
                    enable_network_isolation=False,
                    vpc_config=sagemaker.CfnMonitoringSchedule.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnMonitoringSchedule.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnMonitoringSchedule.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.VpcConfigProperty"]]:
            '''``CfnMonitoringSchedule.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_upload_mode": "s3UploadMode",
            "s3_uri": "s3Uri",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
            s3_uri: builtins.str,
        ) -> None:
            '''
            :param local_path: ``CfnMonitoringSchedule.S3OutputProperty.LocalPath``.
            :param s3_upload_mode: ``CfnMonitoringSchedule.S3OutputProperty.S3UploadMode``.
            :param s3_uri: ``CfnMonitoringSchedule.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                s3_output_property = sagemaker.CfnMonitoringSchedule.S3OutputProperty(
                    local_path="localPath",
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    s3_upload_mode="s3UploadMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnMonitoringSchedule.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnMonitoringSchedule.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ScheduleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression"},
    )
    class ScheduleConfigProperty:
        def __init__(self, *, schedule_expression: builtins.str) -> None:
            '''
            :param schedule_expression: ``CfnMonitoringSchedule.ScheduleConfigProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                schedule_config_property = sagemaker.CfnMonitoringSchedule.ScheduleConfigProperty(
                    schedule_expression="scheduleExpression"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''``CfnMonitoringSchedule.ScheduleConfigProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html#cfn-sagemaker-monitoringschedule-scheduleconfig-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class StatisticsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnMonitoringSchedule.StatisticsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                statistics_resource_property = sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty(
                    s3_uri="s3Uri"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.StatisticsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html#cfn-sagemaker-monitoringschedule-statisticsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnMonitoringSchedule.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                stopping_condition_property = sagemaker.CfnMonitoringSchedule.StoppingConditionProperty(
                    max_runtime_in_seconds=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnMonitoringSchedule.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html#cfn-sagemaker-monitoringschedule-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnMonitoringSchedule.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnMonitoringSchedule.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                vpc_config_property = sagemaker.CfnMonitoringSchedule.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnMonitoringSchedule.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html#cfn-sagemaker-monitoringschedule-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnMonitoringSchedule.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html#cfn-sagemaker-monitoringschedule-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_name": "endpointName",
        "failure_reason": "failureReason",
        "last_monitoring_execution_summary": "lastMonitoringExecutionSummary",
        "monitoring_schedule_config": "monitoringScheduleConfig",
        "monitoring_schedule_name": "monitoringScheduleName",
        "monitoring_schedule_status": "monitoringScheduleStatus",
        "tags": "tags",
    },
)
class CfnMonitoringScheduleProps:
    def __init__(
        self,
        *,
        endpoint_name: typing.Optional[builtins.str] = None,
        failure_reason: typing.Optional[builtins.str] = None,
        last_monitoring_execution_summary: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringExecutionSummaryProperty]] = None,
        monitoring_schedule_config: typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringScheduleConfigProperty],
        monitoring_schedule_name: builtins.str,
        monitoring_schedule_status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::MonitoringSchedule``.

        :param endpoint_name: ``AWS::SageMaker::MonitoringSchedule.EndpointName``.
        :param failure_reason: ``AWS::SageMaker::MonitoringSchedule.FailureReason``.
        :param last_monitoring_execution_summary: ``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.
        :param monitoring_schedule_config: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.
        :param monitoring_schedule_name: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.
        :param monitoring_schedule_status: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.
        :param tags: ``AWS::SageMaker::MonitoringSchedule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_monitoring_schedule_props = sagemaker.CfnMonitoringScheduleProps(
                monitoring_schedule_config=sagemaker.CfnMonitoringSchedule.MonitoringScheduleConfigProperty(
                    monitoring_job_definition=sagemaker.CfnMonitoringSchedule.MonitoringJobDefinitionProperty(
                        monitoring_app_specification=sagemaker.CfnMonitoringSchedule.MonitoringAppSpecificationProperty(
                            image_uri="imageUri",
            
                            # the properties below are optional
                            container_arguments=["containerArguments"],
                            container_entrypoint=["containerEntrypoint"],
                            post_analytics_processor_source_uri="postAnalyticsProcessorSourceUri",
                            record_preprocessor_source_uri="recordPreprocessorSourceUri"
                        ),
                        monitoring_inputs=[sagemaker.CfnMonitoringSchedule.MonitoringInputProperty(
                            endpoint_input=sagemaker.CfnMonitoringSchedule.EndpointInputProperty(
                                endpoint_name="endpointName",
                                local_path="localPath",
            
                                # the properties below are optional
                                s3_data_distribution_type="s3DataDistributionType",
                                s3_input_mode="s3InputMode"
                            )
                        )],
                        monitoring_output_config=sagemaker.CfnMonitoringSchedule.MonitoringOutputConfigProperty(
                            monitoring_outputs=[sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty(
                                s3_output=sagemaker.CfnMonitoringSchedule.S3OutputProperty(
                                    local_path="localPath",
                                    s3_uri="s3Uri",
            
                                    # the properties below are optional
                                    s3_upload_mode="s3UploadMode"
                                )
                            )],
            
                            # the properties below are optional
                            kms_key_id="kmsKeyId"
                        ),
                        monitoring_resources=sagemaker.CfnMonitoringSchedule.MonitoringResourcesProperty(
                            cluster_config=sagemaker.CfnMonitoringSchedule.ClusterConfigProperty(
                                instance_count=123,
                                instance_type="instanceType",
                                volume_size_in_gb=123,
            
                                # the properties below are optional
                                volume_kms_key_id="volumeKmsKeyId"
                            )
                        ),
                        role_arn="roleArn",
            
                        # the properties below are optional
                        baseline_config=sagemaker.CfnMonitoringSchedule.BaselineConfigProperty(
                            constraints_resource=sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty(
                                s3_uri="s3Uri"
                            ),
                            statistics_resource=sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty(
                                s3_uri="s3Uri"
                            )
                        ),
                        environment={
                            "environment_key": "environment"
                        },
                        network_config=sagemaker.CfnMonitoringSchedule.NetworkConfigProperty(
                            enable_inter_container_traffic_encryption=False,
                            enable_network_isolation=False,
                            vpc_config=sagemaker.CfnMonitoringSchedule.VpcConfigProperty(
                                security_group_ids=["securityGroupIds"],
                                subnets=["subnets"]
                            )
                        ),
                        stopping_condition=sagemaker.CfnMonitoringSchedule.StoppingConditionProperty(
                            max_runtime_in_seconds=123
                        )
                    ),
                    monitoring_job_definition_name="monitoringJobDefinitionName",
                    monitoring_type="monitoringType",
                    schedule_config=sagemaker.CfnMonitoringSchedule.ScheduleConfigProperty(
                        schedule_expression="scheduleExpression"
                    )
                ),
                monitoring_schedule_name="monitoringScheduleName",
            
                # the properties below are optional
                endpoint_name="endpointName",
                failure_reason="failureReason",
                last_monitoring_execution_summary=sagemaker.CfnMonitoringSchedule.MonitoringExecutionSummaryProperty(
                    creation_time="creationTime",
                    last_modified_time="lastModifiedTime",
                    monitoring_execution_status="monitoringExecutionStatus",
                    monitoring_schedule_name="monitoringScheduleName",
                    scheduled_time="scheduledTime",
            
                    # the properties below are optional
                    endpoint_name="endpointName",
                    failure_reason="failureReason",
                    processing_job_arn="processingJobArn"
                ),
                monitoring_schedule_status="monitoringScheduleStatus",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "monitoring_schedule_config": monitoring_schedule_config,
            "monitoring_schedule_name": monitoring_schedule_name,
        }
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if failure_reason is not None:
            self._values["failure_reason"] = failure_reason
        if last_monitoring_execution_summary is not None:
            self._values["last_monitoring_execution_summary"] = last_monitoring_execution_summary
        if monitoring_schedule_status is not None:
            self._values["monitoring_schedule_status"] = monitoring_schedule_status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.EndpointName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-endpointname
        '''
        result = self._values.get("endpoint_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failure_reason(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.FailureReason``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-failurereason
        '''
        result = self._values.get("failure_reason")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_monitoring_execution_summary(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringExecutionSummaryProperty]]:
        '''``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-lastmonitoringexecutionsummary
        '''
        result = self._values.get("last_monitoring_execution_summary")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringExecutionSummaryProperty]], result)

    @builtins.property
    def monitoring_schedule_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringScheduleConfigProperty]:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig
        '''
        result = self._values.get("monitoring_schedule_config")
        assert result is not None, "Required property 'monitoring_schedule_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringScheduleConfigProperty], result)

    @builtins.property
    def monitoring_schedule_name(self) -> builtins.str:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulename
        '''
        result = self._values.get("monitoring_schedule_name")
        assert result is not None, "Required property 'monitoring_schedule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monitoring_schedule_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulestatus
        '''
        result = self._values.get("monitoring_schedule_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::MonitoringSchedule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMonitoringScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNotebookInstance(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstance",
):
    '''A CloudFormation ``AWS::SageMaker::NotebookInstance``.

    :cloudformationResource: AWS::SageMaker::NotebookInstance
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_notebook_instance = sagemaker.CfnNotebookInstance(self, "MyCfnNotebookInstance",
            instance_type="instanceType",
            role_arn="roleArn",
        
            # the properties below are optional
            accelerator_types=["acceleratorTypes"],
            additional_code_repositories=["additionalCodeRepositories"],
            default_code_repository="defaultCodeRepository",
            direct_internet_access="directInternetAccess",
            kms_key_id="kmsKeyId",
            lifecycle_config_name="lifecycleConfigName",
            notebook_instance_name="notebookInstanceName",
            platform_identifier="platformIdentifier",
            root_access="rootAccess",
            security_group_ids=["securityGroupIds"],
            subnet_id="subnetId",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            volume_size_in_gb=123
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_code_repositories: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_code_repository: typing.Optional[builtins.str] = None,
        direct_internet_access: typing.Optional[builtins.str] = None,
        instance_type: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        lifecycle_config_name: typing.Optional[builtins.str] = None,
        notebook_instance_name: typing.Optional[builtins.str] = None,
        platform_identifier: typing.Optional[builtins.str] = None,
        role_arn: builtins.str,
        root_access: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        volume_size_in_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::NotebookInstance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param accelerator_types: ``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.
        :param additional_code_repositories: ``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.
        :param default_code_repository: ``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.
        :param direct_internet_access: ``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.
        :param instance_type: ``AWS::SageMaker::NotebookInstance.InstanceType``.
        :param kms_key_id: ``AWS::SageMaker::NotebookInstance.KmsKeyId``.
        :param lifecycle_config_name: ``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.
        :param notebook_instance_name: ``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.
        :param platform_identifier: ``AWS::SageMaker::NotebookInstance.PlatformIdentifier``.
        :param role_arn: ``AWS::SageMaker::NotebookInstance.RoleArn``.
        :param root_access: ``AWS::SageMaker::NotebookInstance.RootAccess``.
        :param security_group_ids: ``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.
        :param subnet_id: ``AWS::SageMaker::NotebookInstance.SubnetId``.
        :param tags: ``AWS::SageMaker::NotebookInstance.Tags``.
        :param volume_size_in_gb: ``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.
        '''
        props = CfnNotebookInstanceProps(
            accelerator_types=accelerator_types,
            additional_code_repositories=additional_code_repositories,
            default_code_repository=default_code_repository,
            direct_internet_access=direct_internet_access,
            instance_type=instance_type,
            kms_key_id=kms_key_id,
            lifecycle_config_name=lifecycle_config_name,
            notebook_instance_name=notebook_instance_name,
            platform_identifier=platform_identifier,
            role_arn=role_arn,
            root_access=root_access,
            security_group_ids=security_group_ids,
            subnet_id=subnet_id,
            tags=tags,
            volume_size_in_gb=volume_size_in_gb,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorTypes")
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-acceleratortypes
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorTypes"))

    @accelerator_types.setter
    def accelerator_types(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "acceleratorTypes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="additionalCodeRepositories")
    def additional_code_repositories(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-additionalcoderepositories
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalCodeRepositories"))

    @additional_code_repositories.setter
    def additional_code_repositories(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "additionalCodeRepositories", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNotebookInstanceName")
    def attr_notebook_instance_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: NotebookInstanceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNotebookInstanceName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultCodeRepository")
    def default_code_repository(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-defaultcoderepository
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultCodeRepository"))

    @default_code_repository.setter
    def default_code_repository(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultCodeRepository", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="directInternetAccess")
    def direct_internet_access(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-directinternetaccess
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directInternetAccess"))

    @direct_internet_access.setter
    def direct_internet_access(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "directInternetAccess", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''``AWS::SageMaker::NotebookInstance.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-instancetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        jsii.set(self, "instanceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycleConfigName")
    def lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-lifecycleconfigname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigName"))

    @lifecycle_config_name.setter
    def lifecycle_config_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "lifecycleConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notebookInstanceName")
    def notebook_instance_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-notebookinstancename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookInstanceName"))

    @notebook_instance_name.setter
    def notebook_instance_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "notebookInstanceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="platformIdentifier")
    def platform_identifier(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.PlatformIdentifier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-platformidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformIdentifier"))

    @platform_identifier.setter
    def platform_identifier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "platformIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::NotebookInstance.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rootAccess")
    def root_access(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.RootAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rootaccess
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootAccess"))

    @root_access.setter
    def root_access(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "rootAccess", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-securitygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-subnetid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subnetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::NotebookInstance.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeSizeInGb")
    def volume_size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-volumesizeingb
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInGb"))

    @volume_size_in_gb.setter
    def volume_size_in_gb(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "volumeSizeInGb", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNotebookInstanceLifecycleConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfig",
):
    '''A CloudFormation ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

    :cloudformationResource: AWS::SageMaker::NotebookInstanceLifecycleConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_notebook_instance_lifecycle_config = sagemaker.CfnNotebookInstanceLifecycleConfig(self, "MyCfnNotebookInstanceLifecycleConfig",
            notebook_instance_lifecycle_config_name="notebookInstanceLifecycleConfigName",
            on_create=[sagemaker.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty(
                content="content"
            )],
            on_start=[sagemaker.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty(
                content="content"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        notebook_instance_lifecycle_config_name: typing.Optional[builtins.str] = None,
        on_create: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]] = None,
        on_start: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param notebook_instance_lifecycle_config_name: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.
        :param on_create: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.
        :param on_start: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.
        '''
        props = CfnNotebookInstanceLifecycleConfigProps(
            notebook_instance_lifecycle_config_name=notebook_instance_lifecycle_config_name,
            on_create=on_create,
            on_start=on_start,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNotebookInstanceLifecycleConfigName")
    def attr_notebook_instance_lifecycle_config_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: NotebookInstanceLifecycleConfigName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNotebookInstanceLifecycleConfigName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notebookInstanceLifecycleConfigName")
    def notebook_instance_lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecycleconfigname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookInstanceLifecycleConfigName"))

    @notebook_instance_lifecycle_config_name.setter
    def notebook_instance_lifecycle_config_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "notebookInstanceLifecycleConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onCreate")
    def on_create(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-oncreate
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]], jsii.get(self, "onCreate"))

    @on_create.setter
    def on_create(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]],
    ) -> None:
        jsii.set(self, "onCreate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onStart")
    def on_start(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-onstart
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]], jsii.get(self, "onStart"))

    @on_start.setter
    def on_start(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]],
    ) -> None:
        jsii.set(self, "onStart", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content"},
    )
    class NotebookInstanceLifecycleHookProperty:
        def __init__(self, *, content: typing.Optional[builtins.str] = None) -> None:
            '''
            :param content: ``CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty.Content``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                notebook_instance_lifecycle_hook_property = sagemaker.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty(
                    content="content"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''``CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty.Content``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotebookInstanceLifecycleHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "notebook_instance_lifecycle_config_name": "notebookInstanceLifecycleConfigName",
        "on_create": "onCreate",
        "on_start": "onStart",
    },
)
class CfnNotebookInstanceLifecycleConfigProps:
    def __init__(
        self,
        *,
        notebook_instance_lifecycle_config_name: typing.Optional[builtins.str] = None,
        on_create: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]] = None,
        on_start: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

        :param notebook_instance_lifecycle_config_name: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.
        :param on_create: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.
        :param on_start: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_notebook_instance_lifecycle_config_props = sagemaker.CfnNotebookInstanceLifecycleConfigProps(
                notebook_instance_lifecycle_config_name="notebookInstanceLifecycleConfigName",
                on_create=[sagemaker.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty(
                    content="content"
                )],
                on_start=[sagemaker.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty(
                    content="content"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if notebook_instance_lifecycle_config_name is not None:
            self._values["notebook_instance_lifecycle_config_name"] = notebook_instance_lifecycle_config_name
        if on_create is not None:
            self._values["on_create"] = on_create
        if on_start is not None:
            self._values["on_start"] = on_start

    @builtins.property
    def notebook_instance_lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecycleconfigname
        '''
        result = self._values.get("notebook_instance_lifecycle_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_create(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-oncreate
        '''
        result = self._values.get("on_create")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]], result)

    @builtins.property
    def on_start(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-onstart
        '''
        result = self._values.get("on_start")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotebookInstanceLifecycleConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_types": "acceleratorTypes",
        "additional_code_repositories": "additionalCodeRepositories",
        "default_code_repository": "defaultCodeRepository",
        "direct_internet_access": "directInternetAccess",
        "instance_type": "instanceType",
        "kms_key_id": "kmsKeyId",
        "lifecycle_config_name": "lifecycleConfigName",
        "notebook_instance_name": "notebookInstanceName",
        "platform_identifier": "platformIdentifier",
        "role_arn": "roleArn",
        "root_access": "rootAccess",
        "security_group_ids": "securityGroupIds",
        "subnet_id": "subnetId",
        "tags": "tags",
        "volume_size_in_gb": "volumeSizeInGb",
    },
)
class CfnNotebookInstanceProps:
    def __init__(
        self,
        *,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_code_repositories: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_code_repository: typing.Optional[builtins.str] = None,
        direct_internet_access: typing.Optional[builtins.str] = None,
        instance_type: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        lifecycle_config_name: typing.Optional[builtins.str] = None,
        notebook_instance_name: typing.Optional[builtins.str] = None,
        platform_identifier: typing.Optional[builtins.str] = None,
        role_arn: builtins.str,
        root_access: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        volume_size_in_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::NotebookInstance``.

        :param accelerator_types: ``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.
        :param additional_code_repositories: ``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.
        :param default_code_repository: ``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.
        :param direct_internet_access: ``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.
        :param instance_type: ``AWS::SageMaker::NotebookInstance.InstanceType``.
        :param kms_key_id: ``AWS::SageMaker::NotebookInstance.KmsKeyId``.
        :param lifecycle_config_name: ``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.
        :param notebook_instance_name: ``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.
        :param platform_identifier: ``AWS::SageMaker::NotebookInstance.PlatformIdentifier``.
        :param role_arn: ``AWS::SageMaker::NotebookInstance.RoleArn``.
        :param root_access: ``AWS::SageMaker::NotebookInstance.RootAccess``.
        :param security_group_ids: ``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.
        :param subnet_id: ``AWS::SageMaker::NotebookInstance.SubnetId``.
        :param tags: ``AWS::SageMaker::NotebookInstance.Tags``.
        :param volume_size_in_gb: ``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_notebook_instance_props = sagemaker.CfnNotebookInstanceProps(
                instance_type="instanceType",
                role_arn="roleArn",
            
                # the properties below are optional
                accelerator_types=["acceleratorTypes"],
                additional_code_repositories=["additionalCodeRepositories"],
                default_code_repository="defaultCodeRepository",
                direct_internet_access="directInternetAccess",
                kms_key_id="kmsKeyId",
                lifecycle_config_name="lifecycleConfigName",
                notebook_instance_name="notebookInstanceName",
                platform_identifier="platformIdentifier",
                root_access="rootAccess",
                security_group_ids=["securityGroupIds"],
                subnet_id="subnetId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                volume_size_in_gb=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
            "role_arn": role_arn,
        }
        if accelerator_types is not None:
            self._values["accelerator_types"] = accelerator_types
        if additional_code_repositories is not None:
            self._values["additional_code_repositories"] = additional_code_repositories
        if default_code_repository is not None:
            self._values["default_code_repository"] = default_code_repository
        if direct_internet_access is not None:
            self._values["direct_internet_access"] = direct_internet_access
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if lifecycle_config_name is not None:
            self._values["lifecycle_config_name"] = lifecycle_config_name
        if notebook_instance_name is not None:
            self._values["notebook_instance_name"] = notebook_instance_name
        if platform_identifier is not None:
            self._values["platform_identifier"] = platform_identifier
        if root_access is not None:
            self._values["root_access"] = root_access
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if volume_size_in_gb is not None:
            self._values["volume_size_in_gb"] = volume_size_in_gb

    @builtins.property
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-acceleratortypes
        '''
        result = self._values.get("accelerator_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def additional_code_repositories(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-additionalcoderepositories
        '''
        result = self._values.get("additional_code_repositories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_code_repository(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-defaultcoderepository
        '''
        result = self._values.get("default_code_repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_internet_access(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-directinternetaccess
        '''
        result = self._values.get("direct_internet_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''``AWS::SageMaker::NotebookInstance.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-lifecycleconfigname
        '''
        result = self._values.get("lifecycle_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notebook_instance_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-notebookinstancename
        '''
        result = self._values.get("notebook_instance_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform_identifier(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.PlatformIdentifier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-platformidentifier
        '''
        result = self._values.get("platform_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::NotebookInstance.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_access(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.RootAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rootaccess
        '''
        result = self._values.get("root_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::NotebookInstance.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def volume_size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-volumesizeingb
        '''
        result = self._values.get("volume_size_in_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotebookInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPipeline(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnPipeline",
):
    '''A CloudFormation ``AWS::SageMaker::Pipeline``.

    :cloudformationResource: AWS::SageMaker::Pipeline
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        # pipeline_definition is of type object
        
        cfn_pipeline = sagemaker.CfnPipeline(self, "MyCfnPipeline",
            pipeline_definition=pipeline_definition,
            pipeline_name="pipelineName",
            role_arn="roleArn",
        
            # the properties below are optional
            pipeline_description="pipelineDescription",
            pipeline_display_name="pipelineDisplayName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        pipeline_definition: typing.Any,
        pipeline_description: typing.Optional[builtins.str] = None,
        pipeline_display_name: typing.Optional[builtins.str] = None,
        pipeline_name: builtins.str,
        role_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Pipeline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param pipeline_definition: ``AWS::SageMaker::Pipeline.PipelineDefinition``.
        :param pipeline_description: ``AWS::SageMaker::Pipeline.PipelineDescription``.
        :param pipeline_display_name: ``AWS::SageMaker::Pipeline.PipelineDisplayName``.
        :param pipeline_name: ``AWS::SageMaker::Pipeline.PipelineName``.
        :param role_arn: ``AWS::SageMaker::Pipeline.RoleArn``.
        :param tags: ``AWS::SageMaker::Pipeline.Tags``.
        '''
        props = CfnPipelineProps(
            pipeline_definition=pipeline_definition,
            pipeline_description=pipeline_description,
            pipeline_display_name=pipeline_display_name,
            pipeline_name=pipeline_name,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineDefinition")
    def pipeline_definition(self) -> typing.Any:
        '''``AWS::SageMaker::Pipeline.PipelineDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedefinition
        '''
        return typing.cast(typing.Any, jsii.get(self, "pipelineDefinition"))

    @pipeline_definition.setter
    def pipeline_definition(self, value: typing.Any) -> None:
        jsii.set(self, "pipelineDefinition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineDescription")
    def pipeline_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Pipeline.PipelineDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineDescription"))

    @pipeline_description.setter
    def pipeline_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pipelineDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineDisplayName")
    def pipeline_display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Pipeline.PipelineDisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedisplayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineDisplayName"))

    @pipeline_display_name.setter
    def pipeline_display_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pipelineDisplayName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineName")
    def pipeline_name(self) -> builtins.str:
        '''``AWS::SageMaker::Pipeline.PipelineName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinename
        '''
        return typing.cast(builtins.str, jsii.get(self, "pipelineName"))

    @pipeline_name.setter
    def pipeline_name(self, value: builtins.str) -> None:
        jsii.set(self, "pipelineName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Pipeline.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnPipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "pipeline_definition": "pipelineDefinition",
        "pipeline_description": "pipelineDescription",
        "pipeline_display_name": "pipelineDisplayName",
        "pipeline_name": "pipelineName",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnPipelineProps:
    def __init__(
        self,
        *,
        pipeline_definition: typing.Any,
        pipeline_description: typing.Optional[builtins.str] = None,
        pipeline_display_name: typing.Optional[builtins.str] = None,
        pipeline_name: builtins.str,
        role_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Pipeline``.

        :param pipeline_definition: ``AWS::SageMaker::Pipeline.PipelineDefinition``.
        :param pipeline_description: ``AWS::SageMaker::Pipeline.PipelineDescription``.
        :param pipeline_display_name: ``AWS::SageMaker::Pipeline.PipelineDisplayName``.
        :param pipeline_name: ``AWS::SageMaker::Pipeline.PipelineName``.
        :param role_arn: ``AWS::SageMaker::Pipeline.RoleArn``.
        :param tags: ``AWS::SageMaker::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            # pipeline_definition is of type object
            
            cfn_pipeline_props = sagemaker.CfnPipelineProps(
                pipeline_definition=pipeline_definition,
                pipeline_name="pipelineName",
                role_arn="roleArn",
            
                # the properties below are optional
                pipeline_description="pipelineDescription",
                pipeline_display_name="pipelineDisplayName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "pipeline_definition": pipeline_definition,
            "pipeline_name": pipeline_name,
            "role_arn": role_arn,
        }
        if pipeline_description is not None:
            self._values["pipeline_description"] = pipeline_description
        if pipeline_display_name is not None:
            self._values["pipeline_display_name"] = pipeline_display_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pipeline_definition(self) -> typing.Any:
        '''``AWS::SageMaker::Pipeline.PipelineDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedefinition
        '''
        result = self._values.get("pipeline_definition")
        assert result is not None, "Required property 'pipeline_definition' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def pipeline_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Pipeline.PipelineDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedescription
        '''
        result = self._values.get("pipeline_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipeline_display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Pipeline.PipelineDisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedisplayname
        '''
        result = self._values.get("pipeline_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        '''``AWS::SageMaker::Pipeline.PipelineName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinename
        '''
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Pipeline.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnProject(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnProject",
):
    '''A CloudFormation ``AWS::SageMaker::Project``.

    :cloudformationResource: AWS::SageMaker::Project
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        # service_catalog_provisioning_details is of type object
        
        cfn_project = sagemaker.CfnProject(self, "MyCfnProject",
            project_name="projectName",
            service_catalog_provisioning_details=service_catalog_provisioning_details,
        
            # the properties below are optional
            project_description="projectDescription",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        project_description: typing.Optional[builtins.str] = None,
        project_name: builtins.str,
        service_catalog_provisioning_details: typing.Any,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param project_description: ``AWS::SageMaker::Project.ProjectDescription``.
        :param project_name: ``AWS::SageMaker::Project.ProjectName``.
        :param service_catalog_provisioning_details: ``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.
        :param tags: ``AWS::SageMaker::Project.Tags``.
        '''
        props = CfnProjectProps(
            project_description=project_description,
            project_name=project_name,
            service_catalog_provisioning_details=service_catalog_provisioning_details,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProjectArn")
    def attr_project_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProjectStatus")
    def attr_project_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectStatus"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectDescription")
    def project_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Project.ProjectDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectDescription"))

    @project_description.setter
    def project_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "projectDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        '''``AWS::SageMaker::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectname
        '''
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        jsii.set(self, "projectName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceCatalogProvisioningDetails")
    def service_catalog_provisioning_details(self) -> typing.Any:
        '''``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-servicecatalogprovisioningdetails
        '''
        return typing.cast(typing.Any, jsii.get(self, "serviceCatalogProvisioningDetails"))

    @service_catalog_provisioning_details.setter
    def service_catalog_provisioning_details(self, value: typing.Any) -> None:
        jsii.set(self, "serviceCatalogProvisioningDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "project_description": "projectDescription",
        "project_name": "projectName",
        "service_catalog_provisioning_details": "serviceCatalogProvisioningDetails",
        "tags": "tags",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        project_description: typing.Optional[builtins.str] = None,
        project_name: builtins.str,
        service_catalog_provisioning_details: typing.Any,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Project``.

        :param project_description: ``AWS::SageMaker::Project.ProjectDescription``.
        :param project_name: ``AWS::SageMaker::Project.ProjectName``.
        :param service_catalog_provisioning_details: ``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.
        :param tags: ``AWS::SageMaker::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            # service_catalog_provisioning_details is of type object
            
            cfn_project_props = sagemaker.CfnProjectProps(
                project_name="projectName",
                service_catalog_provisioning_details=service_catalog_provisioning_details,
            
                # the properties below are optional
                project_description="projectDescription",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "project_name": project_name,
            "service_catalog_provisioning_details": service_catalog_provisioning_details,
        }
        if project_description is not None:
            self._values["project_description"] = project_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def project_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Project.ProjectDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectdescription
        '''
        result = self._values.get("project_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_name(self) -> builtins.str:
        '''``AWS::SageMaker::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectname
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_catalog_provisioning_details(self) -> typing.Any:
        '''``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-servicecatalogprovisioningdetails
        '''
        result = self._values.get("service_catalog_provisioning_details")
        assert result is not None, "Required property 'service_catalog_provisioning_details' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnUserProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile",
):
    '''A CloudFormation ``AWS::SageMaker::UserProfile``.

    :cloudformationResource: AWS::SageMaker::UserProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_user_profile = sagemaker.CfnUserProfile(self, "MyCfnUserProfile",
            domain_id="domainId",
            user_profile_name="userProfileName",
        
            # the properties below are optional
            single_sign_on_user_identifier="singleSignOnUserIdentifier",
            single_sign_on_user_value="singleSignOnUserValue",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_settings=sagemaker.CfnUserProfile.UserSettingsProperty(
                execution_role="executionRole",
                jupyter_server_app_settings=sagemaker.CfnUserProfile.JupyterServerAppSettingsProperty(
                    default_resource_spec=sagemaker.CfnUserProfile.ResourceSpecProperty(
                        instance_type="instanceType",
                        sage_maker_image_arn="sageMakerImageArn",
                        sage_maker_image_version_arn="sageMakerImageVersionArn"
                    )
                ),
                kernel_gateway_app_settings=sagemaker.CfnUserProfile.KernelGatewayAppSettingsProperty(
                    custom_images=[sagemaker.CfnUserProfile.CustomImageProperty(
                        app_image_config_name="appImageConfigName",
                        image_name="imageName",
        
                        # the properties below are optional
                        image_version_number=123
                    )],
                    default_resource_spec=sagemaker.CfnUserProfile.ResourceSpecProperty(
                        instance_type="instanceType",
                        sage_maker_image_arn="sageMakerImageArn",
                        sage_maker_image_version_arn="sageMakerImageVersionArn"
                    )
                ),
                security_groups=["securityGroups"],
                sharing_settings=sagemaker.CfnUserProfile.SharingSettingsProperty(
                    notebook_output_option="notebookOutputOption",
                    s3_kms_key_id="s3KmsKeyId",
                    s3_output_path="s3OutputPath"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        domain_id: builtins.str,
        single_sign_on_user_identifier: typing.Optional[builtins.str] = None,
        single_sign_on_user_value: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_profile_name: builtins.str,
        user_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.UserSettingsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::UserProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_id: ``AWS::SageMaker::UserProfile.DomainId``.
        :param single_sign_on_user_identifier: ``AWS::SageMaker::UserProfile.SingleSignOnUserIdentifier``.
        :param single_sign_on_user_value: ``AWS::SageMaker::UserProfile.SingleSignOnUserValue``.
        :param tags: ``AWS::SageMaker::UserProfile.Tags``.
        :param user_profile_name: ``AWS::SageMaker::UserProfile.UserProfileName``.
        :param user_settings: ``AWS::SageMaker::UserProfile.UserSettings``.
        '''
        props = CfnUserProfileProps(
            domain_id=domain_id,
            single_sign_on_user_identifier=single_sign_on_user_identifier,
            single_sign_on_user_value=single_sign_on_user_value,
            tags=tags,
            user_profile_name=user_profile_name,
            user_settings=user_settings,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserProfileArn")
    def attr_user_profile_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: UserProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserProfileArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        '''``AWS::SageMaker::UserProfile.DomainId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-domainid
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: builtins.str) -> None:
        jsii.set(self, "domainId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="singleSignOnUserIdentifier")
    def single_sign_on_user_identifier(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::UserProfile.SingleSignOnUserIdentifier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuseridentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleSignOnUserIdentifier"))

    @single_sign_on_user_identifier.setter
    def single_sign_on_user_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "singleSignOnUserIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="singleSignOnUserValue")
    def single_sign_on_user_value(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::UserProfile.SingleSignOnUserValue``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuservalue
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleSignOnUserValue"))

    @single_sign_on_user_value.setter
    def single_sign_on_user_value(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "singleSignOnUserValue", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::UserProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userProfileName")
    def user_profile_name(self) -> builtins.str:
        '''``AWS::SageMaker::UserProfile.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-userprofilename
        '''
        return typing.cast(builtins.str, jsii.get(self, "userProfileName"))

    @user_profile_name.setter
    def user_profile_name(self, value: builtins.str) -> None:
        jsii.set(self, "userProfileName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userSettings")
    def user_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.UserSettingsProperty"]]:
        '''``AWS::SageMaker::UserProfile.UserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-usersettings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.UserSettingsProperty"]], jsii.get(self, "userSettings"))

    @user_settings.setter
    def user_settings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.UserSettingsProperty"]],
    ) -> None:
        jsii.set(self, "userSettings", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.CustomImageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_image_config_name": "appImageConfigName",
            "image_name": "imageName",
            "image_version_number": "imageVersionNumber",
        },
    )
    class CustomImageProperty:
        def __init__(
            self,
            *,
            app_image_config_name: builtins.str,
            image_name: builtins.str,
            image_version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param app_image_config_name: ``CfnUserProfile.CustomImageProperty.AppImageConfigName``.
            :param image_name: ``CfnUserProfile.CustomImageProperty.ImageName``.
            :param image_version_number: ``CfnUserProfile.CustomImageProperty.ImageVersionNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                custom_image_property = sagemaker.CfnUserProfile.CustomImageProperty(
                    app_image_config_name="appImageConfigName",
                    image_name="imageName",
                
                    # the properties below are optional
                    image_version_number=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_image_config_name": app_image_config_name,
                "image_name": image_name,
            }
            if image_version_number is not None:
                self._values["image_version_number"] = image_version_number

        @builtins.property
        def app_image_config_name(self) -> builtins.str:
            '''``CfnUserProfile.CustomImageProperty.AppImageConfigName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-appimageconfigname
            '''
            result = self._values.get("app_image_config_name")
            assert result is not None, "Required property 'app_image_config_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_name(self) -> builtins.str:
            '''``CfnUserProfile.CustomImageProperty.ImageName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-imagename
            '''
            result = self._values.get("image_name")
            assert result is not None, "Required property 'image_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_version_number(self) -> typing.Optional[jsii.Number]:
            '''``CfnUserProfile.CustomImageProperty.ImageVersionNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-imageversionnumber
            '''
            result = self._values.get("image_version_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomImageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.JupyterServerAppSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"default_resource_spec": "defaultResourceSpec"},
    )
    class JupyterServerAppSettingsProperty:
        def __init__(
            self,
            *,
            default_resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]] = None,
        ) -> None:
            '''
            :param default_resource_spec: ``CfnUserProfile.JupyterServerAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-jupyterserverappsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                jupyter_server_app_settings_property = sagemaker.CfnUserProfile.JupyterServerAppSettingsProperty(
                    default_resource_spec=sagemaker.CfnUserProfile.ResourceSpecProperty(
                        instance_type="instanceType",
                        sage_maker_image_arn="sageMakerImageArn",
                        sage_maker_image_version_arn="sageMakerImageVersionArn"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_resource_spec is not None:
                self._values["default_resource_spec"] = default_resource_spec

        @builtins.property
        def default_resource_spec(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]]:
            '''``CfnUserProfile.JupyterServerAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-jupyterserverappsettings.html#cfn-sagemaker-userprofile-jupyterserverappsettings-defaultresourcespec
            '''
            result = self._values.get("default_resource_spec")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JupyterServerAppSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.KernelGatewayAppSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_images": "customImages",
            "default_resource_spec": "defaultResourceSpec",
        },
    )
    class KernelGatewayAppSettingsProperty:
        def __init__(
            self,
            *,
            custom_images: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.CustomImageProperty"]]]] = None,
            default_resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]] = None,
        ) -> None:
            '''
            :param custom_images: ``CfnUserProfile.KernelGatewayAppSettingsProperty.CustomImages``.
            :param default_resource_spec: ``CfnUserProfile.KernelGatewayAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                kernel_gateway_app_settings_property = sagemaker.CfnUserProfile.KernelGatewayAppSettingsProperty(
                    custom_images=[sagemaker.CfnUserProfile.CustomImageProperty(
                        app_image_config_name="appImageConfigName",
                        image_name="imageName",
                
                        # the properties below are optional
                        image_version_number=123
                    )],
                    default_resource_spec=sagemaker.CfnUserProfile.ResourceSpecProperty(
                        instance_type="instanceType",
                        sage_maker_image_arn="sageMakerImageArn",
                        sage_maker_image_version_arn="sageMakerImageVersionArn"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_images is not None:
                self._values["custom_images"] = custom_images
            if default_resource_spec is not None:
                self._values["default_resource_spec"] = default_resource_spec

        @builtins.property
        def custom_images(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.CustomImageProperty"]]]]:
            '''``CfnUserProfile.KernelGatewayAppSettingsProperty.CustomImages``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html#cfn-sagemaker-userprofile-kernelgatewayappsettings-customimages
            '''
            result = self._values.get("custom_images")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.CustomImageProperty"]]]], result)

        @builtins.property
        def default_resource_spec(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]]:
            '''``CfnUserProfile.KernelGatewayAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html#cfn-sagemaker-userprofile-kernelgatewayappsettings-defaultresourcespec
            '''
            result = self._values.get("default_resource_spec")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KernelGatewayAppSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.ResourceSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "sage_maker_image_arn": "sageMakerImageArn",
            "sage_maker_image_version_arn": "sageMakerImageVersionArn",
        },
    )
    class ResourceSpecProperty:
        def __init__(
            self,
            *,
            instance_type: typing.Optional[builtins.str] = None,
            sage_maker_image_arn: typing.Optional[builtins.str] = None,
            sage_maker_image_version_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_type: ``CfnUserProfile.ResourceSpecProperty.InstanceType``.
            :param sage_maker_image_arn: ``CfnUserProfile.ResourceSpecProperty.SageMakerImageArn``.
            :param sage_maker_image_version_arn: ``CfnUserProfile.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                resource_spec_property = sagemaker.CfnUserProfile.ResourceSpecProperty(
                    instance_type="instanceType",
                    sage_maker_image_arn="sageMakerImageArn",
                    sage_maker_image_version_arn="sageMakerImageVersionArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if sage_maker_image_arn is not None:
                self._values["sage_maker_image_arn"] = sage_maker_image_arn
            if sage_maker_image_version_arn is not None:
                self._values["sage_maker_image_version_arn"] = sage_maker_image_version_arn

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.ResourceSpecProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.ResourceSpecProperty.SageMakerImageArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-sagemakerimagearn
            '''
            result = self._values.get("sage_maker_image_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_version_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-sagemakerimageversionarn
            '''
            result = self._values.get("sage_maker_image_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.SharingSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "notebook_output_option": "notebookOutputOption",
            "s3_kms_key_id": "s3KmsKeyId",
            "s3_output_path": "s3OutputPath",
        },
    )
    class SharingSettingsProperty:
        def __init__(
            self,
            *,
            notebook_output_option: typing.Optional[builtins.str] = None,
            s3_kms_key_id: typing.Optional[builtins.str] = None,
            s3_output_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param notebook_output_option: ``CfnUserProfile.SharingSettingsProperty.NotebookOutputOption``.
            :param s3_kms_key_id: ``CfnUserProfile.SharingSettingsProperty.S3KmsKeyId``.
            :param s3_output_path: ``CfnUserProfile.SharingSettingsProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                sharing_settings_property = sagemaker.CfnUserProfile.SharingSettingsProperty(
                    notebook_output_option="notebookOutputOption",
                    s3_kms_key_id="s3KmsKeyId",
                    s3_output_path="s3OutputPath"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if notebook_output_option is not None:
                self._values["notebook_output_option"] = notebook_output_option
            if s3_kms_key_id is not None:
                self._values["s3_kms_key_id"] = s3_kms_key_id
            if s3_output_path is not None:
                self._values["s3_output_path"] = s3_output_path

        @builtins.property
        def notebook_output_option(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.SharingSettingsProperty.NotebookOutputOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-notebookoutputoption
            '''
            result = self._values.get("notebook_output_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.SharingSettingsProperty.S3KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-s3kmskeyid
            '''
            result = self._values.get("s3_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_output_path(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.SharingSettingsProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-s3outputpath
            '''
            result = self._values.get("s3_output_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SharingSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.UserSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_role": "executionRole",
            "jupyter_server_app_settings": "jupyterServerAppSettings",
            "kernel_gateway_app_settings": "kernelGatewayAppSettings",
            "security_groups": "securityGroups",
            "sharing_settings": "sharingSettings",
        },
    )
    class UserSettingsProperty:
        def __init__(
            self,
            *,
            execution_role: typing.Optional[builtins.str] = None,
            jupyter_server_app_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.JupyterServerAppSettingsProperty"]] = None,
            kernel_gateway_app_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.KernelGatewayAppSettingsProperty"]] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            sharing_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.SharingSettingsProperty"]] = None,
        ) -> None:
            '''
            :param execution_role: ``CfnUserProfile.UserSettingsProperty.ExecutionRole``.
            :param jupyter_server_app_settings: ``CfnUserProfile.UserSettingsProperty.JupyterServerAppSettings``.
            :param kernel_gateway_app_settings: ``CfnUserProfile.UserSettingsProperty.KernelGatewayAppSettings``.
            :param security_groups: ``CfnUserProfile.UserSettingsProperty.SecurityGroups``.
            :param sharing_settings: ``CfnUserProfile.UserSettingsProperty.SharingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                user_settings_property = sagemaker.CfnUserProfile.UserSettingsProperty(
                    execution_role="executionRole",
                    jupyter_server_app_settings=sagemaker.CfnUserProfile.JupyterServerAppSettingsProperty(
                        default_resource_spec=sagemaker.CfnUserProfile.ResourceSpecProperty(
                            instance_type="instanceType",
                            sage_maker_image_arn="sageMakerImageArn",
                            sage_maker_image_version_arn="sageMakerImageVersionArn"
                        )
                    ),
                    kernel_gateway_app_settings=sagemaker.CfnUserProfile.KernelGatewayAppSettingsProperty(
                        custom_images=[sagemaker.CfnUserProfile.CustomImageProperty(
                            app_image_config_name="appImageConfigName",
                            image_name="imageName",
                
                            # the properties below are optional
                            image_version_number=123
                        )],
                        default_resource_spec=sagemaker.CfnUserProfile.ResourceSpecProperty(
                            instance_type="instanceType",
                            sage_maker_image_arn="sageMakerImageArn",
                            sage_maker_image_version_arn="sageMakerImageVersionArn"
                        )
                    ),
                    security_groups=["securityGroups"],
                    sharing_settings=sagemaker.CfnUserProfile.SharingSettingsProperty(
                        notebook_output_option="notebookOutputOption",
                        s3_kms_key_id="s3KmsKeyId",
                        s3_output_path="s3OutputPath"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if execution_role is not None:
                self._values["execution_role"] = execution_role
            if jupyter_server_app_settings is not None:
                self._values["jupyter_server_app_settings"] = jupyter_server_app_settings
            if kernel_gateway_app_settings is not None:
                self._values["kernel_gateway_app_settings"] = kernel_gateway_app_settings
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if sharing_settings is not None:
                self._values["sharing_settings"] = sharing_settings

        @builtins.property
        def execution_role(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.UserSettingsProperty.ExecutionRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-executionrole
            '''
            result = self._values.get("execution_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def jupyter_server_app_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.JupyterServerAppSettingsProperty"]]:
            '''``CfnUserProfile.UserSettingsProperty.JupyterServerAppSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-jupyterserverappsettings
            '''
            result = self._values.get("jupyter_server_app_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.JupyterServerAppSettingsProperty"]], result)

        @builtins.property
        def kernel_gateway_app_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.KernelGatewayAppSettingsProperty"]]:
            '''``CfnUserProfile.UserSettingsProperty.KernelGatewayAppSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-kernelgatewayappsettings
            '''
            result = self._values.get("kernel_gateway_app_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.KernelGatewayAppSettingsProperty"]], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnUserProfile.UserSettingsProperty.SecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def sharing_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.SharingSettingsProperty"]]:
            '''``CfnUserProfile.UserSettingsProperty.SharingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-sharingsettings
            '''
            result = self._values.get("sharing_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.SharingSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_id": "domainId",
        "single_sign_on_user_identifier": "singleSignOnUserIdentifier",
        "single_sign_on_user_value": "singleSignOnUserValue",
        "tags": "tags",
        "user_profile_name": "userProfileName",
        "user_settings": "userSettings",
    },
)
class CfnUserProfileProps:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        single_sign_on_user_identifier: typing.Optional[builtins.str] = None,
        single_sign_on_user_value: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_profile_name: builtins.str,
        user_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUserProfile.UserSettingsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::UserProfile``.

        :param domain_id: ``AWS::SageMaker::UserProfile.DomainId``.
        :param single_sign_on_user_identifier: ``AWS::SageMaker::UserProfile.SingleSignOnUserIdentifier``.
        :param single_sign_on_user_value: ``AWS::SageMaker::UserProfile.SingleSignOnUserValue``.
        :param tags: ``AWS::SageMaker::UserProfile.Tags``.
        :param user_profile_name: ``AWS::SageMaker::UserProfile.UserProfileName``.
        :param user_settings: ``AWS::SageMaker::UserProfile.UserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_user_profile_props = sagemaker.CfnUserProfileProps(
                domain_id="domainId",
                user_profile_name="userProfileName",
            
                # the properties below are optional
                single_sign_on_user_identifier="singleSignOnUserIdentifier",
                single_sign_on_user_value="singleSignOnUserValue",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_settings=sagemaker.CfnUserProfile.UserSettingsProperty(
                    execution_role="executionRole",
                    jupyter_server_app_settings=sagemaker.CfnUserProfile.JupyterServerAppSettingsProperty(
                        default_resource_spec=sagemaker.CfnUserProfile.ResourceSpecProperty(
                            instance_type="instanceType",
                            sage_maker_image_arn="sageMakerImageArn",
                            sage_maker_image_version_arn="sageMakerImageVersionArn"
                        )
                    ),
                    kernel_gateway_app_settings=sagemaker.CfnUserProfile.KernelGatewayAppSettingsProperty(
                        custom_images=[sagemaker.CfnUserProfile.CustomImageProperty(
                            app_image_config_name="appImageConfigName",
                            image_name="imageName",
            
                            # the properties below are optional
                            image_version_number=123
                        )],
                        default_resource_spec=sagemaker.CfnUserProfile.ResourceSpecProperty(
                            instance_type="instanceType",
                            sage_maker_image_arn="sageMakerImageArn",
                            sage_maker_image_version_arn="sageMakerImageVersionArn"
                        )
                    ),
                    security_groups=["securityGroups"],
                    sharing_settings=sagemaker.CfnUserProfile.SharingSettingsProperty(
                        notebook_output_option="notebookOutputOption",
                        s3_kms_key_id="s3KmsKeyId",
                        s3_output_path="s3OutputPath"
                    )
                )
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_id": domain_id,
            "user_profile_name": user_profile_name,
        }
        if single_sign_on_user_identifier is not None:
            self._values["single_sign_on_user_identifier"] = single_sign_on_user_identifier
        if single_sign_on_user_value is not None:
            self._values["single_sign_on_user_value"] = single_sign_on_user_value
        if tags is not None:
            self._values["tags"] = tags
        if user_settings is not None:
            self._values["user_settings"] = user_settings

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''``AWS::SageMaker::UserProfile.DomainId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-domainid
        '''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def single_sign_on_user_identifier(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::UserProfile.SingleSignOnUserIdentifier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuseridentifier
        '''
        result = self._values.get("single_sign_on_user_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_sign_on_user_value(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::UserProfile.SingleSignOnUserValue``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuservalue
        '''
        result = self._values.get("single_sign_on_user_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::UserProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def user_profile_name(self) -> builtins.str:
        '''``AWS::SageMaker::UserProfile.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-userprofilename
        '''
        result = self._values.get("user_profile_name")
        assert result is not None, "Required property 'user_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUserProfile.UserSettingsProperty]]:
        '''``AWS::SageMaker::UserProfile.UserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-usersettings
        '''
        result = self._values.get("user_settings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUserProfile.UserSettingsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWorkteam(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam",
):
    '''A CloudFormation ``AWS::SageMaker::Workteam``.

    :cloudformationResource: AWS::SageMaker::Workteam
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker as sagemaker
        
        cfn_workteam = sagemaker.CfnWorkteam(self, "MyCfnWorkteam",
            description="description",
            member_definitions=[sagemaker.CfnWorkteam.MemberDefinitionProperty(
                cognito_member_definition=sagemaker.CfnWorkteam.CognitoMemberDefinitionProperty(
                    cognito_client_id="cognitoClientId",
                    cognito_user_group="cognitoUserGroup",
                    cognito_user_pool="cognitoUserPool"
                )
            )],
            notification_configuration=sagemaker.CfnWorkteam.NotificationConfigurationProperty(
                notification_topic_arn="notificationTopicArn"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            workteam_name="workteamName"
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        member_definitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]] = None,
        notification_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        workteam_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Workteam``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::SageMaker::Workteam.Description``.
        :param member_definitions: ``AWS::SageMaker::Workteam.MemberDefinitions``.
        :param notification_configuration: ``AWS::SageMaker::Workteam.NotificationConfiguration``.
        :param tags: ``AWS::SageMaker::Workteam.Tags``.
        :param workteam_name: ``AWS::SageMaker::Workteam.WorkteamName``.
        '''
        props = CfnWorkteamProps(
            description=description,
            member_definitions=member_definitions,
            notification_configuration=notification_configuration,
            tags=tags,
            workteam_name=workteam_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrWorkteamName")
    def attr_workteam_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: WorkteamName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkteamName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Workteam.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memberDefinitions")
    def member_definitions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]]:
        '''``AWS::SageMaker::Workteam.MemberDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-memberdefinitions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]], jsii.get(self, "memberDefinitions"))

    @member_definitions.setter
    def member_definitions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]],
    ) -> None:
        jsii.set(self, "memberDefinitions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]]:
        '''``AWS::SageMaker::Workteam.NotificationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-notificationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]], jsii.get(self, "notificationConfiguration"))

    @notification_configuration.setter
    def notification_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "notificationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Workteam.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workteamName")
    def workteam_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Workteam.WorkteamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-workteamname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workteamName"))

    @workteam_name.setter
    def workteam_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "workteamName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.CognitoMemberDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cognito_client_id": "cognitoClientId",
            "cognito_user_group": "cognitoUserGroup",
            "cognito_user_pool": "cognitoUserPool",
        },
    )
    class CognitoMemberDefinitionProperty:
        def __init__(
            self,
            *,
            cognito_client_id: builtins.str,
            cognito_user_group: builtins.str,
            cognito_user_pool: builtins.str,
        ) -> None:
            '''
            :param cognito_client_id: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoClientId``.
            :param cognito_user_group: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserGroup``.
            :param cognito_user_pool: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserPool``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                cognito_member_definition_property = sagemaker.CfnWorkteam.CognitoMemberDefinitionProperty(
                    cognito_client_id="cognitoClientId",
                    cognito_user_group="cognitoUserGroup",
                    cognito_user_pool="cognitoUserPool"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cognito_client_id": cognito_client_id,
                "cognito_user_group": cognito_user_group,
                "cognito_user_pool": cognito_user_pool,
            }

        @builtins.property
        def cognito_client_id(self) -> builtins.str:
            '''``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoClientId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitoclientid
            '''
            result = self._values.get("cognito_client_id")
            assert result is not None, "Required property 'cognito_client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cognito_user_group(self) -> builtins.str:
            '''``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitousergroup
            '''
            result = self._values.get("cognito_user_group")
            assert result is not None, "Required property 'cognito_user_group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cognito_user_pool(self) -> builtins.str:
            '''``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserPool``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitouserpool
            '''
            result = self._values.get("cognito_user_pool")
            assert result is not None, "Required property 'cognito_user_pool' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoMemberDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.MemberDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"cognito_member_definition": "cognitoMemberDefinition"},
    )
    class MemberDefinitionProperty:
        def __init__(
            self,
            *,
            cognito_member_definition: typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.CognitoMemberDefinitionProperty"],
        ) -> None:
            '''
            :param cognito_member_definition: ``CfnWorkteam.MemberDefinitionProperty.CognitoMemberDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                member_definition_property = sagemaker.CfnWorkteam.MemberDefinitionProperty(
                    cognito_member_definition=sagemaker.CfnWorkteam.CognitoMemberDefinitionProperty(
                        cognito_client_id="cognitoClientId",
                        cognito_user_group="cognitoUserGroup",
                        cognito_user_pool="cognitoUserPool"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cognito_member_definition": cognito_member_definition,
            }

        @builtins.property
        def cognito_member_definition(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.CognitoMemberDefinitionProperty"]:
            '''``CfnWorkteam.MemberDefinitionProperty.CognitoMemberDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html#cfn-sagemaker-workteam-memberdefinition-cognitomemberdefinition
            '''
            result = self._values.get("cognito_member_definition")
            assert result is not None, "Required property 'cognito_member_definition' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.CognitoMemberDefinitionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.NotificationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"notification_topic_arn": "notificationTopicArn"},
    )
    class NotificationConfigurationProperty:
        def __init__(self, *, notification_topic_arn: builtins.str) -> None:
            '''
            :param notification_topic_arn: ``CfnWorkteam.NotificationConfigurationProperty.NotificationTopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sagemaker as sagemaker
                
                notification_configuration_property = sagemaker.CfnWorkteam.NotificationConfigurationProperty(
                    notification_topic_arn="notificationTopicArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "notification_topic_arn": notification_topic_arn,
            }

        @builtins.property
        def notification_topic_arn(self) -> builtins.str:
            '''``CfnWorkteam.NotificationConfigurationProperty.NotificationTopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html#cfn-sagemaker-workteam-notificationconfiguration-notificationtopicarn
            '''
            result = self._values.get("notification_topic_arn")
            assert result is not None, "Required property 'notification_topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteamProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "member_definitions": "memberDefinitions",
        "notification_configuration": "notificationConfiguration",
        "tags": "tags",
        "workteam_name": "workteamName",
    },
)
class CfnWorkteamProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        member_definitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.MemberDefinitionProperty]]]] = None,
        notification_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.NotificationConfigurationProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        workteam_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Workteam``.

        :param description: ``AWS::SageMaker::Workteam.Description``.
        :param member_definitions: ``AWS::SageMaker::Workteam.MemberDefinitions``.
        :param notification_configuration: ``AWS::SageMaker::Workteam.NotificationConfiguration``.
        :param tags: ``AWS::SageMaker::Workteam.Tags``.
        :param workteam_name: ``AWS::SageMaker::Workteam.WorkteamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker as sagemaker
            
            cfn_workteam_props = sagemaker.CfnWorkteamProps(
                description="description",
                member_definitions=[sagemaker.CfnWorkteam.MemberDefinitionProperty(
                    cognito_member_definition=sagemaker.CfnWorkteam.CognitoMemberDefinitionProperty(
                        cognito_client_id="cognitoClientId",
                        cognito_user_group="cognitoUserGroup",
                        cognito_user_pool="cognitoUserPool"
                    )
                )],
                notification_configuration=sagemaker.CfnWorkteam.NotificationConfigurationProperty(
                    notification_topic_arn="notificationTopicArn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                workteam_name="workteamName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if member_definitions is not None:
            self._values["member_definitions"] = member_definitions
        if notification_configuration is not None:
            self._values["notification_configuration"] = notification_configuration
        if tags is not None:
            self._values["tags"] = tags
        if workteam_name is not None:
            self._values["workteam_name"] = workteam_name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Workteam.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def member_definitions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.MemberDefinitionProperty]]]]:
        '''``AWS::SageMaker::Workteam.MemberDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-memberdefinitions
        '''
        result = self._values.get("member_definitions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.MemberDefinitionProperty]]]], result)

    @builtins.property
    def notification_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.NotificationConfigurationProperty]]:
        '''``AWS::SageMaker::Workteam.NotificationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-notificationconfiguration
        '''
        result = self._values.get("notification_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.NotificationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Workteam.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def workteam_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Workteam.WorkteamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-workteamname
        '''
        result = self._values.get("workteam_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkteamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApp",
    "CfnAppImageConfig",
    "CfnAppImageConfigProps",
    "CfnAppProps",
    "CfnCodeRepository",
    "CfnCodeRepositoryProps",
    "CfnDataQualityJobDefinition",
    "CfnDataQualityJobDefinitionProps",
    "CfnDevice",
    "CfnDeviceFleet",
    "CfnDeviceFleetProps",
    "CfnDeviceProps",
    "CfnDomain",
    "CfnDomainProps",
    "CfnEndpoint",
    "CfnEndpointConfig",
    "CfnEndpointConfigProps",
    "CfnEndpointProps",
    "CfnFeatureGroup",
    "CfnFeatureGroupProps",
    "CfnImage",
    "CfnImageProps",
    "CfnImageVersion",
    "CfnImageVersionProps",
    "CfnModel",
    "CfnModelBiasJobDefinition",
    "CfnModelBiasJobDefinitionProps",
    "CfnModelExplainabilityJobDefinition",
    "CfnModelExplainabilityJobDefinitionProps",
    "CfnModelPackageGroup",
    "CfnModelPackageGroupProps",
    "CfnModelProps",
    "CfnModelQualityJobDefinition",
    "CfnModelQualityJobDefinitionProps",
    "CfnMonitoringSchedule",
    "CfnMonitoringScheduleProps",
    "CfnNotebookInstance",
    "CfnNotebookInstanceLifecycleConfig",
    "CfnNotebookInstanceLifecycleConfigProps",
    "CfnNotebookInstanceProps",
    "CfnPipeline",
    "CfnPipelineProps",
    "CfnProject",
    "CfnProjectProps",
    "CfnUserProfile",
    "CfnUserProfileProps",
    "CfnWorkteam",
    "CfnWorkteamProps",
]

publication.publish()
