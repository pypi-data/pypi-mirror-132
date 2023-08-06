'''
# AWS::IoTCoreDeviceAdvisor Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotcoredeviceadvisor as iotcoredeviceadvisor
```

> The construct library for this service is in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package named:
>
> ```
> @aws-cdk/aws-iotcoredeviceadvisor-alpha
> ```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTCoreDeviceAdvisor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTCoreDeviceAdvisor.html).

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

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnSuiteDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotcoredeviceadvisor.CfnSuiteDefinition",
):
    '''A CloudFormation ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition``.

    :cloudformationResource: AWS::IoTCoreDeviceAdvisor::SuiteDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotcoredeviceadvisor as iotcoredeviceadvisor
        
        # suite_definition_configuration is of type object
        
        cfn_suite_definition = iotcoredeviceadvisor.CfnSuiteDefinition(self, "MyCfnSuiteDefinition",
            suite_definition_configuration=suite_definition_configuration,
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        suite_definition_configuration: typing.Any,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param suite_definition_configuration: ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.SuiteDefinitionConfiguration``.
        :param tags: ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.Tags``.
        '''
        props = CfnSuiteDefinitionProps(
            suite_definition_configuration=suite_definition_configuration, tags=tags
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
    @jsii.member(jsii_name="attrSuiteDefinitionArn")
    def attr_suite_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SuiteDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSuiteDefinitionId")
    def attr_suite_definition_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SuiteDefinitionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSuiteDefinitionVersion")
    def attr_suite_definition_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: SuiteDefinitionVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSuiteDefinitionVersion"))

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
    @jsii.member(jsii_name="suiteDefinitionConfiguration")
    def suite_definition_configuration(self) -> typing.Any:
        '''``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.SuiteDefinitionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        '''
        return typing.cast(typing.Any, jsii.get(self, "suiteDefinitionConfiguration"))

    @suite_definition_configuration.setter
    def suite_definition_configuration(self, value: typing.Any) -> None:
        jsii.set(self, "suiteDefinitionConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotcoredeviceadvisor.CfnSuiteDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "suite_definition_configuration": "suiteDefinitionConfiguration",
        "tags": "tags",
    },
)
class CfnSuiteDefinitionProps:
    def __init__(
        self,
        *,
        suite_definition_configuration: typing.Any,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition``.

        :param suite_definition_configuration: ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.SuiteDefinitionConfiguration``.
        :param tags: ``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotcoredeviceadvisor as iotcoredeviceadvisor
            
            # suite_definition_configuration is of type object
            
            cfn_suite_definition_props = iotcoredeviceadvisor.CfnSuiteDefinitionProps(
                suite_definition_configuration=suite_definition_configuration,
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "suite_definition_configuration": suite_definition_configuration,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def suite_definition_configuration(self) -> typing.Any:
        '''``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.SuiteDefinitionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        '''
        result = self._values.get("suite_definition_configuration")
        assert result is not None, "Required property 'suite_definition_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::IoTCoreDeviceAdvisor::SuiteDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSuiteDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSuiteDefinition",
    "CfnSuiteDefinitionProps",
]

publication.publish()
