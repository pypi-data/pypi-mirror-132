'''
# AWS::ApplicationInsights Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_applicationinsights as applicationinsights
```

> The construct library for this service is in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package named:
>
> ```
> @aws-cdk/aws-applicationinsights-alpha
> ```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ApplicationInsights](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationInsights.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication",
):
    '''A CloudFormation ``AWS::ApplicationInsights::Application``.

    :cloudformationResource: AWS::ApplicationInsights::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_applicationinsights as applicationinsights
        
        cfn_application = applicationinsights.CfnApplication(self, "MyCfnApplication",
            resource_group_name="resourceGroupName",
        
            # the properties below are optional
            auto_configuration_enabled=False,
            component_monitoring_settings=[applicationinsights.CfnApplication.ComponentMonitoringSettingProperty(
                component_configuration_mode="componentConfigurationMode",
                tier="tier",
        
                # the properties below are optional
                component_arn="componentArn",
                component_name="componentName",
                custom_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                    configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                        alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                            alarm_metric_name="alarmMetricName"
                        )],
                        alarms=[applicationinsights.CfnApplication.AlarmProperty(
                            alarm_name="alarmName",
        
                            # the properties below are optional
                            severity="severity"
                        )],
                        jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                            host_port="hostPort",
                            jmxurl="jmxurl",
                            prometheus_port="prometheusPort"
                        ),
                        logs=[applicationinsights.CfnApplication.LogProperty(
                            log_type="logType",
        
                            # the properties below are optional
                            encoding="encoding",
                            log_group_name="logGroupName",
                            log_path="logPath",
                            pattern_set="patternSet"
                        )],
                        windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                            event_levels=["eventLevels"],
                            event_name="eventName",
                            log_group_name="logGroupName",
        
                            # the properties below are optional
                            pattern_set="patternSet"
                        )]
                    ),
                    sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                        sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
        
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
        
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type="subComponentType"
                    )]
                ),
                default_overwrite_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                    configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                        alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                            alarm_metric_name="alarmMetricName"
                        )],
                        alarms=[applicationinsights.CfnApplication.AlarmProperty(
                            alarm_name="alarmName",
        
                            # the properties below are optional
                            severity="severity"
                        )],
                        jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                            host_port="hostPort",
                            jmxurl="jmxurl",
                            prometheus_port="prometheusPort"
                        ),
                        logs=[applicationinsights.CfnApplication.LogProperty(
                            log_type="logType",
        
                            # the properties below are optional
                            encoding="encoding",
                            log_group_name="logGroupName",
                            log_path="logPath",
                            pattern_set="patternSet"
                        )],
                        windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                            event_levels=["eventLevels"],
                            event_name="eventName",
                            log_group_name="logGroupName",
        
                            # the properties below are optional
                            pattern_set="patternSet"
                        )]
                    ),
                    sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                        sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
        
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
        
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type="subComponentType"
                    )]
                )
            )],
            custom_components=[applicationinsights.CfnApplication.CustomComponentProperty(
                component_name="componentName",
                resource_list=["resourceList"]
            )],
            cwe_monitor_enabled=False,
            log_pattern_sets=[applicationinsights.CfnApplication.LogPatternSetProperty(
                log_patterns=[applicationinsights.CfnApplication.LogPatternProperty(
                    pattern="pattern",
                    pattern_name="patternName",
                    rank=123
                )],
                pattern_set_name="patternSetName"
            )],
            ops_center_enabled=False,
            ops_item_sns_topic_arn="opsItemSnsTopicArn",
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
        auto_configuration_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        component_monitoring_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.ComponentMonitoringSettingProperty", _IResolvable_da3f097b]]]] = None,
        custom_components: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.CustomComponentProperty", _IResolvable_da3f097b]]]] = None,
        cwe_monitor_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        log_pattern_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.LogPatternSetProperty", _IResolvable_da3f097b]]]] = None,
        ops_center_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ops_item_sns_topic_arn: typing.Optional[builtins.str] = None,
        resource_group_name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::ApplicationInsights::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param auto_configuration_enabled: ``AWS::ApplicationInsights::Application.AutoConfigurationEnabled``.
        :param component_monitoring_settings: ``AWS::ApplicationInsights::Application.ComponentMonitoringSettings``.
        :param custom_components: ``AWS::ApplicationInsights::Application.CustomComponents``.
        :param cwe_monitor_enabled: ``AWS::ApplicationInsights::Application.CWEMonitorEnabled``.
        :param log_pattern_sets: ``AWS::ApplicationInsights::Application.LogPatternSets``.
        :param ops_center_enabled: ``AWS::ApplicationInsights::Application.OpsCenterEnabled``.
        :param ops_item_sns_topic_arn: ``AWS::ApplicationInsights::Application.OpsItemSNSTopicArn``.
        :param resource_group_name: ``AWS::ApplicationInsights::Application.ResourceGroupName``.
        :param tags: ``AWS::ApplicationInsights::Application.Tags``.
        '''
        props = CfnApplicationProps(
            auto_configuration_enabled=auto_configuration_enabled,
            component_monitoring_settings=component_monitoring_settings,
            custom_components=custom_components,
            cwe_monitor_enabled=cwe_monitor_enabled,
            log_pattern_sets=log_pattern_sets,
            ops_center_enabled=ops_center_enabled,
            ops_item_sns_topic_arn=ops_item_sns_topic_arn,
            resource_group_name=resource_group_name,
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
    @jsii.member(jsii_name="attrApplicationArn")
    def attr_application_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApplicationARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoConfigurationEnabled")
    def auto_configuration_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::ApplicationInsights::Application.AutoConfigurationEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-autoconfigurationenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoConfigurationEnabled"))

    @auto_configuration_enabled.setter
    def auto_configuration_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "autoConfigurationEnabled", value)

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
    @jsii.member(jsii_name="componentMonitoringSettings")
    def component_monitoring_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.ComponentMonitoringSettingProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::ApplicationInsights::Application.ComponentMonitoringSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-componentmonitoringsettings
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.ComponentMonitoringSettingProperty", _IResolvable_da3f097b]]]], jsii.get(self, "componentMonitoringSettings"))

    @component_monitoring_settings.setter
    def component_monitoring_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.ComponentMonitoringSettingProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "componentMonitoringSettings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customComponents")
    def custom_components(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.CustomComponentProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::ApplicationInsights::Application.CustomComponents``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-customcomponents
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.CustomComponentProperty", _IResolvable_da3f097b]]]], jsii.get(self, "customComponents"))

    @custom_components.setter
    def custom_components(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.CustomComponentProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "customComponents", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cweMonitorEnabled")
    def cwe_monitor_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::ApplicationInsights::Application.CWEMonitorEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-cwemonitorenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "cweMonitorEnabled"))

    @cwe_monitor_enabled.setter
    def cwe_monitor_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "cweMonitorEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logPatternSets")
    def log_pattern_sets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternSetProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::ApplicationInsights::Application.LogPatternSets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-logpatternsets
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternSetProperty", _IResolvable_da3f097b]]]], jsii.get(self, "logPatternSets"))

    @log_pattern_sets.setter
    def log_pattern_sets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternSetProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "logPatternSets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="opsCenterEnabled")
    def ops_center_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::ApplicationInsights::Application.OpsCenterEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opscenterenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "opsCenterEnabled"))

    @ops_center_enabled.setter
    def ops_center_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "opsCenterEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="opsItemSnsTopicArn")
    def ops_item_sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ApplicationInsights::Application.OpsItemSNSTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opsitemsnstopicarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opsItemSnsTopicArn"))

    @ops_item_sns_topic_arn.setter
    def ops_item_sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "opsItemSnsTopicArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        '''``AWS::ApplicationInsights::Application.ResourceGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-resourcegroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "resourceGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::ApplicationInsights::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.AlarmMetricProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_metric_name": "alarmMetricName"},
    )
    class AlarmMetricProperty:
        def __init__(self, *, alarm_metric_name: builtins.str) -> None:
            '''
            :param alarm_metric_name: ``CfnApplication.AlarmMetricProperty.AlarmMetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                alarm_metric_property = applicationinsights.CfnApplication.AlarmMetricProperty(
                    alarm_metric_name="alarmMetricName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "alarm_metric_name": alarm_metric_name,
            }

        @builtins.property
        def alarm_metric_name(self) -> builtins.str:
            '''``CfnApplication.AlarmMetricProperty.AlarmMetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html#cfn-applicationinsights-application-alarmmetric-alarmmetricname
            '''
            result = self._values.get("alarm_metric_name")
            assert result is not None, "Required property 'alarm_metric_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmMetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.AlarmProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_name": "alarmName", "severity": "severity"},
    )
    class AlarmProperty:
        def __init__(
            self,
            *,
            alarm_name: builtins.str,
            severity: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param alarm_name: ``CfnApplication.AlarmProperty.AlarmName``.
            :param severity: ``CfnApplication.AlarmProperty.Severity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                alarm_property = applicationinsights.CfnApplication.AlarmProperty(
                    alarm_name="alarmName",
                
                    # the properties below are optional
                    severity="severity"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "alarm_name": alarm_name,
            }
            if severity is not None:
                self._values["severity"] = severity

        @builtins.property
        def alarm_name(self) -> builtins.str:
            '''``CfnApplication.AlarmProperty.AlarmName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-alarmname
            '''
            result = self._values.get("alarm_name")
            assert result is not None, "Required property 'alarm_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def severity(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.AlarmProperty.Severity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-severity
            '''
            result = self._values.get("severity")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.ComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_details": "configurationDetails",
            "sub_component_type_configurations": "subComponentTypeConfigurations",
        },
    )
    class ComponentConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_details: typing.Optional[typing.Union["CfnApplication.ConfigurationDetailsProperty", _IResolvable_da3f097b]] = None,
            sub_component_type_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.SubComponentTypeConfigurationProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param configuration_details: ``CfnApplication.ComponentConfigurationProperty.ConfigurationDetails``.
            :param sub_component_type_configurations: ``CfnApplication.ComponentConfigurationProperty.SubComponentTypeConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                component_configuration_property = applicationinsights.CfnApplication.ComponentConfigurationProperty(
                    configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                        alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                            alarm_metric_name="alarmMetricName"
                        )],
                        alarms=[applicationinsights.CfnApplication.AlarmProperty(
                            alarm_name="alarmName",
                
                            # the properties below are optional
                            severity="severity"
                        )],
                        jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                            host_port="hostPort",
                            jmxurl="jmxurl",
                            prometheus_port="prometheusPort"
                        ),
                        logs=[applicationinsights.CfnApplication.LogProperty(
                            log_type="logType",
                
                            # the properties below are optional
                            encoding="encoding",
                            log_group_name="logGroupName",
                            log_path="logPath",
                            pattern_set="patternSet"
                        )],
                        windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                            event_levels=["eventLevels"],
                            event_name="eventName",
                            log_group_name="logGroupName",
                
                            # the properties below are optional
                            pattern_set="patternSet"
                        )]
                    ),
                    sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                        sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
                
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
                
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type="subComponentType"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if configuration_details is not None:
                self._values["configuration_details"] = configuration_details
            if sub_component_type_configurations is not None:
                self._values["sub_component_type_configurations"] = sub_component_type_configurations

        @builtins.property
        def configuration_details(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ConfigurationDetailsProperty", _IResolvable_da3f097b]]:
            '''``CfnApplication.ComponentConfigurationProperty.ConfigurationDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-configurationdetails
            '''
            result = self._values.get("configuration_details")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ConfigurationDetailsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sub_component_type_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.SubComponentTypeConfigurationProperty", _IResolvable_da3f097b]]]]:
            '''``CfnApplication.ComponentConfigurationProperty.SubComponentTypeConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-subcomponenttypeconfigurations
            '''
            result = self._values.get("sub_component_type_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.SubComponentTypeConfigurationProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.ComponentMonitoringSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_arn": "componentArn",
            "component_configuration_mode": "componentConfigurationMode",
            "component_name": "componentName",
            "custom_component_configuration": "customComponentConfiguration",
            "default_overwrite_component_configuration": "defaultOverwriteComponentConfiguration",
            "tier": "tier",
        },
    )
    class ComponentMonitoringSettingProperty:
        def __init__(
            self,
            *,
            component_arn: typing.Optional[builtins.str] = None,
            component_configuration_mode: builtins.str,
            component_name: typing.Optional[builtins.str] = None,
            custom_component_configuration: typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]] = None,
            default_overwrite_component_configuration: typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]] = None,
            tier: builtins.str,
        ) -> None:
            '''
            :param component_arn: ``CfnApplication.ComponentMonitoringSettingProperty.ComponentARN``.
            :param component_configuration_mode: ``CfnApplication.ComponentMonitoringSettingProperty.ComponentConfigurationMode``.
            :param component_name: ``CfnApplication.ComponentMonitoringSettingProperty.ComponentName``.
            :param custom_component_configuration: ``CfnApplication.ComponentMonitoringSettingProperty.CustomComponentConfiguration``.
            :param default_overwrite_component_configuration: ``CfnApplication.ComponentMonitoringSettingProperty.DefaultOverwriteComponentConfiguration``.
            :param tier: ``CfnApplication.ComponentMonitoringSettingProperty.Tier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                component_monitoring_setting_property = applicationinsights.CfnApplication.ComponentMonitoringSettingProperty(
                    component_configuration_mode="componentConfigurationMode",
                    tier="tier",
                
                    # the properties below are optional
                    component_arn="componentArn",
                    component_name="componentName",
                    custom_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                        configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            alarms=[applicationinsights.CfnApplication.AlarmProperty(
                                alarm_name="alarmName",
                
                                # the properties below are optional
                                severity="severity"
                            )],
                            jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                                host_port="hostPort",
                                jmxurl="jmxurl",
                                prometheus_port="prometheusPort"
                            ),
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
                
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
                
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                            sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                                alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                    alarm_metric_name="alarmMetricName"
                                )],
                                logs=[applicationinsights.CfnApplication.LogProperty(
                                    log_type="logType",
                
                                    # the properties below are optional
                                    encoding="encoding",
                                    log_group_name="logGroupName",
                                    log_path="logPath",
                                    pattern_set="patternSet"
                                )],
                                windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                    event_levels=["eventLevels"],
                                    event_name="eventName",
                                    log_group_name="logGroupName",
                
                                    # the properties below are optional
                                    pattern_set="patternSet"
                                )]
                            ),
                            sub_component_type="subComponentType"
                        )]
                    ),
                    default_overwrite_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                        configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            alarms=[applicationinsights.CfnApplication.AlarmProperty(
                                alarm_name="alarmName",
                
                                # the properties below are optional
                                severity="severity"
                            )],
                            jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                                host_port="hostPort",
                                jmxurl="jmxurl",
                                prometheus_port="prometheusPort"
                            ),
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
                
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
                
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                            sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                                alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                    alarm_metric_name="alarmMetricName"
                                )],
                                logs=[applicationinsights.CfnApplication.LogProperty(
                                    log_type="logType",
                
                                    # the properties below are optional
                                    encoding="encoding",
                                    log_group_name="logGroupName",
                                    log_path="logPath",
                                    pattern_set="patternSet"
                                )],
                                windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                    event_levels=["eventLevels"],
                                    event_name="eventName",
                                    log_group_name="logGroupName",
                
                                    # the properties below are optional
                                    pattern_set="patternSet"
                                )]
                            ),
                            sub_component_type="subComponentType"
                        )]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "component_configuration_mode": component_configuration_mode,
                "tier": tier,
            }
            if component_arn is not None:
                self._values["component_arn"] = component_arn
            if component_name is not None:
                self._values["component_name"] = component_name
            if custom_component_configuration is not None:
                self._values["custom_component_configuration"] = custom_component_configuration
            if default_overwrite_component_configuration is not None:
                self._values["default_overwrite_component_configuration"] = default_overwrite_component_configuration

        @builtins.property
        def component_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.ComponentMonitoringSettingProperty.ComponentARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentarn
            '''
            result = self._values.get("component_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def component_configuration_mode(self) -> builtins.str:
            '''``CfnApplication.ComponentMonitoringSettingProperty.ComponentConfigurationMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentconfigurationmode
            '''
            result = self._values.get("component_configuration_mode")
            assert result is not None, "Required property 'component_configuration_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def component_name(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.ComponentMonitoringSettingProperty.ComponentName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentname
            '''
            result = self._values.get("component_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_component_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnApplication.ComponentMonitoringSettingProperty.CustomComponentConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-customcomponentconfiguration
            '''
            result = self._values.get("custom_component_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def default_overwrite_component_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnApplication.ComponentMonitoringSettingProperty.DefaultOverwriteComponentConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-defaultoverwritecomponentconfiguration
            '''
            result = self._values.get("default_overwrite_component_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def tier(self) -> builtins.str:
            '''``CfnApplication.ComponentMonitoringSettingProperty.Tier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-tier
            '''
            result = self._values.get("tier")
            assert result is not None, "Required property 'tier' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentMonitoringSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.ConfigurationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarm_metrics": "alarmMetrics",
            "alarms": "alarms",
            "jmx_prometheus_exporter": "jmxPrometheusExporter",
            "logs": "logs",
            "windows_events": "windowsEvents",
        },
    )
    class ConfigurationDetailsProperty:
        def __init__(
            self,
            *,
            alarm_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]] = None,
            alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.AlarmProperty", _IResolvable_da3f097b]]]] = None,
            jmx_prometheus_exporter: typing.Optional[typing.Union["CfnApplication.JMXPrometheusExporterProperty", _IResolvable_da3f097b]] = None,
            logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]] = None,
            windows_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param alarm_metrics: ``CfnApplication.ConfigurationDetailsProperty.AlarmMetrics``.
            :param alarms: ``CfnApplication.ConfigurationDetailsProperty.Alarms``.
            :param jmx_prometheus_exporter: ``CfnApplication.ConfigurationDetailsProperty.JMXPrometheusExporter``.
            :param logs: ``CfnApplication.ConfigurationDetailsProperty.Logs``.
            :param windows_events: ``CfnApplication.ConfigurationDetailsProperty.WindowsEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                configuration_details_property = applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                    alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                        alarm_metric_name="alarmMetricName"
                    )],
                    alarms=[applicationinsights.CfnApplication.AlarmProperty(
                        alarm_name="alarmName",
                
                        # the properties below are optional
                        severity="severity"
                    )],
                    jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                        host_port="hostPort",
                        jmxurl="jmxurl",
                        prometheus_port="prometheusPort"
                    ),
                    logs=[applicationinsights.CfnApplication.LogProperty(
                        log_type="logType",
                
                        # the properties below are optional
                        encoding="encoding",
                        log_group_name="logGroupName",
                        log_path="logPath",
                        pattern_set="patternSet"
                    )],
                    windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                        event_levels=["eventLevels"],
                        event_name="eventName",
                        log_group_name="logGroupName",
                
                        # the properties below are optional
                        pattern_set="patternSet"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if alarm_metrics is not None:
                self._values["alarm_metrics"] = alarm_metrics
            if alarms is not None:
                self._values["alarms"] = alarms
            if jmx_prometheus_exporter is not None:
                self._values["jmx_prometheus_exporter"] = jmx_prometheus_exporter
            if logs is not None:
                self._values["logs"] = logs
            if windows_events is not None:
                self._values["windows_events"] = windows_events

        @builtins.property
        def alarm_metrics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]]:
            '''``CfnApplication.ConfigurationDetailsProperty.AlarmMetrics``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarmmetrics
            '''
            result = self._values.get("alarm_metrics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def alarms(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmProperty", _IResolvable_da3f097b]]]]:
            '''``CfnApplication.ConfigurationDetailsProperty.Alarms``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarms
            '''
            result = self._values.get("alarms")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def jmx_prometheus_exporter(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.JMXPrometheusExporterProperty", _IResolvable_da3f097b]]:
            '''``CfnApplication.ConfigurationDetailsProperty.JMXPrometheusExporter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-jmxprometheusexporter
            '''
            result = self._values.get("jmx_prometheus_exporter")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.JMXPrometheusExporterProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]]:
            '''``CfnApplication.ConfigurationDetailsProperty.Logs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-logs
            '''
            result = self._values.get("logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def windows_events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]]:
            '''``CfnApplication.ConfigurationDetailsProperty.WindowsEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-windowsevents
            '''
            result = self._values.get("windows_events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.CustomComponentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_name": "componentName",
            "resource_list": "resourceList",
        },
    )
    class CustomComponentProperty:
        def __init__(
            self,
            *,
            component_name: builtins.str,
            resource_list: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param component_name: ``CfnApplication.CustomComponentProperty.ComponentName``.
            :param resource_list: ``CfnApplication.CustomComponentProperty.ResourceList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                custom_component_property = applicationinsights.CfnApplication.CustomComponentProperty(
                    component_name="componentName",
                    resource_list=["resourceList"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "component_name": component_name,
                "resource_list": resource_list,
            }

        @builtins.property
        def component_name(self) -> builtins.str:
            '''``CfnApplication.CustomComponentProperty.ComponentName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-componentname
            '''
            result = self._values.get("component_name")
            assert result is not None, "Required property 'component_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_list(self) -> typing.List[builtins.str]:
            '''``CfnApplication.CustomComponentProperty.ResourceList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-resourcelist
            '''
            result = self._values.get("resource_list")
            assert result is not None, "Required property 'resource_list' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomComponentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.JMXPrometheusExporterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "host_port": "hostPort",
            "jmxurl": "jmxurl",
            "prometheus_port": "prometheusPort",
        },
    )
    class JMXPrometheusExporterProperty:
        def __init__(
            self,
            *,
            host_port: typing.Optional[builtins.str] = None,
            jmxurl: typing.Optional[builtins.str] = None,
            prometheus_port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param host_port: ``CfnApplication.JMXPrometheusExporterProperty.HostPort``.
            :param jmxurl: ``CfnApplication.JMXPrometheusExporterProperty.JMXURL``.
            :param prometheus_port: ``CfnApplication.JMXPrometheusExporterProperty.PrometheusPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                j_mXPrometheus_exporter_property = applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                    host_port="hostPort",
                    jmxurl="jmxurl",
                    prometheus_port="prometheusPort"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if host_port is not None:
                self._values["host_port"] = host_port
            if jmxurl is not None:
                self._values["jmxurl"] = jmxurl
            if prometheus_port is not None:
                self._values["prometheus_port"] = prometheus_port

        @builtins.property
        def host_port(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.JMXPrometheusExporterProperty.HostPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-hostport
            '''
            result = self._values.get("host_port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def jmxurl(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.JMXPrometheusExporterProperty.JMXURL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-jmxurl
            '''
            result = self._values.get("jmxurl")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prometheus_port(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.JMXPrometheusExporterProperty.PrometheusPort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-prometheusport
            '''
            result = self._values.get("prometheus_port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JMXPrometheusExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.LogPatternProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pattern": "pattern",
            "pattern_name": "patternName",
            "rank": "rank",
        },
    )
    class LogPatternProperty:
        def __init__(
            self,
            *,
            pattern: builtins.str,
            pattern_name: builtins.str,
            rank: jsii.Number,
        ) -> None:
            '''
            :param pattern: ``CfnApplication.LogPatternProperty.Pattern``.
            :param pattern_name: ``CfnApplication.LogPatternProperty.PatternName``.
            :param rank: ``CfnApplication.LogPatternProperty.Rank``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                log_pattern_property = applicationinsights.CfnApplication.LogPatternProperty(
                    pattern="pattern",
                    pattern_name="patternName",
                    rank=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "pattern": pattern,
                "pattern_name": pattern_name,
                "rank": rank,
            }

        @builtins.property
        def pattern(self) -> builtins.str:
            '''``CfnApplication.LogPatternProperty.Pattern``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pattern_name(self) -> builtins.str:
            '''``CfnApplication.LogPatternProperty.PatternName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-patternname
            '''
            result = self._values.get("pattern_name")
            assert result is not None, "Required property 'pattern_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rank(self) -> jsii.Number:
            '''``CfnApplication.LogPatternProperty.Rank``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-rank
            '''
            result = self._values.get("rank")
            assert result is not None, "Required property 'rank' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogPatternProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.LogPatternSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_patterns": "logPatterns",
            "pattern_set_name": "patternSetName",
        },
    )
    class LogPatternSetProperty:
        def __init__(
            self,
            *,
            log_patterns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.LogPatternProperty", _IResolvable_da3f097b]]],
            pattern_set_name: builtins.str,
        ) -> None:
            '''
            :param log_patterns: ``CfnApplication.LogPatternSetProperty.LogPatterns``.
            :param pattern_set_name: ``CfnApplication.LogPatternSetProperty.PatternSetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                log_pattern_set_property = applicationinsights.CfnApplication.LogPatternSetProperty(
                    log_patterns=[applicationinsights.CfnApplication.LogPatternProperty(
                        pattern="pattern",
                        pattern_name="patternName",
                        rank=123
                    )],
                    pattern_set_name="patternSetName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "log_patterns": log_patterns,
                "pattern_set_name": pattern_set_name,
            }

        @builtins.property
        def log_patterns(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternProperty", _IResolvable_da3f097b]]]:
            '''``CfnApplication.LogPatternSetProperty.LogPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-logpatterns
            '''
            result = self._values.get("log_patterns")
            assert result is not None, "Required property 'log_patterns' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def pattern_set_name(self) -> builtins.str:
            '''``CfnApplication.LogPatternSetProperty.PatternSetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-patternsetname
            '''
            result = self._values.get("pattern_set_name")
            assert result is not None, "Required property 'pattern_set_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogPatternSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.LogProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encoding": "encoding",
            "log_group_name": "logGroupName",
            "log_path": "logPath",
            "log_type": "logType",
            "pattern_set": "patternSet",
        },
    )
    class LogProperty:
        def __init__(
            self,
            *,
            encoding: typing.Optional[builtins.str] = None,
            log_group_name: typing.Optional[builtins.str] = None,
            log_path: typing.Optional[builtins.str] = None,
            log_type: builtins.str,
            pattern_set: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encoding: ``CfnApplication.LogProperty.Encoding``.
            :param log_group_name: ``CfnApplication.LogProperty.LogGroupName``.
            :param log_path: ``CfnApplication.LogProperty.LogPath``.
            :param log_type: ``CfnApplication.LogProperty.LogType``.
            :param pattern_set: ``CfnApplication.LogProperty.PatternSet``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                log_property = applicationinsights.CfnApplication.LogProperty(
                    log_type="logType",
                
                    # the properties below are optional
                    encoding="encoding",
                    log_group_name="logGroupName",
                    log_path="logPath",
                    pattern_set="patternSet"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "log_type": log_type,
            }
            if encoding is not None:
                self._values["encoding"] = encoding
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_path is not None:
                self._values["log_path"] = log_path
            if pattern_set is not None:
                self._values["pattern_set"] = pattern_set

        @builtins.property
        def encoding(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.LogProperty.Encoding``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-encoding
            '''
            result = self._values.get("encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.LogProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_path(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.LogProperty.LogPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logpath
            '''
            result = self._values.get("log_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_type(self) -> builtins.str:
            '''``CfnApplication.LogProperty.LogType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logtype
            '''
            result = self._values.get("log_type")
            assert result is not None, "Required property 'log_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pattern_set(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.LogProperty.PatternSet``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-patternset
            '''
            result = self._values.get("pattern_set")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarm_metrics": "alarmMetrics",
            "logs": "logs",
            "windows_events": "windowsEvents",
        },
    )
    class SubComponentConfigurationDetailsProperty:
        def __init__(
            self,
            *,
            alarm_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]] = None,
            logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]] = None,
            windows_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param alarm_metrics: ``CfnApplication.SubComponentConfigurationDetailsProperty.AlarmMetrics``.
            :param logs: ``CfnApplication.SubComponentConfigurationDetailsProperty.Logs``.
            :param windows_events: ``CfnApplication.SubComponentConfigurationDetailsProperty.WindowsEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                sub_component_configuration_details_property = applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                    alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                        alarm_metric_name="alarmMetricName"
                    )],
                    logs=[applicationinsights.CfnApplication.LogProperty(
                        log_type="logType",
                
                        # the properties below are optional
                        encoding="encoding",
                        log_group_name="logGroupName",
                        log_path="logPath",
                        pattern_set="patternSet"
                    )],
                    windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                        event_levels=["eventLevels"],
                        event_name="eventName",
                        log_group_name="logGroupName",
                
                        # the properties below are optional
                        pattern_set="patternSet"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if alarm_metrics is not None:
                self._values["alarm_metrics"] = alarm_metrics
            if logs is not None:
                self._values["logs"] = logs
            if windows_events is not None:
                self._values["windows_events"] = windows_events

        @builtins.property
        def alarm_metrics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]]:
            '''``CfnApplication.SubComponentConfigurationDetailsProperty.AlarmMetrics``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-alarmmetrics
            '''
            result = self._values.get("alarm_metrics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]]:
            '''``CfnApplication.SubComponentConfigurationDetailsProperty.Logs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-logs
            '''
            result = self._values.get("logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def windows_events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]]:
            '''``CfnApplication.SubComponentConfigurationDetailsProperty.WindowsEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-windowsevents
            '''
            result = self._values.get("windows_events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubComponentConfigurationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sub_component_configuration_details": "subComponentConfigurationDetails",
            "sub_component_type": "subComponentType",
        },
    )
    class SubComponentTypeConfigurationProperty:
        def __init__(
            self,
            *,
            sub_component_configuration_details: typing.Union["CfnApplication.SubComponentConfigurationDetailsProperty", _IResolvable_da3f097b],
            sub_component_type: builtins.str,
        ) -> None:
            '''
            :param sub_component_configuration_details: ``CfnApplication.SubComponentTypeConfigurationProperty.SubComponentConfigurationDetails``.
            :param sub_component_type: ``CfnApplication.SubComponentTypeConfigurationProperty.SubComponentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                sub_component_type_configuration_property = applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                    sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                        alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                            alarm_metric_name="alarmMetricName"
                        )],
                        logs=[applicationinsights.CfnApplication.LogProperty(
                            log_type="logType",
                
                            # the properties below are optional
                            encoding="encoding",
                            log_group_name="logGroupName",
                            log_path="logPath",
                            pattern_set="patternSet"
                        )],
                        windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                            event_levels=["eventLevels"],
                            event_name="eventName",
                            log_group_name="logGroupName",
                
                            # the properties below are optional
                            pattern_set="patternSet"
                        )]
                    ),
                    sub_component_type="subComponentType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "sub_component_configuration_details": sub_component_configuration_details,
                "sub_component_type": sub_component_type,
            }

        @builtins.property
        def sub_component_configuration_details(
            self,
        ) -> typing.Union["CfnApplication.SubComponentConfigurationDetailsProperty", _IResolvable_da3f097b]:
            '''``CfnApplication.SubComponentTypeConfigurationProperty.SubComponentConfigurationDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponentconfigurationdetails
            '''
            result = self._values.get("sub_component_configuration_details")
            assert result is not None, "Required property 'sub_component_configuration_details' is missing"
            return typing.cast(typing.Union["CfnApplication.SubComponentConfigurationDetailsProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def sub_component_type(self) -> builtins.str:
            '''``CfnApplication.SubComponentTypeConfigurationProperty.SubComponentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponenttype
            '''
            result = self._values.get("sub_component_type")
            assert result is not None, "Required property 'sub_component_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubComponentTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.WindowsEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_levels": "eventLevels",
            "event_name": "eventName",
            "log_group_name": "logGroupName",
            "pattern_set": "patternSet",
        },
    )
    class WindowsEventProperty:
        def __init__(
            self,
            *,
            event_levels: typing.Sequence[builtins.str],
            event_name: builtins.str,
            log_group_name: builtins.str,
            pattern_set: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param event_levels: ``CfnApplication.WindowsEventProperty.EventLevels``.
            :param event_name: ``CfnApplication.WindowsEventProperty.EventName``.
            :param log_group_name: ``CfnApplication.WindowsEventProperty.LogGroupName``.
            :param pattern_set: ``CfnApplication.WindowsEventProperty.PatternSet``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                windows_event_property = applicationinsights.CfnApplication.WindowsEventProperty(
                    event_levels=["eventLevels"],
                    event_name="eventName",
                    log_group_name="logGroupName",
                
                    # the properties below are optional
                    pattern_set="patternSet"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "event_levels": event_levels,
                "event_name": event_name,
                "log_group_name": log_group_name,
            }
            if pattern_set is not None:
                self._values["pattern_set"] = pattern_set

        @builtins.property
        def event_levels(self) -> typing.List[builtins.str]:
            '''``CfnApplication.WindowsEventProperty.EventLevels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventlevels
            '''
            result = self._values.get("event_levels")
            assert result is not None, "Required property 'event_levels' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def event_name(self) -> builtins.str:
            '''``CfnApplication.WindowsEventProperty.EventName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventname
            '''
            result = self._values.get("event_name")
            assert result is not None, "Required property 'event_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''``CfnApplication.WindowsEventProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pattern_set(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.WindowsEventProperty.PatternSet``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-patternset
            '''
            result = self._values.get("pattern_set")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WindowsEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_configuration_enabled": "autoConfigurationEnabled",
        "component_monitoring_settings": "componentMonitoringSettings",
        "custom_components": "customComponents",
        "cwe_monitor_enabled": "cweMonitorEnabled",
        "log_pattern_sets": "logPatternSets",
        "ops_center_enabled": "opsCenterEnabled",
        "ops_item_sns_topic_arn": "opsItemSnsTopicArn",
        "resource_group_name": "resourceGroupName",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        auto_configuration_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        component_monitoring_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnApplication.ComponentMonitoringSettingProperty, _IResolvable_da3f097b]]]] = None,
        custom_components: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnApplication.CustomComponentProperty, _IResolvable_da3f097b]]]] = None,
        cwe_monitor_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        log_pattern_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnApplication.LogPatternSetProperty, _IResolvable_da3f097b]]]] = None,
        ops_center_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ops_item_sns_topic_arn: typing.Optional[builtins.str] = None,
        resource_group_name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ApplicationInsights::Application``.

        :param auto_configuration_enabled: ``AWS::ApplicationInsights::Application.AutoConfigurationEnabled``.
        :param component_monitoring_settings: ``AWS::ApplicationInsights::Application.ComponentMonitoringSettings``.
        :param custom_components: ``AWS::ApplicationInsights::Application.CustomComponents``.
        :param cwe_monitor_enabled: ``AWS::ApplicationInsights::Application.CWEMonitorEnabled``.
        :param log_pattern_sets: ``AWS::ApplicationInsights::Application.LogPatternSets``.
        :param ops_center_enabled: ``AWS::ApplicationInsights::Application.OpsCenterEnabled``.
        :param ops_item_sns_topic_arn: ``AWS::ApplicationInsights::Application.OpsItemSNSTopicArn``.
        :param resource_group_name: ``AWS::ApplicationInsights::Application.ResourceGroupName``.
        :param tags: ``AWS::ApplicationInsights::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_applicationinsights as applicationinsights
            
            cfn_application_props = applicationinsights.CfnApplicationProps(
                resource_group_name="resourceGroupName",
            
                # the properties below are optional
                auto_configuration_enabled=False,
                component_monitoring_settings=[applicationinsights.CfnApplication.ComponentMonitoringSettingProperty(
                    component_configuration_mode="componentConfigurationMode",
                    tier="tier",
            
                    # the properties below are optional
                    component_arn="componentArn",
                    component_name="componentName",
                    custom_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                        configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            alarms=[applicationinsights.CfnApplication.AlarmProperty(
                                alarm_name="alarmName",
            
                                # the properties below are optional
                                severity="severity"
                            )],
                            jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                                host_port="hostPort",
                                jmxurl="jmxurl",
                                prometheus_port="prometheusPort"
                            ),
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
            
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
            
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                            sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                                alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                    alarm_metric_name="alarmMetricName"
                                )],
                                logs=[applicationinsights.CfnApplication.LogProperty(
                                    log_type="logType",
            
                                    # the properties below are optional
                                    encoding="encoding",
                                    log_group_name="logGroupName",
                                    log_path="logPath",
                                    pattern_set="patternSet"
                                )],
                                windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                    event_levels=["eventLevels"],
                                    event_name="eventName",
                                    log_group_name="logGroupName",
            
                                    # the properties below are optional
                                    pattern_set="patternSet"
                                )]
                            ),
                            sub_component_type="subComponentType"
                        )]
                    ),
                    default_overwrite_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                        configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            alarms=[applicationinsights.CfnApplication.AlarmProperty(
                                alarm_name="alarmName",
            
                                # the properties below are optional
                                severity="severity"
                            )],
                            jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                                host_port="hostPort",
                                jmxurl="jmxurl",
                                prometheus_port="prometheusPort"
                            ),
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
            
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
            
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                            sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                                alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                    alarm_metric_name="alarmMetricName"
                                )],
                                logs=[applicationinsights.CfnApplication.LogProperty(
                                    log_type="logType",
            
                                    # the properties below are optional
                                    encoding="encoding",
                                    log_group_name="logGroupName",
                                    log_path="logPath",
                                    pattern_set="patternSet"
                                )],
                                windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                    event_levels=["eventLevels"],
                                    event_name="eventName",
                                    log_group_name="logGroupName",
            
                                    # the properties below are optional
                                    pattern_set="patternSet"
                                )]
                            ),
                            sub_component_type="subComponentType"
                        )]
                    )
                )],
                custom_components=[applicationinsights.CfnApplication.CustomComponentProperty(
                    component_name="componentName",
                    resource_list=["resourceList"]
                )],
                cwe_monitor_enabled=False,
                log_pattern_sets=[applicationinsights.CfnApplication.LogPatternSetProperty(
                    log_patterns=[applicationinsights.CfnApplication.LogPatternProperty(
                        pattern="pattern",
                        pattern_name="patternName",
                        rank=123
                    )],
                    pattern_set_name="patternSetName"
                )],
                ops_center_enabled=False,
                ops_item_sns_topic_arn="opsItemSnsTopicArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_group_name": resource_group_name,
        }
        if auto_configuration_enabled is not None:
            self._values["auto_configuration_enabled"] = auto_configuration_enabled
        if component_monitoring_settings is not None:
            self._values["component_monitoring_settings"] = component_monitoring_settings
        if custom_components is not None:
            self._values["custom_components"] = custom_components
        if cwe_monitor_enabled is not None:
            self._values["cwe_monitor_enabled"] = cwe_monitor_enabled
        if log_pattern_sets is not None:
            self._values["log_pattern_sets"] = log_pattern_sets
        if ops_center_enabled is not None:
            self._values["ops_center_enabled"] = ops_center_enabled
        if ops_item_sns_topic_arn is not None:
            self._values["ops_item_sns_topic_arn"] = ops_item_sns_topic_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auto_configuration_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::ApplicationInsights::Application.AutoConfigurationEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-autoconfigurationenabled
        '''
        result = self._values.get("auto_configuration_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def component_monitoring_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.ComponentMonitoringSettingProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::ApplicationInsights::Application.ComponentMonitoringSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-componentmonitoringsettings
        '''
        result = self._values.get("component_monitoring_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.ComponentMonitoringSettingProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def custom_components(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.CustomComponentProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::ApplicationInsights::Application.CustomComponents``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-customcomponents
        '''
        result = self._values.get("custom_components")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.CustomComponentProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def cwe_monitor_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::ApplicationInsights::Application.CWEMonitorEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-cwemonitorenabled
        '''
        result = self._values.get("cwe_monitor_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def log_pattern_sets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.LogPatternSetProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::ApplicationInsights::Application.LogPatternSets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-logpatternsets
        '''
        result = self._values.get("log_pattern_sets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.LogPatternSetProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def ops_center_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::ApplicationInsights::Application.OpsCenterEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opscenterenabled
        '''
        result = self._values.get("ops_center_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def ops_item_sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ApplicationInsights::Application.OpsItemSNSTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opsitemsnstopicarn
        '''
        result = self._values.get("ops_item_sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''``AWS::ApplicationInsights::Application.ResourceGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-resourcegroupname
        '''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::ApplicationInsights::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
]

publication.publish()
