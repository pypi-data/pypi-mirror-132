'''
# AWS::SSMIncidents Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ssmincidents as ssmincidents
```

> The construct library for this service is in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package named:
>
> ```
> @aws-cdk/aws-ssmincidents-alpha
> ```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSMIncidents](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMIncidents.html).

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
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnReplicationSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmincidents.CfnReplicationSet",
):
    '''A CloudFormation ``AWS::SSMIncidents::ReplicationSet``.

    :cloudformationResource: AWS::SSMIncidents::ReplicationSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmincidents as ssmincidents
        
        cfn_replication_set = ssmincidents.CfnReplicationSet(self, "MyCfnReplicationSet",
            regions=[ssmincidents.CfnReplicationSet.ReplicationRegionProperty(
                region_configuration=ssmincidents.CfnReplicationSet.RegionConfigurationProperty(
                    sse_kms_key_id="sseKmsKeyId"
                ),
                region_name="regionName"
            )],
        
            # the properties below are optional
            deletion_protected=False
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        deletion_protected: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        regions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnReplicationSet.ReplicationRegionProperty", _IResolvable_da3f097b]]],
    ) -> None:
        '''Create a new ``AWS::SSMIncidents::ReplicationSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param deletion_protected: ``AWS::SSMIncidents::ReplicationSet.DeletionProtected``.
        :param regions: ``AWS::SSMIncidents::ReplicationSet.Regions``.
        '''
        props = CfnReplicationSetProps(
            deletion_protected=deletion_protected, regions=regions
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
    @jsii.member(jsii_name="deletionProtected")
    def deletion_protected(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::SSMIncidents::ReplicationSet.DeletionProtected``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deletionProtected"))

    @deletion_protected.setter
    def deletion_protected(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "deletionProtected", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="regions")
    def regions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnReplicationSet.ReplicationRegionProperty", _IResolvable_da3f097b]]]:
        '''``AWS::SSMIncidents::ReplicationSet.Regions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnReplicationSet.ReplicationRegionProperty", _IResolvable_da3f097b]]], jsii.get(self, "regions"))

    @regions.setter
    def regions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnReplicationSet.ReplicationRegionProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "regions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmincidents.CfnReplicationSet.RegionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"sse_kms_key_id": "sseKmsKeyId"},
    )
    class RegionConfigurationProperty:
        def __init__(self, *, sse_kms_key_id: builtins.str) -> None:
            '''
            :param sse_kms_key_id: ``CfnReplicationSet.RegionConfigurationProperty.SseKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-regionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmincidents as ssmincidents
                
                region_configuration_property = ssmincidents.CfnReplicationSet.RegionConfigurationProperty(
                    sse_kms_key_id="sseKmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "sse_kms_key_id": sse_kms_key_id,
            }

        @builtins.property
        def sse_kms_key_id(self) -> builtins.str:
            '''``CfnReplicationSet.RegionConfigurationProperty.SseKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-regionconfiguration.html#cfn-ssmincidents-replicationset-regionconfiguration-ssekmskeyid
            '''
            result = self._values.get("sse_kms_key_id")
            assert result is not None, "Required property 'sse_kms_key_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmincidents.CfnReplicationSet.ReplicationRegionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region_configuration": "regionConfiguration",
            "region_name": "regionName",
        },
    )
    class ReplicationRegionProperty:
        def __init__(
            self,
            *,
            region_configuration: typing.Optional[typing.Union["CfnReplicationSet.RegionConfigurationProperty", _IResolvable_da3f097b]] = None,
            region_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param region_configuration: ``CfnReplicationSet.ReplicationRegionProperty.RegionConfiguration``.
            :param region_name: ``CfnReplicationSet.ReplicationRegionProperty.RegionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmincidents as ssmincidents
                
                replication_region_property = ssmincidents.CfnReplicationSet.ReplicationRegionProperty(
                    region_configuration=ssmincidents.CfnReplicationSet.RegionConfigurationProperty(
                        sse_kms_key_id="sseKmsKeyId"
                    ),
                    region_name="regionName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if region_configuration is not None:
                self._values["region_configuration"] = region_configuration
            if region_name is not None:
                self._values["region_name"] = region_name

        @builtins.property
        def region_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnReplicationSet.RegionConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnReplicationSet.ReplicationRegionProperty.RegionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html#cfn-ssmincidents-replicationset-replicationregion-regionconfiguration
            '''
            result = self._values.get("region_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnReplicationSet.RegionConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def region_name(self) -> typing.Optional[builtins.str]:
            '''``CfnReplicationSet.ReplicationRegionProperty.RegionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html#cfn-ssmincidents-replicationset-replicationregion-regionname
            '''
            result = self._values.get("region_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicationRegionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmincidents.CfnReplicationSetProps",
    jsii_struct_bases=[],
    name_mapping={"deletion_protected": "deletionProtected", "regions": "regions"},
)
class CfnReplicationSetProps:
    def __init__(
        self,
        *,
        deletion_protected: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        regions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnReplicationSet.ReplicationRegionProperty, _IResolvable_da3f097b]]],
    ) -> None:
        '''Properties for defining a ``AWS::SSMIncidents::ReplicationSet``.

        :param deletion_protected: ``AWS::SSMIncidents::ReplicationSet.DeletionProtected``.
        :param regions: ``AWS::SSMIncidents::ReplicationSet.Regions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmincidents as ssmincidents
            
            cfn_replication_set_props = ssmincidents.CfnReplicationSetProps(
                regions=[ssmincidents.CfnReplicationSet.ReplicationRegionProperty(
                    region_configuration=ssmincidents.CfnReplicationSet.RegionConfigurationProperty(
                        sse_kms_key_id="sseKmsKeyId"
                    ),
                    region_name="regionName"
                )],
            
                # the properties below are optional
                deletion_protected=False
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "regions": regions,
        }
        if deletion_protected is not None:
            self._values["deletion_protected"] = deletion_protected

    @builtins.property
    def deletion_protected(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::SSMIncidents::ReplicationSet.DeletionProtected``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
        '''
        result = self._values.get("deletion_protected")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def regions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnReplicationSet.ReplicationRegionProperty, _IResolvable_da3f097b]]]:
        '''``AWS::SSMIncidents::ReplicationSet.Regions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
        '''
        result = self._values.get("regions")
        assert result is not None, "Required property 'regions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnReplicationSet.ReplicationRegionProperty, _IResolvable_da3f097b]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResponsePlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmincidents.CfnResponsePlan",
):
    '''A CloudFormation ``AWS::SSMIncidents::ResponsePlan``.

    :cloudformationResource: AWS::SSMIncidents::ResponsePlan
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmincidents as ssmincidents
        
        cfn_response_plan = ssmincidents.CfnResponsePlan(self, "MyCfnResponsePlan",
            incident_template=ssmincidents.CfnResponsePlan.IncidentTemplateProperty(
                impact=123,
                title="title",
        
                # the properties below are optional
                dedupe_string="dedupeString",
                notification_targets=[ssmincidents.CfnResponsePlan.NotificationTargetItemProperty(
                    sns_topic_arn="snsTopicArn"
                )],
                summary="summary"
            ),
            name="name",
        
            # the properties below are optional
            actions=[ssmincidents.CfnResponsePlan.ActionProperty(
                ssm_automation=ssmincidents.CfnResponsePlan.SsmAutomationProperty(
                    document_name="documentName",
                    role_arn="roleArn",
        
                    # the properties below are optional
                    document_version="documentVersion",
                    parameters=[ssmincidents.CfnResponsePlan.SsmParameterProperty(
                        key="key",
                        values=["values"]
                    )],
                    target_account="targetAccount"
                )
            )],
            chat_channel=ssmincidents.CfnResponsePlan.ChatChannelProperty(
                chatbot_sns=["chatbotSns"]
            ),
            display_name="displayName",
            engagements=["engagements"],
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
        actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnResponsePlan.ActionProperty", _IResolvable_da3f097b]]]] = None,
        chat_channel: typing.Optional[typing.Union["CfnResponsePlan.ChatChannelProperty", _IResolvable_da3f097b]] = None,
        display_name: typing.Optional[builtins.str] = None,
        engagements: typing.Optional[typing.Sequence[builtins.str]] = None,
        incident_template: typing.Union["CfnResponsePlan.IncidentTemplateProperty", _IResolvable_da3f097b],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::SSMIncidents::ResponsePlan``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param actions: ``AWS::SSMIncidents::ResponsePlan.Actions``.
        :param chat_channel: ``AWS::SSMIncidents::ResponsePlan.ChatChannel``.
        :param display_name: ``AWS::SSMIncidents::ResponsePlan.DisplayName``.
        :param engagements: ``AWS::SSMIncidents::ResponsePlan.Engagements``.
        :param incident_template: ``AWS::SSMIncidents::ResponsePlan.IncidentTemplate``.
        :param name: ``AWS::SSMIncidents::ResponsePlan.Name``.
        :param tags: ``AWS::SSMIncidents::ResponsePlan.Tags``.
        '''
        props = CfnResponsePlanProps(
            actions=actions,
            chat_channel=chat_channel,
            display_name=display_name,
            engagements=engagements,
            incident_template=incident_template,
            name=name,
            tags=tags,
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
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnResponsePlan.ActionProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::SSMIncidents::ResponsePlan.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-actions
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnResponsePlan.ActionProperty", _IResolvable_da3f097b]]]], jsii.get(self, "actions"))

    @actions.setter
    def actions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnResponsePlan.ActionProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "actions", value)

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
    @jsii.member(jsii_name="chatChannel")
    def chat_channel(
        self,
    ) -> typing.Optional[typing.Union["CfnResponsePlan.ChatChannelProperty", _IResolvable_da3f097b]]:
        '''``AWS::SSMIncidents::ResponsePlan.ChatChannel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-chatchannel
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResponsePlan.ChatChannelProperty", _IResolvable_da3f097b]], jsii.get(self, "chatChannel"))

    @chat_channel.setter
    def chat_channel(
        self,
        value: typing.Optional[typing.Union["CfnResponsePlan.ChatChannelProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "chatChannel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSMIncidents::ResponsePlan.DisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-displayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "displayName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engagements")
    def engagements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSMIncidents::ResponsePlan.Engagements``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-engagements
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "engagements"))

    @engagements.setter
    def engagements(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "engagements", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="incidentTemplate")
    def incident_template(
        self,
    ) -> typing.Union["CfnResponsePlan.IncidentTemplateProperty", _IResolvable_da3f097b]:
        '''``AWS::SSMIncidents::ResponsePlan.IncidentTemplate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-incidenttemplate
        '''
        return typing.cast(typing.Union["CfnResponsePlan.IncidentTemplateProperty", _IResolvable_da3f097b], jsii.get(self, "incidentTemplate"))

    @incident_template.setter
    def incident_template(
        self,
        value: typing.Union["CfnResponsePlan.IncidentTemplateProperty", _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "incidentTemplate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::SSMIncidents::ResponsePlan.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::SSMIncidents::ResponsePlan.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmincidents.CfnResponsePlan.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"ssm_automation": "ssmAutomation"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            ssm_automation: typing.Optional[typing.Union["CfnResponsePlan.SsmAutomationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param ssm_automation: ``CfnResponsePlan.ActionProperty.SsmAutomation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmincidents as ssmincidents
                
                action_property = ssmincidents.CfnResponsePlan.ActionProperty(
                    ssm_automation=ssmincidents.CfnResponsePlan.SsmAutomationProperty(
                        document_name="documentName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        document_version="documentVersion",
                        parameters=[ssmincidents.CfnResponsePlan.SsmParameterProperty(
                            key="key",
                            values=["values"]
                        )],
                        target_account="targetAccount"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ssm_automation is not None:
                self._values["ssm_automation"] = ssm_automation

        @builtins.property
        def ssm_automation(
            self,
        ) -> typing.Optional[typing.Union["CfnResponsePlan.SsmAutomationProperty", _IResolvable_da3f097b]]:
            '''``CfnResponsePlan.ActionProperty.SsmAutomation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-action.html#cfn-ssmincidents-responseplan-action-ssmautomation
            '''
            result = self._values.get("ssm_automation")
            return typing.cast(typing.Optional[typing.Union["CfnResponsePlan.SsmAutomationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmincidents.CfnResponsePlan.ChatChannelProperty",
        jsii_struct_bases=[],
        name_mapping={"chatbot_sns": "chatbotSns"},
    )
    class ChatChannelProperty:
        def __init__(
            self,
            *,
            chatbot_sns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param chatbot_sns: ``CfnResponsePlan.ChatChannelProperty.ChatbotSns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-chatchannel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmincidents as ssmincidents
                
                chat_channel_property = ssmincidents.CfnResponsePlan.ChatChannelProperty(
                    chatbot_sns=["chatbotSns"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if chatbot_sns is not None:
                self._values["chatbot_sns"] = chatbot_sns

        @builtins.property
        def chatbot_sns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnResponsePlan.ChatChannelProperty.ChatbotSns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-chatchannel.html#cfn-ssmincidents-responseplan-chatchannel-chatbotsns
            '''
            result = self._values.get("chatbot_sns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChatChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmincidents.CfnResponsePlan.IncidentTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dedupe_string": "dedupeString",
            "impact": "impact",
            "notification_targets": "notificationTargets",
            "summary": "summary",
            "title": "title",
        },
    )
    class IncidentTemplateProperty:
        def __init__(
            self,
            *,
            dedupe_string: typing.Optional[builtins.str] = None,
            impact: jsii.Number,
            notification_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnResponsePlan.NotificationTargetItemProperty", _IResolvable_da3f097b]]]] = None,
            summary: typing.Optional[builtins.str] = None,
            title: builtins.str,
        ) -> None:
            '''
            :param dedupe_string: ``CfnResponsePlan.IncidentTemplateProperty.DedupeString``.
            :param impact: ``CfnResponsePlan.IncidentTemplateProperty.Impact``.
            :param notification_targets: ``CfnResponsePlan.IncidentTemplateProperty.NotificationTargets``.
            :param summary: ``CfnResponsePlan.IncidentTemplateProperty.Summary``.
            :param title: ``CfnResponsePlan.IncidentTemplateProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmincidents as ssmincidents
                
                incident_template_property = ssmincidents.CfnResponsePlan.IncidentTemplateProperty(
                    impact=123,
                    title="title",
                
                    # the properties below are optional
                    dedupe_string="dedupeString",
                    notification_targets=[ssmincidents.CfnResponsePlan.NotificationTargetItemProperty(
                        sns_topic_arn="snsTopicArn"
                    )],
                    summary="summary"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "impact": impact,
                "title": title,
            }
            if dedupe_string is not None:
                self._values["dedupe_string"] = dedupe_string
            if notification_targets is not None:
                self._values["notification_targets"] = notification_targets
            if summary is not None:
                self._values["summary"] = summary

        @builtins.property
        def dedupe_string(self) -> typing.Optional[builtins.str]:
            '''``CfnResponsePlan.IncidentTemplateProperty.DedupeString``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-dedupestring
            '''
            result = self._values.get("dedupe_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def impact(self) -> jsii.Number:
            '''``CfnResponsePlan.IncidentTemplateProperty.Impact``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-impact
            '''
            result = self._values.get("impact")
            assert result is not None, "Required property 'impact' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def notification_targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnResponsePlan.NotificationTargetItemProperty", _IResolvable_da3f097b]]]]:
            '''``CfnResponsePlan.IncidentTemplateProperty.NotificationTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-notificationtargets
            '''
            result = self._values.get("notification_targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnResponsePlan.NotificationTargetItemProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def summary(self) -> typing.Optional[builtins.str]:
            '''``CfnResponsePlan.IncidentTemplateProperty.Summary``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-summary
            '''
            result = self._values.get("summary")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> builtins.str:
            '''``CfnResponsePlan.IncidentTemplateProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-title
            '''
            result = self._values.get("title")
            assert result is not None, "Required property 'title' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IncidentTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmincidents.CfnResponsePlan.NotificationTargetItemProperty",
        jsii_struct_bases=[],
        name_mapping={"sns_topic_arn": "snsTopicArn"},
    )
    class NotificationTargetItemProperty:
        def __init__(
            self,
            *,
            sns_topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param sns_topic_arn: ``CfnResponsePlan.NotificationTargetItemProperty.SnsTopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-notificationtargetitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmincidents as ssmincidents
                
                notification_target_item_property = ssmincidents.CfnResponsePlan.NotificationTargetItemProperty(
                    sns_topic_arn="snsTopicArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if sns_topic_arn is not None:
                self._values["sns_topic_arn"] = sns_topic_arn

        @builtins.property
        def sns_topic_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnResponsePlan.NotificationTargetItemProperty.SnsTopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-notificationtargetitem.html#cfn-ssmincidents-responseplan-notificationtargetitem-snstopicarn
            '''
            result = self._values.get("sns_topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationTargetItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmincidents.CfnResponsePlan.SsmAutomationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_name": "documentName",
            "document_version": "documentVersion",
            "parameters": "parameters",
            "role_arn": "roleArn",
            "target_account": "targetAccount",
        },
    )
    class SsmAutomationProperty:
        def __init__(
            self,
            *,
            document_name: builtins.str,
            document_version: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnResponsePlan.SsmParameterProperty", _IResolvable_da3f097b]]]] = None,
            role_arn: builtins.str,
            target_account: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param document_name: ``CfnResponsePlan.SsmAutomationProperty.DocumentName``.
            :param document_version: ``CfnResponsePlan.SsmAutomationProperty.DocumentVersion``.
            :param parameters: ``CfnResponsePlan.SsmAutomationProperty.Parameters``.
            :param role_arn: ``CfnResponsePlan.SsmAutomationProperty.RoleArn``.
            :param target_account: ``CfnResponsePlan.SsmAutomationProperty.TargetAccount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmincidents as ssmincidents
                
                ssm_automation_property = ssmincidents.CfnResponsePlan.SsmAutomationProperty(
                    document_name="documentName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    document_version="documentVersion",
                    parameters=[ssmincidents.CfnResponsePlan.SsmParameterProperty(
                        key="key",
                        values=["values"]
                    )],
                    target_account="targetAccount"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "document_name": document_name,
                "role_arn": role_arn,
            }
            if document_version is not None:
                self._values["document_version"] = document_version
            if parameters is not None:
                self._values["parameters"] = parameters
            if target_account is not None:
                self._values["target_account"] = target_account

        @builtins.property
        def document_name(self) -> builtins.str:
            '''``CfnResponsePlan.SsmAutomationProperty.DocumentName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-documentname
            '''
            result = self._values.get("document_name")
            assert result is not None, "Required property 'document_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''``CfnResponsePlan.SsmAutomationProperty.DocumentVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnResponsePlan.SsmParameterProperty", _IResolvable_da3f097b]]]]:
            '''``CfnResponsePlan.SsmAutomationProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnResponsePlan.SsmParameterProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnResponsePlan.SsmAutomationProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_account(self) -> typing.Optional[builtins.str]:
            '''``CfnResponsePlan.SsmAutomationProperty.TargetAccount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-targetaccount
            '''
            result = self._values.get("target_account")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsmAutomationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmincidents.CfnResponsePlan.SsmParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class SsmParameterProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param key: ``CfnResponsePlan.SsmParameterProperty.Key``.
            :param values: ``CfnResponsePlan.SsmParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmincidents as ssmincidents
                
                ssm_parameter_property = ssmincidents.CfnResponsePlan.SsmParameterProperty(
                    key="key",
                    values=["values"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnResponsePlan.SsmParameterProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html#cfn-ssmincidents-responseplan-ssmparameter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''``CfnResponsePlan.SsmParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html#cfn-ssmincidents-responseplan-ssmparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsmParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmincidents.CfnResponsePlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "chat_channel": "chatChannel",
        "display_name": "displayName",
        "engagements": "engagements",
        "incident_template": "incidentTemplate",
        "name": "name",
        "tags": "tags",
    },
)
class CfnResponsePlanProps:
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnResponsePlan.ActionProperty, _IResolvable_da3f097b]]]] = None,
        chat_channel: typing.Optional[typing.Union[CfnResponsePlan.ChatChannelProperty, _IResolvable_da3f097b]] = None,
        display_name: typing.Optional[builtins.str] = None,
        engagements: typing.Optional[typing.Sequence[builtins.str]] = None,
        incident_template: typing.Union[CfnResponsePlan.IncidentTemplateProperty, _IResolvable_da3f097b],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSMIncidents::ResponsePlan``.

        :param actions: ``AWS::SSMIncidents::ResponsePlan.Actions``.
        :param chat_channel: ``AWS::SSMIncidents::ResponsePlan.ChatChannel``.
        :param display_name: ``AWS::SSMIncidents::ResponsePlan.DisplayName``.
        :param engagements: ``AWS::SSMIncidents::ResponsePlan.Engagements``.
        :param incident_template: ``AWS::SSMIncidents::ResponsePlan.IncidentTemplate``.
        :param name: ``AWS::SSMIncidents::ResponsePlan.Name``.
        :param tags: ``AWS::SSMIncidents::ResponsePlan.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmincidents as ssmincidents
            
            cfn_response_plan_props = ssmincidents.CfnResponsePlanProps(
                incident_template=ssmincidents.CfnResponsePlan.IncidentTemplateProperty(
                    impact=123,
                    title="title",
            
                    # the properties below are optional
                    dedupe_string="dedupeString",
                    notification_targets=[ssmincidents.CfnResponsePlan.NotificationTargetItemProperty(
                        sns_topic_arn="snsTopicArn"
                    )],
                    summary="summary"
                ),
                name="name",
            
                # the properties below are optional
                actions=[ssmincidents.CfnResponsePlan.ActionProperty(
                    ssm_automation=ssmincidents.CfnResponsePlan.SsmAutomationProperty(
                        document_name="documentName",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        document_version="documentVersion",
                        parameters=[ssmincidents.CfnResponsePlan.SsmParameterProperty(
                            key="key",
                            values=["values"]
                        )],
                        target_account="targetAccount"
                    )
                )],
                chat_channel=ssmincidents.CfnResponsePlan.ChatChannelProperty(
                    chatbot_sns=["chatbotSns"]
                ),
                display_name="displayName",
                engagements=["engagements"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "incident_template": incident_template,
            "name": name,
        }
        if actions is not None:
            self._values["actions"] = actions
        if chat_channel is not None:
            self._values["chat_channel"] = chat_channel
        if display_name is not None:
            self._values["display_name"] = display_name
        if engagements is not None:
            self._values["engagements"] = engagements
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnResponsePlan.ActionProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::SSMIncidents::ResponsePlan.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-actions
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnResponsePlan.ActionProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def chat_channel(
        self,
    ) -> typing.Optional[typing.Union[CfnResponsePlan.ChatChannelProperty, _IResolvable_da3f097b]]:
        '''``AWS::SSMIncidents::ResponsePlan.ChatChannel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-chatchannel
        '''
        result = self._values.get("chat_channel")
        return typing.cast(typing.Optional[typing.Union[CfnResponsePlan.ChatChannelProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSMIncidents::ResponsePlan.DisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engagements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSMIncidents::ResponsePlan.Engagements``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-engagements
        '''
        result = self._values.get("engagements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def incident_template(
        self,
    ) -> typing.Union[CfnResponsePlan.IncidentTemplateProperty, _IResolvable_da3f097b]:
        '''``AWS::SSMIncidents::ResponsePlan.IncidentTemplate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-incidenttemplate
        '''
        result = self._values.get("incident_template")
        assert result is not None, "Required property 'incident_template' is missing"
        return typing.cast(typing.Union[CfnResponsePlan.IncidentTemplateProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::SSMIncidents::ResponsePlan.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::SSMIncidents::ResponsePlan.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResponsePlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnReplicationSet",
    "CfnReplicationSetProps",
    "CfnResponsePlan",
    "CfnResponsePlanProps",
]

publication.publish()
