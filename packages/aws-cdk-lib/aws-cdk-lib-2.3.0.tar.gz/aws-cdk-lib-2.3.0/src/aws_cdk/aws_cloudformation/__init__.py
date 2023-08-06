'''
# AWS CloudFormation Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnCustomResource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnCustomResource",
):
    '''A CloudFormation ``AWS::CloudFormation::CustomResource``.

    :cloudformationResource: AWS::CloudFormation::CustomResource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_custom_resource = cloudformation.CfnCustomResource(self, "MyCfnCustomResource",
            service_token="serviceToken"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service_token: builtins.str,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::CustomResource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param service_token: ``AWS::CloudFormation::CustomResource.ServiceToken``.
        '''
        props = CfnCustomResourceProps(service_token=service_token)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> builtins.str:
        '''``AWS::CloudFormation::CustomResource.ServiceToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: builtins.str) -> None:
        jsii.set(self, "serviceToken", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnCustomResourceProps",
    jsii_struct_bases=[],
    name_mapping={"service_token": "serviceToken"},
)
class CfnCustomResourceProps:
    def __init__(self, *, service_token: builtins.str) -> None:
        '''Properties for defining a ``AWS::CloudFormation::CustomResource``.

        :param service_token: ``AWS::CloudFormation::CustomResource.ServiceToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_custom_resource_props = cloudformation.CfnCustomResourceProps(
                service_token="serviceToken"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "service_token": service_token,
        }

    @builtins.property
    def service_token(self) -> builtins.str:
        '''``AWS::CloudFormation::CustomResource.ServiceToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken
        '''
        result = self._values.get("service_token")
        assert result is not None, "Required property 'service_token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMacro(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnMacro",
):
    '''A CloudFormation ``AWS::CloudFormation::Macro``.

    :cloudformationResource: AWS::CloudFormation::Macro
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_macro = cloudformation.CfnMacro(self, "MyCfnMacro",
            function_name="functionName",
            name="name",
        
            # the properties below are optional
            description="description",
            log_group_name="logGroupName",
            log_role_arn="logRoleArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        function_name: builtins.str,
        log_group_name: typing.Optional[builtins.str] = None,
        log_role_arn: typing.Optional[builtins.str] = None,
        name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::Macro``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::CloudFormation::Macro.Description``.
        :param function_name: ``AWS::CloudFormation::Macro.FunctionName``.
        :param log_group_name: ``AWS::CloudFormation::Macro.LogGroupName``.
        :param log_role_arn: ``AWS::CloudFormation::Macro.LogRoleARN``.
        :param name: ``AWS::CloudFormation::Macro.Name``.
        '''
        props = CfnMacroProps(
            description=description,
            function_name=function_name,
            log_group_name=log_group_name,
            log_role_arn=log_role_arn,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
        '''``AWS::CloudFormation::Macro.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        '''``AWS::CloudFormation::Macro.FunctionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        jsii.set(self, "functionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.LogGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logRoleArn")
    def log_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.LogRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logRoleArn"))

    @log_role_arn.setter
    def log_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::CloudFormation::Macro.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnMacroProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "function_name": "functionName",
        "log_group_name": "logGroupName",
        "log_role_arn": "logRoleArn",
        "name": "name",
    },
)
class CfnMacroProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        function_name: builtins.str,
        log_group_name: typing.Optional[builtins.str] = None,
        log_role_arn: typing.Optional[builtins.str] = None,
        name: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::Macro``.

        :param description: ``AWS::CloudFormation::Macro.Description``.
        :param function_name: ``AWS::CloudFormation::Macro.FunctionName``.
        :param log_group_name: ``AWS::CloudFormation::Macro.LogGroupName``.
        :param log_role_arn: ``AWS::CloudFormation::Macro.LogRoleARN``.
        :param name: ``AWS::CloudFormation::Macro.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_macro_props = cloudformation.CfnMacroProps(
                function_name="functionName",
                name="name",
            
                # the properties below are optional
                description="description",
                log_group_name="logGroupName",
                log_role_arn="logRoleArn"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "function_name": function_name,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_role_arn is not None:
            self._values["log_role_arn"] = log_role_arn

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_name(self) -> builtins.str:
        '''``AWS::CloudFormation::Macro.FunctionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
        '''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.LogGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
        '''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.LogRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
        '''
        result = self._values.get("log_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::CloudFormation::Macro.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMacroProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnModuleDefaultVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnModuleDefaultVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::ModuleDefaultVersion``.

    :cloudformationResource: AWS::CloudFormation::ModuleDefaultVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_module_default_version = cloudformation.CfnModuleDefaultVersion(self, "MyCfnModuleDefaultVersion",
            arn="arn",
            module_name="moduleName",
            version_id="versionId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        module_name: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::ModuleDefaultVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param arn: ``AWS::CloudFormation::ModuleDefaultVersion.Arn``.
        :param module_name: ``AWS::CloudFormation::ModuleDefaultVersion.ModuleName``.
        :param version_id: ``AWS::CloudFormation::ModuleDefaultVersion.VersionId``.
        '''
        props = CfnModuleDefaultVersionProps(
            arn=arn, module_name=module_name, version_id=version_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="arn")
    def arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.Arn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-arn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "arn", value)

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
    @jsii.member(jsii_name="moduleName")
    def module_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.ModuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-modulename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "moduleName"))

    @module_name.setter
    def module_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "moduleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-versionid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnModuleDefaultVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "module_name": "moduleName",
        "version_id": "versionId",
    },
)
class CfnModuleDefaultVersionProps:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        module_name: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::ModuleDefaultVersion``.

        :param arn: ``AWS::CloudFormation::ModuleDefaultVersion.Arn``.
        :param module_name: ``AWS::CloudFormation::ModuleDefaultVersion.ModuleName``.
        :param version_id: ``AWS::CloudFormation::ModuleDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_module_default_version_props = cloudformation.CfnModuleDefaultVersionProps(
                arn="arn",
                module_name="moduleName",
                version_id="versionId"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if module_name is not None:
            self._values["module_name"] = module_name
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.Arn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def module_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.ModuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-modulename
        '''
        result = self._values.get("module_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-versionid
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModuleDefaultVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnModuleVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnModuleVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::ModuleVersion``.

    :cloudformationResource: AWS::CloudFormation::ModuleVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_module_version = cloudformation.CfnModuleVersion(self, "MyCfnModuleVersion",
            module_name="moduleName",
            module_package="modulePackage"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        module_name: builtins.str,
        module_package: builtins.str,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::ModuleVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param module_name: ``AWS::CloudFormation::ModuleVersion.ModuleName``.
        :param module_package: ``AWS::CloudFormation::ModuleVersion.ModulePackage``.
        '''
        props = CfnModuleVersionProps(
            module_name=module_name, module_package=module_package
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDescription")
    def attr_description(self) -> builtins.str:
        '''
        :cloudformationAttribute: Description
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDescription"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDocumentationUrl")
    def attr_documentation_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: DocumentationUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDocumentationUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsDefaultVersion")
    def attr_is_default_version(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: IsDefaultVersion
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsDefaultVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSchema")
    def attr_schema(self) -> builtins.str:
        '''
        :cloudformationAttribute: Schema
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchema"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTimeCreated")
    def attr_time_created(self) -> builtins.str:
        '''
        :cloudformationAttribute: TimeCreated
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTimeCreated"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVisibility")
    def attr_visibility(self) -> builtins.str:
        '''
        :cloudformationAttribute: Visibility
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVisibility"))

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
    @jsii.member(jsii_name="moduleName")
    def module_name(self) -> builtins.str:
        '''``AWS::CloudFormation::ModuleVersion.ModuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename
        '''
        return typing.cast(builtins.str, jsii.get(self, "moduleName"))

    @module_name.setter
    def module_name(self, value: builtins.str) -> None:
        jsii.set(self, "moduleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modulePackage")
    def module_package(self) -> builtins.str:
        '''``AWS::CloudFormation::ModuleVersion.ModulePackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage
        '''
        return typing.cast(builtins.str, jsii.get(self, "modulePackage"))

    @module_package.setter
    def module_package(self, value: builtins.str) -> None:
        jsii.set(self, "modulePackage", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnModuleVersionProps",
    jsii_struct_bases=[],
    name_mapping={"module_name": "moduleName", "module_package": "modulePackage"},
)
class CfnModuleVersionProps:
    def __init__(
        self,
        *,
        module_name: builtins.str,
        module_package: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::ModuleVersion``.

        :param module_name: ``AWS::CloudFormation::ModuleVersion.ModuleName``.
        :param module_package: ``AWS::CloudFormation::ModuleVersion.ModulePackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_module_version_props = cloudformation.CfnModuleVersionProps(
                module_name="moduleName",
                module_package="modulePackage"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "module_name": module_name,
            "module_package": module_package,
        }

    @builtins.property
    def module_name(self) -> builtins.str:
        '''``AWS::CloudFormation::ModuleVersion.ModuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename
        '''
        result = self._values.get("module_name")
        assert result is not None, "Required property 'module_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def module_package(self) -> builtins.str:
        '''``AWS::CloudFormation::ModuleVersion.ModulePackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage
        '''
        result = self._values.get("module_package")
        assert result is not None, "Required property 'module_package' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModuleVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPublicTypeVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnPublicTypeVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::PublicTypeVersion``.

    :cloudformationResource: AWS::CloudFormation::PublicTypeVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_public_type_version = cloudformation.CfnPublicTypeVersion(self, "MyCfnPublicTypeVersion",
            arn="arn",
            log_delivery_bucket="logDeliveryBucket",
            public_version_number="publicVersionNumber",
            type="type",
            type_name="typeName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        log_delivery_bucket: typing.Optional[builtins.str] = None,
        public_version_number: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::PublicTypeVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param arn: ``AWS::CloudFormation::PublicTypeVersion.Arn``.
        :param log_delivery_bucket: ``AWS::CloudFormation::PublicTypeVersion.LogDeliveryBucket``.
        :param public_version_number: ``AWS::CloudFormation::PublicTypeVersion.PublicVersionNumber``.
        :param type: ``AWS::CloudFormation::PublicTypeVersion.Type``.
        :param type_name: ``AWS::CloudFormation::PublicTypeVersion.TypeName``.
        '''
        props = CfnPublicTypeVersionProps(
            arn=arn,
            log_delivery_bucket=log_delivery_bucket,
            public_version_number=public_version_number,
            type=type,
            type_name=type_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="arn")
    def arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.Arn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-arn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "arn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublicTypeArn")
    def attr_public_type_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublicTypeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicTypeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublisherId")
    def attr_publisher_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublisherId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTypeVersionArn")
    def attr_type_version_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: TypeVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeVersionArn"))

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
    @jsii.member(jsii_name="logDeliveryBucket")
    def log_delivery_bucket(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.LogDeliveryBucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-logdeliverybucket
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDeliveryBucket"))

    @log_delivery_bucket.setter
    def log_delivery_bucket(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logDeliveryBucket", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publicVersionNumber")
    def public_version_number(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.PublicVersionNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-publicversionnumber
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicVersionNumber"))

    @public_version_number.setter
    def public_version_number(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "publicVersionNumber", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-typename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnPublicTypeVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "log_delivery_bucket": "logDeliveryBucket",
        "public_version_number": "publicVersionNumber",
        "type": "type",
        "type_name": "typeName",
    },
)
class CfnPublicTypeVersionProps:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        log_delivery_bucket: typing.Optional[builtins.str] = None,
        public_version_number: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::PublicTypeVersion``.

        :param arn: ``AWS::CloudFormation::PublicTypeVersion.Arn``.
        :param log_delivery_bucket: ``AWS::CloudFormation::PublicTypeVersion.LogDeliveryBucket``.
        :param public_version_number: ``AWS::CloudFormation::PublicTypeVersion.PublicVersionNumber``.
        :param type: ``AWS::CloudFormation::PublicTypeVersion.Type``.
        :param type_name: ``AWS::CloudFormation::PublicTypeVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_public_type_version_props = cloudformation.CfnPublicTypeVersionProps(
                arn="arn",
                log_delivery_bucket="logDeliveryBucket",
                public_version_number="publicVersionNumber",
                type="type",
                type_name="typeName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if log_delivery_bucket is not None:
            self._values["log_delivery_bucket"] = log_delivery_bucket
        if public_version_number is not None:
            self._values["public_version_number"] = public_version_number
        if type is not None:
            self._values["type"] = type
        if type_name is not None:
            self._values["type_name"] = type_name

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.Arn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery_bucket(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.LogDeliveryBucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-logdeliverybucket
        '''
        result = self._values.get("log_delivery_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_version_number(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.PublicVersionNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-publicversionnumber
        '''
        result = self._values.get("public_version_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublicTypeVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPublisher(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnPublisher",
):
    '''A CloudFormation ``AWS::CloudFormation::Publisher``.

    :cloudformationResource: AWS::CloudFormation::Publisher
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_publisher = cloudformation.CfnPublisher(self, "MyCfnPublisher",
            accept_terms_and_conditions=False,
        
            # the properties below are optional
            connection_arn="connectionArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accept_terms_and_conditions: typing.Union[builtins.bool, _IResolvable_da3f097b],
        connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::Publisher``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param accept_terms_and_conditions: ``AWS::CloudFormation::Publisher.AcceptTermsAndConditions``.
        :param connection_arn: ``AWS::CloudFormation::Publisher.ConnectionArn``.
        '''
        props = CfnPublisherProps(
            accept_terms_and_conditions=accept_terms_and_conditions,
            connection_arn=connection_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="acceptTermsAndConditions")
    def accept_terms_and_conditions(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''``AWS::CloudFormation::Publisher.AcceptTermsAndConditions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-accepttermsandconditions
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "acceptTermsAndConditions"))

    @accept_terms_and_conditions.setter
    def accept_terms_and_conditions(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "acceptTermsAndConditions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIdentityProvider")
    def attr_identity_provider(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdentityProvider
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityProvider"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublisherId")
    def attr_publisher_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublisherId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublisherProfile")
    def attr_publisher_profile(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublisherProfile
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherProfile"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublisherStatus")
    def attr_publisher_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublisherStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherStatus"))

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
    @jsii.member(jsii_name="connectionArn")
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Publisher.ConnectionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-connectionarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionArn"))

    @connection_arn.setter
    def connection_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "connectionArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnPublisherProps",
    jsii_struct_bases=[],
    name_mapping={
        "accept_terms_and_conditions": "acceptTermsAndConditions",
        "connection_arn": "connectionArn",
    },
)
class CfnPublisherProps:
    def __init__(
        self,
        *,
        accept_terms_and_conditions: typing.Union[builtins.bool, _IResolvable_da3f097b],
        connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::Publisher``.

        :param accept_terms_and_conditions: ``AWS::CloudFormation::Publisher.AcceptTermsAndConditions``.
        :param connection_arn: ``AWS::CloudFormation::Publisher.ConnectionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_publisher_props = cloudformation.CfnPublisherProps(
                accept_terms_and_conditions=False,
            
                # the properties below are optional
                connection_arn="connectionArn"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "accept_terms_and_conditions": accept_terms_and_conditions,
        }
        if connection_arn is not None:
            self._values["connection_arn"] = connection_arn

    @builtins.property
    def accept_terms_and_conditions(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''``AWS::CloudFormation::Publisher.AcceptTermsAndConditions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-accepttermsandconditions
        '''
        result = self._values.get("accept_terms_and_conditions")
        assert result is not None, "Required property 'accept_terms_and_conditions' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Publisher.ConnectionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-connectionarn
        '''
        result = self._values.get("connection_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublisherProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceDefaultVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceDefaultVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::ResourceDefaultVersion``.

    :cloudformationResource: AWS::CloudFormation::ResourceDefaultVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_resource_default_version = cloudformation.CfnResourceDefaultVersion(self, "MyCfnResourceDefaultVersion",
            type_name="typeName",
            type_version_arn="typeVersionArn",
            version_id="versionId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type_name: typing.Optional[builtins.str] = None,
        type_version_arn: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::ResourceDefaultVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param type_name: ``AWS::CloudFormation::ResourceDefaultVersion.TypeName``.
        :param type_version_arn: ``AWS::CloudFormation::ResourceDefaultVersion.TypeVersionArn``.
        :param version_id: ``AWS::CloudFormation::ResourceDefaultVersion.VersionId``.
        '''
        props = CfnResourceDefaultVersionProps(
            type_name=type_name,
            type_version_arn=type_version_arn,
            version_id=version_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeVersionArn")
    def type_version_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.TypeVersionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typeversionarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeVersionArn"))

    @type_version_arn.setter
    def type_version_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeVersionArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-versionid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceDefaultVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "type_name": "typeName",
        "type_version_arn": "typeVersionArn",
        "version_id": "versionId",
    },
)
class CfnResourceDefaultVersionProps:
    def __init__(
        self,
        *,
        type_name: typing.Optional[builtins.str] = None,
        type_version_arn: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::ResourceDefaultVersion``.

        :param type_name: ``AWS::CloudFormation::ResourceDefaultVersion.TypeName``.
        :param type_version_arn: ``AWS::CloudFormation::ResourceDefaultVersion.TypeVersionArn``.
        :param version_id: ``AWS::CloudFormation::ResourceDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_resource_default_version_props = cloudformation.CfnResourceDefaultVersionProps(
                type_name="typeName",
                type_version_arn="typeVersionArn",
                version_id="versionId"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if type_name is not None:
            self._values["type_name"] = type_name
        if type_version_arn is not None:
            self._values["type_version_arn"] = type_version_arn
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_version_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.TypeVersionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typeversionarn
        '''
        result = self._values.get("type_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-versionid
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceDefaultVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::ResourceVersion``.

    :cloudformationResource: AWS::CloudFormation::ResourceVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_resource_version = cloudformation.CfnResourceVersion(self, "MyCfnResourceVersion",
            schema_handler_package="schemaHandlerPackage",
            type_name="typeName",
        
            # the properties below are optional
            execution_role_arn="executionRoleArn",
            logging_config=cloudformation.CfnResourceVersion.LoggingConfigProperty(
                log_group_name="logGroupName",
                log_role_arn="logRoleArn"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union["CfnResourceVersion.LoggingConfigProperty", _IResolvable_da3f097b]] = None,
        schema_handler_package: builtins.str,
        type_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::ResourceVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param execution_role_arn: ``AWS::CloudFormation::ResourceVersion.ExecutionRoleArn``.
        :param logging_config: ``AWS::CloudFormation::ResourceVersion.LoggingConfig``.
        :param schema_handler_package: ``AWS::CloudFormation::ResourceVersion.SchemaHandlerPackage``.
        :param type_name: ``AWS::CloudFormation::ResourceVersion.TypeName``.
        '''
        props = CfnResourceVersionProps(
            execution_role_arn=execution_role_arn,
            logging_config=logging_config,
            schema_handler_package=schema_handler_package,
            type_name=type_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsDefaultVersion")
    def attr_is_default_version(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: IsDefaultVersion
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsDefaultVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProvisioningType")
    def attr_provisioning_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProvisioningType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvisioningType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTypeArn")
    def attr_type_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: TypeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVisibility")
    def attr_visibility(self) -> builtins.str:
        '''
        :cloudformationAttribute: Visibility
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVisibility"))

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
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceVersion.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-executionrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union["CfnResourceVersion.LoggingConfigProperty", _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::ResourceVersion.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-loggingconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResourceVersion.LoggingConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "loggingConfig"))

    @logging_config.setter
    def logging_config(
        self,
        value: typing.Optional[typing.Union["CfnResourceVersion.LoggingConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "loggingConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schemaHandlerPackage")
    def schema_handler_package(self) -> builtins.str:
        '''``AWS::CloudFormation::ResourceVersion.SchemaHandlerPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-schemahandlerpackage
        '''
        return typing.cast(builtins.str, jsii.get(self, "schemaHandlerPackage"))

    @schema_handler_package.setter
    def schema_handler_package(self, value: builtins.str) -> None:
        jsii.set(self, "schemaHandlerPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        '''``AWS::CloudFormation::ResourceVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-typename
        '''
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        jsii.set(self, "typeName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceVersion.LoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "log_role_arn": "logRoleArn"},
    )
    class LoggingConfigProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
            log_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group_name: ``CfnResourceVersion.LoggingConfigProperty.LogGroupName``.
            :param log_role_arn: ``CfnResourceVersion.LoggingConfigProperty.LogRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                logging_config_property = cloudformation.CfnResourceVersion.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_role_arn is not None:
                self._values["log_role_arn"] = log_role_arn

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceVersion.LoggingConfigProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html#cfn-cloudformation-resourceversion-loggingconfig-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceVersion.LoggingConfigProperty.LogRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html#cfn-cloudformation-resourceversion-loggingconfig-logrolearn
            '''
            result = self._values.get("log_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role_arn": "executionRoleArn",
        "logging_config": "loggingConfig",
        "schema_handler_package": "schemaHandlerPackage",
        "type_name": "typeName",
    },
)
class CfnResourceVersionProps:
    def __init__(
        self,
        *,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[CfnResourceVersion.LoggingConfigProperty, _IResolvable_da3f097b]] = None,
        schema_handler_package: builtins.str,
        type_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::ResourceVersion``.

        :param execution_role_arn: ``AWS::CloudFormation::ResourceVersion.ExecutionRoleArn``.
        :param logging_config: ``AWS::CloudFormation::ResourceVersion.LoggingConfig``.
        :param schema_handler_package: ``AWS::CloudFormation::ResourceVersion.SchemaHandlerPackage``.
        :param type_name: ``AWS::CloudFormation::ResourceVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_resource_version_props = cloudformation.CfnResourceVersionProps(
                schema_handler_package="schemaHandlerPackage",
                type_name="typeName",
            
                # the properties below are optional
                execution_role_arn="executionRoleArn",
                logging_config=cloudformation.CfnResourceVersion.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                )
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "schema_handler_package": schema_handler_package,
            "type_name": type_name,
        }
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if logging_config is not None:
            self._values["logging_config"] = logging_config

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceVersion.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[CfnResourceVersion.LoggingConfigProperty, _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::ResourceVersion.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-loggingconfig
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional[typing.Union[CfnResourceVersion.LoggingConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def schema_handler_package(self) -> builtins.str:
        '''``AWS::CloudFormation::ResourceVersion.SchemaHandlerPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-schemahandlerpackage
        '''
        result = self._values.get("schema_handler_package")
        assert result is not None, "Required property 'schema_handler_package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''``AWS::CloudFormation::ResourceVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-typename
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStack(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnStack",
):
    '''A CloudFormation ``AWS::CloudFormation::Stack``.

    :cloudformationResource: AWS::CloudFormation::Stack
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_stack = cloudformation.CfnStack(self, "MyCfnStack",
            template_url="templateUrl",
        
            # the properties below are optional
            notification_arns=["notificationArns"],
            parameters={
                "parameters_key": "parameters"
            },
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            timeout_in_minutes=123
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        template_url: builtins.str,
        timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::Stack``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param notification_arns: ``AWS::CloudFormation::Stack.NotificationARNs``.
        :param parameters: ``AWS::CloudFormation::Stack.Parameters``.
        :param tags: ``AWS::CloudFormation::Stack.Tags``.
        :param template_url: ``AWS::CloudFormation::Stack.TemplateURL``.
        :param timeout_in_minutes: ``AWS::CloudFormation::Stack.TimeoutInMinutes``.
        '''
        props = CfnStackProps(
            notification_arns=notification_arns,
            parameters=parameters,
            tags=tags,
            template_url=template_url,
            timeout_in_minutes=timeout_in_minutes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CloudFormation::Stack.NotificationARNs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationArns"))

    @notification_arns.setter
    def notification_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "notificationArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::CloudFormation::Stack.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::CloudFormation::Stack.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> builtins.str:
        '''``AWS::CloudFormation::Stack.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: builtins.str) -> None:
        jsii.set(self, "templateUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutInMinutes")
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInMinutes"))

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "timeoutInMinutes", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackProps",
    jsii_struct_bases=[],
    name_mapping={
        "notification_arns": "notificationArns",
        "parameters": "parameters",
        "tags": "tags",
        "template_url": "templateUrl",
        "timeout_in_minutes": "timeoutInMinutes",
    },
)
class CfnStackProps:
    def __init__(
        self,
        *,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        template_url: builtins.str,
        timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::Stack``.

        :param notification_arns: ``AWS::CloudFormation::Stack.NotificationARNs``.
        :param parameters: ``AWS::CloudFormation::Stack.Parameters``.
        :param tags: ``AWS::CloudFormation::Stack.Tags``.
        :param template_url: ``AWS::CloudFormation::Stack.TemplateURL``.
        :param timeout_in_minutes: ``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_stack_props = cloudformation.CfnStackProps(
                template_url="templateUrl",
            
                # the properties below are optional
                notification_arns=["notificationArns"],
                parameters={
                    "parameters_key": "parameters"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                timeout_in_minutes=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "template_url": template_url,
        }
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags
        if timeout_in_minutes is not None:
            self._values["timeout_in_minutes"] = timeout_in_minutes

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CloudFormation::Stack.NotificationARNs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::CloudFormation::Stack.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::CloudFormation::Stack.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def template_url(self) -> builtins.str:
        '''``AWS::CloudFormation::Stack.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl
        '''
        result = self._values.get("template_url")
        assert result is not None, "Required property 'template_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes
        '''
        result = self._values.get("timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStackSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet",
):
    '''A CloudFormation ``AWS::CloudFormation::StackSet``.

    :cloudformationResource: AWS::CloudFormation::StackSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        # managed_execution is of type object
        
        cfn_stack_set = cloudformation.CfnStackSet(self, "MyCfnStackSet",
            permission_model="permissionModel",
            stack_set_name="stackSetName",
        
            # the properties below are optional
            administration_role_arn="administrationRoleArn",
            auto_deployment=cloudformation.CfnStackSet.AutoDeploymentProperty(
                enabled=False,
                retain_stacks_on_account_removal=False
            ),
            call_as="callAs",
            capabilities=["capabilities"],
            description="description",
            execution_role_name="executionRoleName",
            managed_execution=managed_execution,
            operation_preferences=cloudformation.CfnStackSet.OperationPreferencesProperty(
                failure_tolerance_count=123,
                failure_tolerance_percentage=123,
                max_concurrent_count=123,
                max_concurrent_percentage=123,
                region_concurrency_type="regionConcurrencyType",
                region_order=["regionOrder"]
            ),
            parameters=[cloudformation.CfnStackSet.ParameterProperty(
                parameter_key="parameterKey",
                parameter_value="parameterValue"
            )],
            stack_instances_group=[cloudformation.CfnStackSet.StackInstancesProperty(
                deployment_targets=cloudformation.CfnStackSet.DeploymentTargetsProperty(
                    accounts=["accounts"],
                    organizational_unit_ids=["organizationalUnitIds"]
                ),
                regions=["regions"],
        
                # the properties below are optional
                parameter_overrides=[cloudformation.CfnStackSet.ParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )]
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            template_body="templateBody",
            template_url="templateUrl"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union["CfnStackSet.AutoDeploymentProperty", _IResolvable_da3f097b]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        managed_execution: typing.Any = None,
        operation_preferences: typing.Optional[typing.Union["CfnStackSet.OperationPreferencesProperty", _IResolvable_da3f097b]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnStackSet.ParameterProperty", _IResolvable_da3f097b]]]] = None,
        permission_model: builtins.str,
        stack_instances_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnStackSet.StackInstancesProperty", _IResolvable_da3f097b]]]] = None,
        stack_set_name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::StackSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param administration_role_arn: ``AWS::CloudFormation::StackSet.AdministrationRoleARN``.
        :param auto_deployment: ``AWS::CloudFormation::StackSet.AutoDeployment``.
        :param call_as: ``AWS::CloudFormation::StackSet.CallAs``.
        :param capabilities: ``AWS::CloudFormation::StackSet.Capabilities``.
        :param description: ``AWS::CloudFormation::StackSet.Description``.
        :param execution_role_name: ``AWS::CloudFormation::StackSet.ExecutionRoleName``.
        :param managed_execution: ``AWS::CloudFormation::StackSet.ManagedExecution``.
        :param operation_preferences: ``AWS::CloudFormation::StackSet.OperationPreferences``.
        :param parameters: ``AWS::CloudFormation::StackSet.Parameters``.
        :param permission_model: ``AWS::CloudFormation::StackSet.PermissionModel``.
        :param stack_instances_group: ``AWS::CloudFormation::StackSet.StackInstancesGroup``.
        :param stack_set_name: ``AWS::CloudFormation::StackSet.StackSetName``.
        :param tags: ``AWS::CloudFormation::StackSet.Tags``.
        :param template_body: ``AWS::CloudFormation::StackSet.TemplateBody``.
        :param template_url: ``AWS::CloudFormation::StackSet.TemplateURL``.
        '''
        props = CfnStackSetProps(
            administration_role_arn=administration_role_arn,
            auto_deployment=auto_deployment,
            call_as=call_as,
            capabilities=capabilities,
            description=description,
            execution_role_name=execution_role_name,
            managed_execution=managed_execution,
            operation_preferences=operation_preferences,
            parameters=parameters,
            permission_model=permission_model,
            stack_instances_group=stack_instances_group,
            stack_set_name=stack_set_name,
            tags=tags,
            template_body=template_body,
            template_url=template_url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="administrationRoleArn")
    def administration_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.AdministrationRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-administrationrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administrationRoleArn"))

    @administration_role_arn.setter
    def administration_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "administrationRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStackSetId")
    def attr_stack_set_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: StackSetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStackSetId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoDeployment")
    def auto_deployment(
        self,
    ) -> typing.Optional[typing.Union["CfnStackSet.AutoDeploymentProperty", _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::StackSet.AutoDeployment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-autodeployment
        '''
        return typing.cast(typing.Optional[typing.Union["CfnStackSet.AutoDeploymentProperty", _IResolvable_da3f097b]], jsii.get(self, "autoDeployment"))

    @auto_deployment.setter
    def auto_deployment(
        self,
        value: typing.Optional[typing.Union["CfnStackSet.AutoDeploymentProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "autoDeployment", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="callAs")
    def call_as(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.CallAs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-callas
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callAs"))

    @call_as.setter
    def call_as(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "callAs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CloudFormation::StackSet.Capabilities``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-capabilities
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "capabilities"))

    @capabilities.setter
    def capabilities(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "capabilities", value)

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
        '''``AWS::CloudFormation::StackSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleName")
    def execution_role_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.ExecutionRoleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-executionrolename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleName"))

    @execution_role_name.setter
    def execution_role_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "executionRoleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="managedExecution")
    def managed_execution(self) -> typing.Any:
        '''``AWS::CloudFormation::StackSet.ManagedExecution``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-managedexecution
        '''
        return typing.cast(typing.Any, jsii.get(self, "managedExecution"))

    @managed_execution.setter
    def managed_execution(self, value: typing.Any) -> None:
        jsii.set(self, "managedExecution", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="operationPreferences")
    def operation_preferences(
        self,
    ) -> typing.Optional[typing.Union["CfnStackSet.OperationPreferencesProperty", _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::StackSet.OperationPreferences``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-operationpreferences
        '''
        return typing.cast(typing.Optional[typing.Union["CfnStackSet.OperationPreferencesProperty", _IResolvable_da3f097b]], jsii.get(self, "operationPreferences"))

    @operation_preferences.setter
    def operation_preferences(
        self,
        value: typing.Optional[typing.Union["CfnStackSet.OperationPreferencesProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "operationPreferences", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnStackSet.ParameterProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::CloudFormation::StackSet.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnStackSet.ParameterProperty", _IResolvable_da3f097b]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnStackSet.ParameterProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionModel")
    def permission_model(self) -> builtins.str:
        '''``AWS::CloudFormation::StackSet.PermissionModel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-permissionmodel
        '''
        return typing.cast(builtins.str, jsii.get(self, "permissionModel"))

    @permission_model.setter
    def permission_model(self, value: builtins.str) -> None:
        jsii.set(self, "permissionModel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackInstancesGroup")
    def stack_instances_group(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnStackSet.StackInstancesProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::CloudFormation::StackSet.StackInstancesGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stackinstancesgroup
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnStackSet.StackInstancesProperty", _IResolvable_da3f097b]]]], jsii.get(self, "stackInstancesGroup"))

    @stack_instances_group.setter
    def stack_instances_group(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnStackSet.StackInstancesProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "stackInstancesGroup", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackSetName")
    def stack_set_name(self) -> builtins.str:
        '''``AWS::CloudFormation::StackSet.StackSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stacksetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackSetName"))

    @stack_set_name.setter
    def stack_set_name(self, value: builtins.str) -> None:
        jsii.set(self, "stackSetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::CloudFormation::StackSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.TemplateBody``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templatebody
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateBody", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templateurl
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateUrl", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.AutoDeploymentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "retain_stacks_on_account_removal": "retainStacksOnAccountRemoval",
        },
    )
    class AutoDeploymentProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param enabled: ``CfnStackSet.AutoDeploymentProperty.Enabled``.
            :param retain_stacks_on_account_removal: ``CfnStackSet.AutoDeploymentProperty.RetainStacksOnAccountRemoval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                auto_deployment_property = cloudformation.CfnStackSet.AutoDeploymentProperty(
                    enabled=False,
                    retain_stacks_on_account_removal=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if retain_stacks_on_account_removal is not None:
                self._values["retain_stacks_on_account_removal"] = retain_stacks_on_account_removal

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnStackSet.AutoDeploymentProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def retain_stacks_on_account_removal(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnStackSet.AutoDeploymentProperty.RetainStacksOnAccountRemoval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-retainstacksonaccountremoval
            '''
            result = self._values.get("retain_stacks_on_account_removal")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoDeploymentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.DeploymentTargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "accounts": "accounts",
            "organizational_unit_ids": "organizationalUnitIds",
        },
    )
    class DeploymentTargetsProperty:
        def __init__(
            self,
            *,
            accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            organizational_unit_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param accounts: ``CfnStackSet.DeploymentTargetsProperty.Accounts``.
            :param organizational_unit_ids: ``CfnStackSet.DeploymentTargetsProperty.OrganizationalUnitIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                deployment_targets_property = cloudformation.CfnStackSet.DeploymentTargetsProperty(
                    accounts=["accounts"],
                    organizational_unit_ids=["organizationalUnitIds"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if accounts is not None:
                self._values["accounts"] = accounts
            if organizational_unit_ids is not None:
                self._values["organizational_unit_ids"] = organizational_unit_ids

        @builtins.property
        def accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnStackSet.DeploymentTargetsProperty.Accounts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-accounts
            '''
            result = self._values.get("accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def organizational_unit_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnStackSet.DeploymentTargetsProperty.OrganizationalUnitIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-organizationalunitids
            '''
            result = self._values.get("organizational_unit_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentTargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.OperationPreferencesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failure_tolerance_count": "failureToleranceCount",
            "failure_tolerance_percentage": "failureTolerancePercentage",
            "max_concurrent_count": "maxConcurrentCount",
            "max_concurrent_percentage": "maxConcurrentPercentage",
            "region_concurrency_type": "regionConcurrencyType",
            "region_order": "regionOrder",
        },
    )
    class OperationPreferencesProperty:
        def __init__(
            self,
            *,
            failure_tolerance_count: typing.Optional[jsii.Number] = None,
            failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
            max_concurrent_count: typing.Optional[jsii.Number] = None,
            max_concurrent_percentage: typing.Optional[jsii.Number] = None,
            region_concurrency_type: typing.Optional[builtins.str] = None,
            region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param failure_tolerance_count: ``CfnStackSet.OperationPreferencesProperty.FailureToleranceCount``.
            :param failure_tolerance_percentage: ``CfnStackSet.OperationPreferencesProperty.FailureTolerancePercentage``.
            :param max_concurrent_count: ``CfnStackSet.OperationPreferencesProperty.MaxConcurrentCount``.
            :param max_concurrent_percentage: ``CfnStackSet.OperationPreferencesProperty.MaxConcurrentPercentage``.
            :param region_concurrency_type: ``CfnStackSet.OperationPreferencesProperty.RegionConcurrencyType``.
            :param region_order: ``CfnStackSet.OperationPreferencesProperty.RegionOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                operation_preferences_property = cloudformation.CfnStackSet.OperationPreferencesProperty(
                    failure_tolerance_count=123,
                    failure_tolerance_percentage=123,
                    max_concurrent_count=123,
                    max_concurrent_percentage=123,
                    region_concurrency_type="regionConcurrencyType",
                    region_order=["regionOrder"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if failure_tolerance_count is not None:
                self._values["failure_tolerance_count"] = failure_tolerance_count
            if failure_tolerance_percentage is not None:
                self._values["failure_tolerance_percentage"] = failure_tolerance_percentage
            if max_concurrent_count is not None:
                self._values["max_concurrent_count"] = max_concurrent_count
            if max_concurrent_percentage is not None:
                self._values["max_concurrent_percentage"] = max_concurrent_percentage
            if region_concurrency_type is not None:
                self._values["region_concurrency_type"] = region_concurrency_type
            if region_order is not None:
                self._values["region_order"] = region_order

        @builtins.property
        def failure_tolerance_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnStackSet.OperationPreferencesProperty.FailureToleranceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-failuretolerancecount
            '''
            result = self._values.get("failure_tolerance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def failure_tolerance_percentage(self) -> typing.Optional[jsii.Number]:
            '''``CfnStackSet.OperationPreferencesProperty.FailureTolerancePercentage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-failuretolerancepercentage
            '''
            result = self._values.get("failure_tolerance_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_concurrent_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnStackSet.OperationPreferencesProperty.MaxConcurrentCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-maxconcurrentcount
            '''
            result = self._values.get("max_concurrent_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_concurrent_percentage(self) -> typing.Optional[jsii.Number]:
            '''``CfnStackSet.OperationPreferencesProperty.MaxConcurrentPercentage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-maxconcurrentpercentage
            '''
            result = self._values.get("max_concurrent_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def region_concurrency_type(self) -> typing.Optional[builtins.str]:
            '''``CfnStackSet.OperationPreferencesProperty.RegionConcurrencyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-regionconcurrencytype
            '''
            result = self._values.get("region_concurrency_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region_order(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnStackSet.OperationPreferencesProperty.RegionOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-regionorder
            '''
            result = self._values.get("region_order")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OperationPreferencesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.ParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_key": "parameterKey",
            "parameter_value": "parameterValue",
        },
    )
    class ParameterProperty:
        def __init__(
            self,
            *,
            parameter_key: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''
            :param parameter_key: ``CfnStackSet.ParameterProperty.ParameterKey``.
            :param parameter_value: ``CfnStackSet.ParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                parameter_property = cloudformation.CfnStackSet.ParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "parameter_key": parameter_key,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_key(self) -> builtins.str:
            '''``CfnStackSet.ParameterProperty.ParameterKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html#cfn-cloudformation-stackset-parameter-parameterkey
            '''
            result = self._values.get("parameter_key")
            assert result is not None, "Required property 'parameter_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''``CfnStackSet.ParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html#cfn-cloudformation-stackset-parameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.StackInstancesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deployment_targets": "deploymentTargets",
            "parameter_overrides": "parameterOverrides",
            "regions": "regions",
        },
    )
    class StackInstancesProperty:
        def __init__(
            self,
            *,
            deployment_targets: typing.Union["CfnStackSet.DeploymentTargetsProperty", _IResolvable_da3f097b],
            parameter_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnStackSet.ParameterProperty", _IResolvable_da3f097b]]]] = None,
            regions: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param deployment_targets: ``CfnStackSet.StackInstancesProperty.DeploymentTargets``.
            :param parameter_overrides: ``CfnStackSet.StackInstancesProperty.ParameterOverrides``.
            :param regions: ``CfnStackSet.StackInstancesProperty.Regions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                stack_instances_property = cloudformation.CfnStackSet.StackInstancesProperty(
                    deployment_targets=cloudformation.CfnStackSet.DeploymentTargetsProperty(
                        accounts=["accounts"],
                        organizational_unit_ids=["organizationalUnitIds"]
                    ),
                    regions=["regions"],
                
                    # the properties below are optional
                    parameter_overrides=[cloudformation.CfnStackSet.ParameterProperty(
                        parameter_key="parameterKey",
                        parameter_value="parameterValue"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "deployment_targets": deployment_targets,
                "regions": regions,
            }
            if parameter_overrides is not None:
                self._values["parameter_overrides"] = parameter_overrides

        @builtins.property
        def deployment_targets(
            self,
        ) -> typing.Union["CfnStackSet.DeploymentTargetsProperty", _IResolvable_da3f097b]:
            '''``CfnStackSet.StackInstancesProperty.DeploymentTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-deploymenttargets
            '''
            result = self._values.get("deployment_targets")
            assert result is not None, "Required property 'deployment_targets' is missing"
            return typing.cast(typing.Union["CfnStackSet.DeploymentTargetsProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def parameter_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnStackSet.ParameterProperty", _IResolvable_da3f097b]]]]:
            '''``CfnStackSet.StackInstancesProperty.ParameterOverrides``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-parameteroverrides
            '''
            result = self._values.get("parameter_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnStackSet.ParameterProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def regions(self) -> typing.List[builtins.str]:
            '''``CfnStackSet.StackInstancesProperty.Regions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-regions
            '''
            result = self._values.get("regions")
            assert result is not None, "Required property 'regions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StackInstancesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "administration_role_arn": "administrationRoleArn",
        "auto_deployment": "autoDeployment",
        "call_as": "callAs",
        "capabilities": "capabilities",
        "description": "description",
        "execution_role_name": "executionRoleName",
        "managed_execution": "managedExecution",
        "operation_preferences": "operationPreferences",
        "parameters": "parameters",
        "permission_model": "permissionModel",
        "stack_instances_group": "stackInstancesGroup",
        "stack_set_name": "stackSetName",
        "tags": "tags",
        "template_body": "templateBody",
        "template_url": "templateUrl",
    },
)
class CfnStackSetProps:
    def __init__(
        self,
        *,
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union[CfnStackSet.AutoDeploymentProperty, _IResolvable_da3f097b]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        managed_execution: typing.Any = None,
        operation_preferences: typing.Optional[typing.Union[CfnStackSet.OperationPreferencesProperty, _IResolvable_da3f097b]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnStackSet.ParameterProperty, _IResolvable_da3f097b]]]] = None,
        permission_model: builtins.str,
        stack_instances_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnStackSet.StackInstancesProperty, _IResolvable_da3f097b]]]] = None,
        stack_set_name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::StackSet``.

        :param administration_role_arn: ``AWS::CloudFormation::StackSet.AdministrationRoleARN``.
        :param auto_deployment: ``AWS::CloudFormation::StackSet.AutoDeployment``.
        :param call_as: ``AWS::CloudFormation::StackSet.CallAs``.
        :param capabilities: ``AWS::CloudFormation::StackSet.Capabilities``.
        :param description: ``AWS::CloudFormation::StackSet.Description``.
        :param execution_role_name: ``AWS::CloudFormation::StackSet.ExecutionRoleName``.
        :param managed_execution: ``AWS::CloudFormation::StackSet.ManagedExecution``.
        :param operation_preferences: ``AWS::CloudFormation::StackSet.OperationPreferences``.
        :param parameters: ``AWS::CloudFormation::StackSet.Parameters``.
        :param permission_model: ``AWS::CloudFormation::StackSet.PermissionModel``.
        :param stack_instances_group: ``AWS::CloudFormation::StackSet.StackInstancesGroup``.
        :param stack_set_name: ``AWS::CloudFormation::StackSet.StackSetName``.
        :param tags: ``AWS::CloudFormation::StackSet.Tags``.
        :param template_body: ``AWS::CloudFormation::StackSet.TemplateBody``.
        :param template_url: ``AWS::CloudFormation::StackSet.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            # managed_execution is of type object
            
            cfn_stack_set_props = cloudformation.CfnStackSetProps(
                permission_model="permissionModel",
                stack_set_name="stackSetName",
            
                # the properties below are optional
                administration_role_arn="administrationRoleArn",
                auto_deployment=cloudformation.CfnStackSet.AutoDeploymentProperty(
                    enabled=False,
                    retain_stacks_on_account_removal=False
                ),
                call_as="callAs",
                capabilities=["capabilities"],
                description="description",
                execution_role_name="executionRoleName",
                managed_execution=managed_execution,
                operation_preferences=cloudformation.CfnStackSet.OperationPreferencesProperty(
                    failure_tolerance_count=123,
                    failure_tolerance_percentage=123,
                    max_concurrent_count=123,
                    max_concurrent_percentage=123,
                    region_concurrency_type="regionConcurrencyType",
                    region_order=["regionOrder"]
                ),
                parameters=[cloudformation.CfnStackSet.ParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )],
                stack_instances_group=[cloudformation.CfnStackSet.StackInstancesProperty(
                    deployment_targets=cloudformation.CfnStackSet.DeploymentTargetsProperty(
                        accounts=["accounts"],
                        organizational_unit_ids=["organizationalUnitIds"]
                    ),
                    regions=["regions"],
            
                    # the properties below are optional
                    parameter_overrides=[cloudformation.CfnStackSet.ParameterProperty(
                        parameter_key="parameterKey",
                        parameter_value="parameterValue"
                    )]
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                template_body="templateBody",
                template_url="templateUrl"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "permission_model": permission_model,
            "stack_set_name": stack_set_name,
        }
        if administration_role_arn is not None:
            self._values["administration_role_arn"] = administration_role_arn
        if auto_deployment is not None:
            self._values["auto_deployment"] = auto_deployment
        if call_as is not None:
            self._values["call_as"] = call_as
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if description is not None:
            self._values["description"] = description
        if execution_role_name is not None:
            self._values["execution_role_name"] = execution_role_name
        if managed_execution is not None:
            self._values["managed_execution"] = managed_execution
        if operation_preferences is not None:
            self._values["operation_preferences"] = operation_preferences
        if parameters is not None:
            self._values["parameters"] = parameters
        if stack_instances_group is not None:
            self._values["stack_instances_group"] = stack_instances_group
        if tags is not None:
            self._values["tags"] = tags
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_url is not None:
            self._values["template_url"] = template_url

    @builtins.property
    def administration_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.AdministrationRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-administrationrolearn
        '''
        result = self._values.get("administration_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_deployment(
        self,
    ) -> typing.Optional[typing.Union[CfnStackSet.AutoDeploymentProperty, _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::StackSet.AutoDeployment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-autodeployment
        '''
        result = self._values.get("auto_deployment")
        return typing.cast(typing.Optional[typing.Union[CfnStackSet.AutoDeploymentProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def call_as(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.CallAs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-callas
        '''
        result = self._values.get("call_as")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CloudFormation::StackSet.Capabilities``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-capabilities
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.ExecutionRoleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-executionrolename
        '''
        result = self._values.get("execution_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_execution(self) -> typing.Any:
        '''``AWS::CloudFormation::StackSet.ManagedExecution``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-managedexecution
        '''
        result = self._values.get("managed_execution")
        return typing.cast(typing.Any, result)

    @builtins.property
    def operation_preferences(
        self,
    ) -> typing.Optional[typing.Union[CfnStackSet.OperationPreferencesProperty, _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::StackSet.OperationPreferences``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-operationpreferences
        '''
        result = self._values.get("operation_preferences")
        return typing.cast(typing.Optional[typing.Union[CfnStackSet.OperationPreferencesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnStackSet.ParameterProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::CloudFormation::StackSet.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnStackSet.ParameterProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def permission_model(self) -> builtins.str:
        '''``AWS::CloudFormation::StackSet.PermissionModel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-permissionmodel
        '''
        result = self._values.get("permission_model")
        assert result is not None, "Required property 'permission_model' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_instances_group(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnStackSet.StackInstancesProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::CloudFormation::StackSet.StackInstancesGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stackinstancesgroup
        '''
        result = self._values.get("stack_instances_group")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnStackSet.StackInstancesProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def stack_set_name(self) -> builtins.str:
        '''``AWS::CloudFormation::StackSet.StackSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stacksetname
        '''
        result = self._values.get("stack_set_name")
        assert result is not None, "Required property 'stack_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::CloudFormation::StackSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.TemplateBody``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templatebody
        '''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templateurl
        '''
        result = self._values.get("template_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTypeActivation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnTypeActivation",
):
    '''A CloudFormation ``AWS::CloudFormation::TypeActivation``.

    :cloudformationResource: AWS::CloudFormation::TypeActivation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_type_activation = cloudformation.CfnTypeActivation(self, "MyCfnTypeActivation",
            auto_update=False,
            execution_role_arn="executionRoleArn",
            logging_config=cloudformation.CfnTypeActivation.LoggingConfigProperty(
                log_group_name="logGroupName",
                log_role_arn="logRoleArn"
            ),
            major_version="majorVersion",
            public_type_arn="publicTypeArn",
            publisher_id="publisherId",
            type="type",
            type_name="typeName",
            type_name_alias="typeNameAlias",
            version_bump="versionBump"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        auto_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union["CfnTypeActivation.LoggingConfigProperty", _IResolvable_da3f097b]] = None,
        major_version: typing.Optional[builtins.str] = None,
        public_type_arn: typing.Optional[builtins.str] = None,
        publisher_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        type_name_alias: typing.Optional[builtins.str] = None,
        version_bump: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::TypeActivation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param auto_update: ``AWS::CloudFormation::TypeActivation.AutoUpdate``.
        :param execution_role_arn: ``AWS::CloudFormation::TypeActivation.ExecutionRoleArn``.
        :param logging_config: ``AWS::CloudFormation::TypeActivation.LoggingConfig``.
        :param major_version: ``AWS::CloudFormation::TypeActivation.MajorVersion``.
        :param public_type_arn: ``AWS::CloudFormation::TypeActivation.PublicTypeArn``.
        :param publisher_id: ``AWS::CloudFormation::TypeActivation.PublisherId``.
        :param type: ``AWS::CloudFormation::TypeActivation.Type``.
        :param type_name: ``AWS::CloudFormation::TypeActivation.TypeName``.
        :param type_name_alias: ``AWS::CloudFormation::TypeActivation.TypeNameAlias``.
        :param version_bump: ``AWS::CloudFormation::TypeActivation.VersionBump``.
        '''
        props = CfnTypeActivationProps(
            auto_update=auto_update,
            execution_role_arn=execution_role_arn,
            logging_config=logging_config,
            major_version=major_version,
            public_type_arn=public_type_arn,
            publisher_id=publisher_id,
            type=type,
            type_name=type_name,
            type_name_alias=type_name_alias,
            version_bump=version_bump,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoUpdate")
    def auto_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::TypeActivation.AutoUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-autoupdate
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoUpdate"))

    @auto_update.setter
    def auto_update(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "autoUpdate", value)

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
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-executionrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union["CfnTypeActivation.LoggingConfigProperty", _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::TypeActivation.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-loggingconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTypeActivation.LoggingConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "loggingConfig"))

    @logging_config.setter
    def logging_config(
        self,
        value: typing.Optional[typing.Union["CfnTypeActivation.LoggingConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "loggingConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="majorVersion")
    def major_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.MajorVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-majorversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "majorVersion"))

    @major_version.setter
    def major_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "majorVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publicTypeArn")
    def public_type_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.PublicTypeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publictypearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicTypeArn"))

    @public_type_arn.setter
    def public_type_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "publicTypeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publisherId")
    def publisher_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.PublisherId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publisherid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherId"))

    @publisher_id.setter
    def publisher_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "publisherId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeNameAlias")
    def type_name_alias(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.TypeNameAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typenamealias
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameAlias"))

    @type_name_alias.setter
    def type_name_alias(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeNameAlias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionBump")
    def version_bump(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.VersionBump``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-versionbump
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionBump"))

    @version_bump.setter
    def version_bump(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionBump", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnTypeActivation.LoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "log_role_arn": "logRoleArn"},
    )
    class LoggingConfigProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
            log_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group_name: ``CfnTypeActivation.LoggingConfigProperty.LogGroupName``.
            :param log_role_arn: ``CfnTypeActivation.LoggingConfigProperty.LogRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                logging_config_property = cloudformation.CfnTypeActivation.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_role_arn is not None:
                self._values["log_role_arn"] = log_role_arn

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''``CfnTypeActivation.LoggingConfigProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html#cfn-cloudformation-typeactivation-loggingconfig-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnTypeActivation.LoggingConfigProperty.LogRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html#cfn-cloudformation-typeactivation-loggingconfig-logrolearn
            '''
            result = self._values.get("log_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnTypeActivationProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_update": "autoUpdate",
        "execution_role_arn": "executionRoleArn",
        "logging_config": "loggingConfig",
        "major_version": "majorVersion",
        "public_type_arn": "publicTypeArn",
        "publisher_id": "publisherId",
        "type": "type",
        "type_name": "typeName",
        "type_name_alias": "typeNameAlias",
        "version_bump": "versionBump",
    },
)
class CfnTypeActivationProps:
    def __init__(
        self,
        *,
        auto_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[CfnTypeActivation.LoggingConfigProperty, _IResolvable_da3f097b]] = None,
        major_version: typing.Optional[builtins.str] = None,
        public_type_arn: typing.Optional[builtins.str] = None,
        publisher_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        type_name_alias: typing.Optional[builtins.str] = None,
        version_bump: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::TypeActivation``.

        :param auto_update: ``AWS::CloudFormation::TypeActivation.AutoUpdate``.
        :param execution_role_arn: ``AWS::CloudFormation::TypeActivation.ExecutionRoleArn``.
        :param logging_config: ``AWS::CloudFormation::TypeActivation.LoggingConfig``.
        :param major_version: ``AWS::CloudFormation::TypeActivation.MajorVersion``.
        :param public_type_arn: ``AWS::CloudFormation::TypeActivation.PublicTypeArn``.
        :param publisher_id: ``AWS::CloudFormation::TypeActivation.PublisherId``.
        :param type: ``AWS::CloudFormation::TypeActivation.Type``.
        :param type_name: ``AWS::CloudFormation::TypeActivation.TypeName``.
        :param type_name_alias: ``AWS::CloudFormation::TypeActivation.TypeNameAlias``.
        :param version_bump: ``AWS::CloudFormation::TypeActivation.VersionBump``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_type_activation_props = cloudformation.CfnTypeActivationProps(
                auto_update=False,
                execution_role_arn="executionRoleArn",
                logging_config=cloudformation.CfnTypeActivation.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                ),
                major_version="majorVersion",
                public_type_arn="publicTypeArn",
                publisher_id="publisherId",
                type="type",
                type_name="typeName",
                type_name_alias="typeNameAlias",
                version_bump="versionBump"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_update is not None:
            self._values["auto_update"] = auto_update
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if major_version is not None:
            self._values["major_version"] = major_version
        if public_type_arn is not None:
            self._values["public_type_arn"] = public_type_arn
        if publisher_id is not None:
            self._values["publisher_id"] = publisher_id
        if type is not None:
            self._values["type"] = type
        if type_name is not None:
            self._values["type_name"] = type_name
        if type_name_alias is not None:
            self._values["type_name_alias"] = type_name_alias
        if version_bump is not None:
            self._values["version_bump"] = version_bump

    @builtins.property
    def auto_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::TypeActivation.AutoUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-autoupdate
        '''
        result = self._values.get("auto_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[CfnTypeActivation.LoggingConfigProperty, _IResolvable_da3f097b]]:
        '''``AWS::CloudFormation::TypeActivation.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-loggingconfig
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional[typing.Union[CfnTypeActivation.LoggingConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def major_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.MajorVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-majorversion
        '''
        result = self._values.get("major_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_type_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.PublicTypeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publictypearn
        '''
        result = self._values.get("public_type_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publisher_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.PublisherId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publisherid
        '''
        result = self._values.get("publisher_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name_alias(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.TypeNameAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typenamealias
        '''
        result = self._values.get("type_name_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_bump(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.VersionBump``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-versionbump
        '''
        result = self._values.get("version_bump")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTypeActivationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnWaitCondition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnWaitCondition",
):
    '''A CloudFormation ``AWS::CloudFormation::WaitCondition``.

    :cloudformationResource: AWS::CloudFormation::WaitCondition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_wait_condition = cloudformation.CfnWaitCondition(self, "MyCfnWaitCondition",
            count=123,
            handle="handle",
            timeout="timeout"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        count: typing.Optional[jsii.Number] = None,
        handle: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::WaitCondition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param count: ``AWS::CloudFormation::WaitCondition.Count``.
        :param handle: ``AWS::CloudFormation::WaitCondition.Handle``.
        :param timeout: ``AWS::CloudFormation::WaitCondition.Timeout``.
        '''
        props = CfnWaitConditionProps(count=count, handle=handle, timeout=timeout)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
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
    @jsii.member(jsii_name="attrData")
    def attr_data(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Data
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrData"))

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
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CloudFormation::WaitCondition.Count``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "count"))

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "count", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="handle")
    def handle(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::WaitCondition.Handle``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handle"))

    @handle.setter
    def handle(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "handle", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::WaitCondition.Timeout``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "timeout", value)


@jsii.implements(_IInspectable_c2943556)
class CfnWaitConditionHandle(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnWaitConditionHandle",
):
    '''A CloudFormation ``AWS::CloudFormation::WaitConditionHandle``.

    :cloudformationResource: AWS::CloudFormation::WaitConditionHandle
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_wait_condition_handle = cloudformation.CfnWaitConditionHandle(self, "MyCfnWaitConditionHandle")
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''Create a new ``AWS::CloudFormation::WaitConditionHandle``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        '''
        jsii.create(self.__class__, self, [scope, id])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnWaitConditionProps",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "handle": "handle", "timeout": "timeout"},
)
class CfnWaitConditionProps:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        handle: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::WaitCondition``.

        :param count: ``AWS::CloudFormation::WaitCondition.Count``.
        :param handle: ``AWS::CloudFormation::WaitCondition.Handle``.
        :param timeout: ``AWS::CloudFormation::WaitCondition.Timeout``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_wait_condition_props = cloudformation.CfnWaitConditionProps(
                count=123,
                handle="handle",
                timeout="timeout"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if handle is not None:
            self._values["handle"] = handle
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CloudFormation::WaitCondition.Count``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def handle(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::WaitCondition.Handle``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle
        '''
        result = self._values.get("handle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::WaitCondition.Timeout``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWaitConditionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCustomResource",
    "CfnCustomResourceProps",
    "CfnMacro",
    "CfnMacroProps",
    "CfnModuleDefaultVersion",
    "CfnModuleDefaultVersionProps",
    "CfnModuleVersion",
    "CfnModuleVersionProps",
    "CfnPublicTypeVersion",
    "CfnPublicTypeVersionProps",
    "CfnPublisher",
    "CfnPublisherProps",
    "CfnResourceDefaultVersion",
    "CfnResourceDefaultVersionProps",
    "CfnResourceVersion",
    "CfnResourceVersionProps",
    "CfnStack",
    "CfnStackProps",
    "CfnStackSet",
    "CfnStackSetProps",
    "CfnTypeActivation",
    "CfnTypeActivationProps",
    "CfnWaitCondition",
    "CfnWaitConditionHandle",
    "CfnWaitConditionProps",
]

publication.publish()
