'''
# AWS::GroundStation Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_groundstation as groundstation
```

> The construct library for this service is in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package named:
>
> ```
> @aws-cdk/aws-groundstation-alpha
> ```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GroundStation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GroundStation.html).

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
class CfnConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig",
):
    '''A CloudFormation ``AWS::GroundStation::Config``.

    :cloudformationResource: AWS::GroundStation::Config
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_groundstation as groundstation
        
        cfn_config = groundstation.CfnConfig(self, "MyCfnConfig",
            config_data=groundstation.CfnConfig.ConfigDataProperty(
                antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                ),
                antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                    decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                ),
                antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    ),
                    target_eirp=groundstation.CfnConfig.EirpProperty(
                        units="units",
                        value=123
                    ),
                    transmit_disabled=False
                ),
                dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                    dataflow_endpoint_name="dataflowEndpointName",
                    dataflow_endpoint_region="dataflowEndpointRegion"
                ),
                s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                    bucket_arn="bucketArn",
                    prefix="prefix",
                    role_arn="roleArn"
                ),
                tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                    autotrack="autotrack"
                ),
                uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                    antenna_uplink_config_arn="antennaUplinkConfigArn",
                    enabled=False
                )
            ),
            name="name",
        
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
        config_data: typing.Union["CfnConfig.ConfigDataProperty", _IResolvable_da3f097b],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::GroundStation::Config``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param config_data: ``AWS::GroundStation::Config.ConfigData``.
        :param name: ``AWS::GroundStation::Config.Name``.
        :param tags: ``AWS::GroundStation::Config.Tags``.
        '''
        props = CfnConfigProps(config_data=config_data, name=name, tags=tags)

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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

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
    @jsii.member(jsii_name="configData")
    def config_data(
        self,
    ) -> typing.Union["CfnConfig.ConfigDataProperty", _IResolvable_da3f097b]:
        '''``AWS::GroundStation::Config.ConfigData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-configdata
        '''
        return typing.cast(typing.Union["CfnConfig.ConfigDataProperty", _IResolvable_da3f097b], jsii.get(self, "configData"))

    @config_data.setter
    def config_data(
        self,
        value: typing.Union["CfnConfig.ConfigDataProperty", _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "configData", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::GroundStation::Config.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::GroundStation::Config.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.AntennaDownlinkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"spectrum_config": "spectrumConfig"},
    )
    class AntennaDownlinkConfigProperty:
        def __init__(
            self,
            *,
            spectrum_config: typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param spectrum_config: ``CfnConfig.AntennaDownlinkConfigProperty.SpectrumConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                antenna_downlink_config_property = groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.AntennaDownlinkConfigProperty.SpectrumConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html#cfn-groundstation-config-antennadownlinkconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaDownlinkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "decode_config": "decodeConfig",
            "demodulation_config": "demodulationConfig",
            "spectrum_config": "spectrumConfig",
        },
    )
    class AntennaDownlinkDemodDecodeConfigProperty:
        def __init__(
            self,
            *,
            decode_config: typing.Optional[typing.Union["CfnConfig.DecodeConfigProperty", _IResolvable_da3f097b]] = None,
            demodulation_config: typing.Optional[typing.Union["CfnConfig.DemodulationConfigProperty", _IResolvable_da3f097b]] = None,
            spectrum_config: typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param decode_config: ``CfnConfig.AntennaDownlinkDemodDecodeConfigProperty.DecodeConfig``.
            :param demodulation_config: ``CfnConfig.AntennaDownlinkDemodDecodeConfigProperty.DemodulationConfig``.
            :param spectrum_config: ``CfnConfig.AntennaDownlinkDemodDecodeConfigProperty.SpectrumConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                antenna_downlink_demod_decode_config_property = groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                    decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                        unvalidated_json="unvalidatedJson"
                    ),
                    spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                        bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                            units="units",
                            value=123
                        ),
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if decode_config is not None:
                self._values["decode_config"] = decode_config
            if demodulation_config is not None:
                self._values["demodulation_config"] = demodulation_config
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config

        @builtins.property
        def decode_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.DecodeConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.AntennaDownlinkDemodDecodeConfigProperty.DecodeConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-decodeconfig
            '''
            result = self._values.get("decode_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.DecodeConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def demodulation_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.DemodulationConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.AntennaDownlinkDemodDecodeConfigProperty.DemodulationConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-demodulationconfig
            '''
            result = self._values.get("demodulation_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.DemodulationConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.AntennaDownlinkDemodDecodeConfigProperty.SpectrumConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.SpectrumConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaDownlinkDemodDecodeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.AntennaUplinkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "spectrum_config": "spectrumConfig",
            "target_eirp": "targetEirp",
            "transmit_disabled": "transmitDisabled",
        },
    )
    class AntennaUplinkConfigProperty:
        def __init__(
            self,
            *,
            spectrum_config: typing.Optional[typing.Union["CfnConfig.UplinkSpectrumConfigProperty", _IResolvable_da3f097b]] = None,
            target_eirp: typing.Optional[typing.Union["CfnConfig.EirpProperty", _IResolvable_da3f097b]] = None,
            transmit_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param spectrum_config: ``CfnConfig.AntennaUplinkConfigProperty.SpectrumConfig``.
            :param target_eirp: ``CfnConfig.AntennaUplinkConfigProperty.TargetEirp``.
            :param transmit_disabled: ``CfnConfig.AntennaUplinkConfigProperty.TransmitDisabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                antenna_uplink_config_property = groundstation.CfnConfig.AntennaUplinkConfigProperty(
                    spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                        center_frequency=groundstation.CfnConfig.FrequencyProperty(
                            units="units",
                            value=123
                        ),
                        polarization="polarization"
                    ),
                    target_eirp=groundstation.CfnConfig.EirpProperty(
                        units="units",
                        value=123
                    ),
                    transmit_disabled=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if spectrum_config is not None:
                self._values["spectrum_config"] = spectrum_config
            if target_eirp is not None:
                self._values["target_eirp"] = target_eirp
            if transmit_disabled is not None:
                self._values["transmit_disabled"] = transmit_disabled

        @builtins.property
        def spectrum_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.UplinkSpectrumConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.AntennaUplinkConfigProperty.SpectrumConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-spectrumconfig
            '''
            result = self._values.get("spectrum_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.UplinkSpectrumConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def target_eirp(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.EirpProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.AntennaUplinkConfigProperty.TargetEirp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-targeteirp
            '''
            result = self._values.get("target_eirp")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.EirpProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def transmit_disabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnConfig.AntennaUplinkConfigProperty.TransmitDisabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-transmitdisabled
            '''
            result = self._values.get("transmit_disabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AntennaUplinkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.ConfigDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "antenna_downlink_config": "antennaDownlinkConfig",
            "antenna_downlink_demod_decode_config": "antennaDownlinkDemodDecodeConfig",
            "antenna_uplink_config": "antennaUplinkConfig",
            "dataflow_endpoint_config": "dataflowEndpointConfig",
            "s3_recording_config": "s3RecordingConfig",
            "tracking_config": "trackingConfig",
            "uplink_echo_config": "uplinkEchoConfig",
        },
    )
    class ConfigDataProperty:
        def __init__(
            self,
            *,
            antenna_downlink_config: typing.Optional[typing.Union["CfnConfig.AntennaDownlinkConfigProperty", _IResolvable_da3f097b]] = None,
            antenna_downlink_demod_decode_config: typing.Optional[typing.Union["CfnConfig.AntennaDownlinkDemodDecodeConfigProperty", _IResolvable_da3f097b]] = None,
            antenna_uplink_config: typing.Optional[typing.Union["CfnConfig.AntennaUplinkConfigProperty", _IResolvable_da3f097b]] = None,
            dataflow_endpoint_config: typing.Optional[typing.Union["CfnConfig.DataflowEndpointConfigProperty", _IResolvable_da3f097b]] = None,
            s3_recording_config: typing.Optional[typing.Union["CfnConfig.S3RecordingConfigProperty", _IResolvable_da3f097b]] = None,
            tracking_config: typing.Optional[typing.Union["CfnConfig.TrackingConfigProperty", _IResolvable_da3f097b]] = None,
            uplink_echo_config: typing.Optional[typing.Union["CfnConfig.UplinkEchoConfigProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param antenna_downlink_config: ``CfnConfig.ConfigDataProperty.AntennaDownlinkConfig``.
            :param antenna_downlink_demod_decode_config: ``CfnConfig.ConfigDataProperty.AntennaDownlinkDemodDecodeConfig``.
            :param antenna_uplink_config: ``CfnConfig.ConfigDataProperty.AntennaUplinkConfig``.
            :param dataflow_endpoint_config: ``CfnConfig.ConfigDataProperty.DataflowEndpointConfig``.
            :param s3_recording_config: ``CfnConfig.ConfigDataProperty.S3RecordingConfig``.
            :param tracking_config: ``CfnConfig.ConfigDataProperty.TrackingConfig``.
            :param uplink_echo_config: ``CfnConfig.ConfigDataProperty.UplinkEchoConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                config_data_property = groundstation.CfnConfig.ConfigDataProperty(
                    antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                        decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        ),
                        target_eirp=groundstation.CfnConfig.EirpProperty(
                            units="units",
                            value=123
                        ),
                        transmit_disabled=False
                    ),
                    dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                        dataflow_endpoint_name="dataflowEndpointName",
                        dataflow_endpoint_region="dataflowEndpointRegion"
                    ),
                    s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                        bucket_arn="bucketArn",
                        prefix="prefix",
                        role_arn="roleArn"
                    ),
                    tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                        autotrack="autotrack"
                    ),
                    uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                        antenna_uplink_config_arn="antennaUplinkConfigArn",
                        enabled=False
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if antenna_downlink_config is not None:
                self._values["antenna_downlink_config"] = antenna_downlink_config
            if antenna_downlink_demod_decode_config is not None:
                self._values["antenna_downlink_demod_decode_config"] = antenna_downlink_demod_decode_config
            if antenna_uplink_config is not None:
                self._values["antenna_uplink_config"] = antenna_uplink_config
            if dataflow_endpoint_config is not None:
                self._values["dataflow_endpoint_config"] = dataflow_endpoint_config
            if s3_recording_config is not None:
                self._values["s3_recording_config"] = s3_recording_config
            if tracking_config is not None:
                self._values["tracking_config"] = tracking_config
            if uplink_echo_config is not None:
                self._values["uplink_echo_config"] = uplink_echo_config

        @builtins.property
        def antenna_downlink_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.AntennaDownlinkConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.ConfigDataProperty.AntennaDownlinkConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennadownlinkconfig
            '''
            result = self._values.get("antenna_downlink_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.AntennaDownlinkConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def antenna_downlink_demod_decode_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.AntennaDownlinkDemodDecodeConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.ConfigDataProperty.AntennaDownlinkDemodDecodeConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennadownlinkdemoddecodeconfig
            '''
            result = self._values.get("antenna_downlink_demod_decode_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.AntennaDownlinkDemodDecodeConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def antenna_uplink_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.AntennaUplinkConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.ConfigDataProperty.AntennaUplinkConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennauplinkconfig
            '''
            result = self._values.get("antenna_uplink_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.AntennaUplinkConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def dataflow_endpoint_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.DataflowEndpointConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.ConfigDataProperty.DataflowEndpointConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-dataflowendpointconfig
            '''
            result = self._values.get("dataflow_endpoint_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.DataflowEndpointConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_recording_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.S3RecordingConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.ConfigDataProperty.S3RecordingConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-s3recordingconfig
            '''
            result = self._values.get("s3_recording_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.S3RecordingConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def tracking_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.TrackingConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.ConfigDataProperty.TrackingConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-trackingconfig
            '''
            result = self._values.get("tracking_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.TrackingConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def uplink_echo_config(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.UplinkEchoConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.ConfigDataProperty.UplinkEchoConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-uplinkechoconfig
            '''
            result = self._values.get("uplink_echo_config")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.UplinkEchoConfigProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.DataflowEndpointConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dataflow_endpoint_name": "dataflowEndpointName",
            "dataflow_endpoint_region": "dataflowEndpointRegion",
        },
    )
    class DataflowEndpointConfigProperty:
        def __init__(
            self,
            *,
            dataflow_endpoint_name: typing.Optional[builtins.str] = None,
            dataflow_endpoint_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param dataflow_endpoint_name: ``CfnConfig.DataflowEndpointConfigProperty.DataflowEndpointName``.
            :param dataflow_endpoint_region: ``CfnConfig.DataflowEndpointConfigProperty.DataflowEndpointRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                dataflow_endpoint_config_property = groundstation.CfnConfig.DataflowEndpointConfigProperty(
                    dataflow_endpoint_name="dataflowEndpointName",
                    dataflow_endpoint_region="dataflowEndpointRegion"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dataflow_endpoint_name is not None:
                self._values["dataflow_endpoint_name"] = dataflow_endpoint_name
            if dataflow_endpoint_region is not None:
                self._values["dataflow_endpoint_region"] = dataflow_endpoint_region

        @builtins.property
        def dataflow_endpoint_name(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.DataflowEndpointConfigProperty.DataflowEndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointname
            '''
            result = self._values.get("dataflow_endpoint_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dataflow_endpoint_region(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.DataflowEndpointConfigProperty.DataflowEndpointRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointregion
            '''
            result = self._values.get("dataflow_endpoint_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEndpointConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.DecodeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"unvalidated_json": "unvalidatedJson"},
    )
    class DecodeConfigProperty:
        def __init__(
            self,
            *,
            unvalidated_json: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param unvalidated_json: ``CfnConfig.DecodeConfigProperty.UnvalidatedJSON``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                decode_config_property = groundstation.CfnConfig.DecodeConfigProperty(
                    unvalidated_json="unvalidatedJson"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if unvalidated_json is not None:
                self._values["unvalidated_json"] = unvalidated_json

        @builtins.property
        def unvalidated_json(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.DecodeConfigProperty.UnvalidatedJSON``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html#cfn-groundstation-config-decodeconfig-unvalidatedjson
            '''
            result = self._values.get("unvalidated_json")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DecodeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.DemodulationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"unvalidated_json": "unvalidatedJson"},
    )
    class DemodulationConfigProperty:
        def __init__(
            self,
            *,
            unvalidated_json: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param unvalidated_json: ``CfnConfig.DemodulationConfigProperty.UnvalidatedJSON``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                demodulation_config_property = groundstation.CfnConfig.DemodulationConfigProperty(
                    unvalidated_json="unvalidatedJson"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if unvalidated_json is not None:
                self._values["unvalidated_json"] = unvalidated_json

        @builtins.property
        def unvalidated_json(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.DemodulationConfigProperty.UnvalidatedJSON``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html#cfn-groundstation-config-demodulationconfig-unvalidatedjson
            '''
            result = self._values.get("unvalidated_json")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DemodulationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.EirpProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class EirpProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param units: ``CfnConfig.EirpProperty.Units``.
            :param value: ``CfnConfig.EirpProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                eirp_property = groundstation.CfnConfig.EirpProperty(
                    units="units",
                    value=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.EirpProperty.Units``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html#cfn-groundstation-config-eirp-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''``CfnConfig.EirpProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html#cfn-groundstation-config-eirp-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EirpProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.FrequencyBandwidthProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class FrequencyBandwidthProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param units: ``CfnConfig.FrequencyBandwidthProperty.Units``.
            :param value: ``CfnConfig.FrequencyBandwidthProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                frequency_bandwidth_property = groundstation.CfnConfig.FrequencyBandwidthProperty(
                    units="units",
                    value=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.FrequencyBandwidthProperty.Units``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html#cfn-groundstation-config-frequencybandwidth-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''``CfnConfig.FrequencyBandwidthProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html#cfn-groundstation-config-frequencybandwidth-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrequencyBandwidthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.FrequencyProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units", "value": "value"},
    )
    class FrequencyProperty:
        def __init__(
            self,
            *,
            units: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param units: ``CfnConfig.FrequencyProperty.Units``.
            :param value: ``CfnConfig.FrequencyProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                frequency_property = groundstation.CfnConfig.FrequencyProperty(
                    units="units",
                    value=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.FrequencyProperty.Units``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html#cfn-groundstation-config-frequency-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''``CfnConfig.FrequencyProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html#cfn-groundstation-config-frequency-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrequencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.S3RecordingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "prefix": "prefix",
            "role_arn": "roleArn",
        },
    )
    class S3RecordingConfigProperty:
        def __init__(
            self,
            *,
            bucket_arn: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket_arn: ``CfnConfig.S3RecordingConfigProperty.BucketArn``.
            :param prefix: ``CfnConfig.S3RecordingConfigProperty.Prefix``.
            :param role_arn: ``CfnConfig.S3RecordingConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                s3_recording_config_property = groundstation.CfnConfig.S3RecordingConfigProperty(
                    bucket_arn="bucketArn",
                    prefix="prefix",
                    role_arn="roleArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bucket_arn is not None:
                self._values["bucket_arn"] = bucket_arn
            if prefix is not None:
                self._values["prefix"] = prefix
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def bucket_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.S3RecordingConfigProperty.BucketArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-bucketarn
            '''
            result = self._values.get("bucket_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.S3RecordingConfigProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.S3RecordingConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3RecordingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.SpectrumConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bandwidth": "bandwidth",
            "center_frequency": "centerFrequency",
            "polarization": "polarization",
        },
    )
    class SpectrumConfigProperty:
        def __init__(
            self,
            *,
            bandwidth: typing.Optional[typing.Union["CfnConfig.FrequencyBandwidthProperty", _IResolvable_da3f097b]] = None,
            center_frequency: typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_da3f097b]] = None,
            polarization: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bandwidth: ``CfnConfig.SpectrumConfigProperty.Bandwidth``.
            :param center_frequency: ``CfnConfig.SpectrumConfigProperty.CenterFrequency``.
            :param polarization: ``CfnConfig.SpectrumConfigProperty.Polarization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                spectrum_config_property = groundstation.CfnConfig.SpectrumConfigProperty(
                    bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                        units="units",
                        value=123
                    ),
                    center_frequency=groundstation.CfnConfig.FrequencyProperty(
                        units="units",
                        value=123
                    ),
                    polarization="polarization"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bandwidth is not None:
                self._values["bandwidth"] = bandwidth
            if center_frequency is not None:
                self._values["center_frequency"] = center_frequency
            if polarization is not None:
                self._values["polarization"] = polarization

        @builtins.property
        def bandwidth(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.FrequencyBandwidthProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.SpectrumConfigProperty.Bandwidth``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-bandwidth
            '''
            result = self._values.get("bandwidth")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.FrequencyBandwidthProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def center_frequency(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.SpectrumConfigProperty.CenterFrequency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-centerfrequency
            '''
            result = self._values.get("center_frequency")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def polarization(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.SpectrumConfigProperty.Polarization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-polarization
            '''
            result = self._values.get("polarization")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpectrumConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.TrackingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"autotrack": "autotrack"},
    )
    class TrackingConfigProperty:
        def __init__(self, *, autotrack: typing.Optional[builtins.str] = None) -> None:
            '''
            :param autotrack: ``CfnConfig.TrackingConfigProperty.Autotrack``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                tracking_config_property = groundstation.CfnConfig.TrackingConfigProperty(
                    autotrack="autotrack"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if autotrack is not None:
                self._values["autotrack"] = autotrack

        @builtins.property
        def autotrack(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.TrackingConfigProperty.Autotrack``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html#cfn-groundstation-config-trackingconfig-autotrack
            '''
            result = self._values.get("autotrack")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrackingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.UplinkEchoConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "antenna_uplink_config_arn": "antennaUplinkConfigArn",
            "enabled": "enabled",
        },
    )
    class UplinkEchoConfigProperty:
        def __init__(
            self,
            *,
            antenna_uplink_config_arn: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param antenna_uplink_config_arn: ``CfnConfig.UplinkEchoConfigProperty.AntennaUplinkConfigArn``.
            :param enabled: ``CfnConfig.UplinkEchoConfigProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                uplink_echo_config_property = groundstation.CfnConfig.UplinkEchoConfigProperty(
                    antenna_uplink_config_arn="antennaUplinkConfigArn",
                    enabled=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if antenna_uplink_config_arn is not None:
                self._values["antenna_uplink_config_arn"] = antenna_uplink_config_arn
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def antenna_uplink_config_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.UplinkEchoConfigProperty.AntennaUplinkConfigArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html#cfn-groundstation-config-uplinkechoconfig-antennauplinkconfigarn
            '''
            result = self._values.get("antenna_uplink_config_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnConfig.UplinkEchoConfigProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html#cfn-groundstation-config-uplinkechoconfig-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UplinkEchoConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnConfig.UplinkSpectrumConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "center_frequency": "centerFrequency",
            "polarization": "polarization",
        },
    )
    class UplinkSpectrumConfigProperty:
        def __init__(
            self,
            *,
            center_frequency: typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_da3f097b]] = None,
            polarization: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param center_frequency: ``CfnConfig.UplinkSpectrumConfigProperty.CenterFrequency``.
            :param polarization: ``CfnConfig.UplinkSpectrumConfigProperty.Polarization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                uplink_spectrum_config_property = groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                    center_frequency=groundstation.CfnConfig.FrequencyProperty(
                        units="units",
                        value=123
                    ),
                    polarization="polarization"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if center_frequency is not None:
                self._values["center_frequency"] = center_frequency
            if polarization is not None:
                self._values["polarization"] = polarization

        @builtins.property
        def center_frequency(
            self,
        ) -> typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_da3f097b]]:
            '''``CfnConfig.UplinkSpectrumConfigProperty.CenterFrequency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html#cfn-groundstation-config-uplinkspectrumconfig-centerfrequency
            '''
            result = self._values.get("center_frequency")
            return typing.cast(typing.Optional[typing.Union["CfnConfig.FrequencyProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def polarization(self) -> typing.Optional[builtins.str]:
            '''``CfnConfig.UplinkSpectrumConfigProperty.Polarization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html#cfn-groundstation-config-uplinkspectrumconfig-polarization
            '''
            result = self._values.get("polarization")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UplinkSpectrumConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_groundstation.CfnConfigProps",
    jsii_struct_bases=[],
    name_mapping={"config_data": "configData", "name": "name", "tags": "tags"},
)
class CfnConfigProps:
    def __init__(
        self,
        *,
        config_data: typing.Union[CfnConfig.ConfigDataProperty, _IResolvable_da3f097b],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GroundStation::Config``.

        :param config_data: ``AWS::GroundStation::Config.ConfigData``.
        :param name: ``AWS::GroundStation::Config.Name``.
        :param tags: ``AWS::GroundStation::Config.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_groundstation as groundstation
            
            cfn_config_props = groundstation.CfnConfigProps(
                config_data=groundstation.CfnConfig.ConfigDataProperty(
                    antenna_downlink_config=groundstation.CfnConfig.AntennaDownlinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_downlink_demod_decode_config=groundstation.CfnConfig.AntennaDownlinkDemodDecodeConfigProperty(
                        decode_config=groundstation.CfnConfig.DecodeConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        demodulation_config=groundstation.CfnConfig.DemodulationConfigProperty(
                            unvalidated_json="unvalidatedJson"
                        ),
                        spectrum_config=groundstation.CfnConfig.SpectrumConfigProperty(
                            bandwidth=groundstation.CfnConfig.FrequencyBandwidthProperty(
                                units="units",
                                value=123
                            ),
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        )
                    ),
                    antenna_uplink_config=groundstation.CfnConfig.AntennaUplinkConfigProperty(
                        spectrum_config=groundstation.CfnConfig.UplinkSpectrumConfigProperty(
                            center_frequency=groundstation.CfnConfig.FrequencyProperty(
                                units="units",
                                value=123
                            ),
                            polarization="polarization"
                        ),
                        target_eirp=groundstation.CfnConfig.EirpProperty(
                            units="units",
                            value=123
                        ),
                        transmit_disabled=False
                    ),
                    dataflow_endpoint_config=groundstation.CfnConfig.DataflowEndpointConfigProperty(
                        dataflow_endpoint_name="dataflowEndpointName",
                        dataflow_endpoint_region="dataflowEndpointRegion"
                    ),
                    s3_recording_config=groundstation.CfnConfig.S3RecordingConfigProperty(
                        bucket_arn="bucketArn",
                        prefix="prefix",
                        role_arn="roleArn"
                    ),
                    tracking_config=groundstation.CfnConfig.TrackingConfigProperty(
                        autotrack="autotrack"
                    ),
                    uplink_echo_config=groundstation.CfnConfig.UplinkEchoConfigProperty(
                        antenna_uplink_config_arn="antennaUplinkConfigArn",
                        enabled=False
                    )
                ),
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "config_data": config_data,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def config_data(
        self,
    ) -> typing.Union[CfnConfig.ConfigDataProperty, _IResolvable_da3f097b]:
        '''``AWS::GroundStation::Config.ConfigData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-configdata
        '''
        result = self._values.get("config_data")
        assert result is not None, "Required property 'config_data' is missing"
        return typing.cast(typing.Union[CfnConfig.ConfigDataProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::GroundStation::Config.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::GroundStation::Config.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDataflowEndpointGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup",
):
    '''A CloudFormation ``AWS::GroundStation::DataflowEndpointGroup``.

    :cloudformationResource: AWS::GroundStation::DataflowEndpointGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_groundstation as groundstation
        
        cfn_dataflow_endpoint_group = groundstation.CfnDataflowEndpointGroup(self, "MyCfnDataflowEndpointGroup",
            endpoint_details=[groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                    address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                        name="name",
                        port=123
                    ),
                    mtu=123,
                    name="name"
                ),
                security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )],
        
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
        endpoint_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", _IResolvable_da3f097b]]],
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::GroundStation::DataflowEndpointGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_details: ``AWS::GroundStation::DataflowEndpointGroup.EndpointDetails``.
        :param tags: ``AWS::GroundStation::DataflowEndpointGroup.Tags``.
        '''
        props = CfnDataflowEndpointGroupProps(
            endpoint_details=endpoint_details, tags=tags
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="endpointDetails")
    def endpoint_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", _IResolvable_da3f097b]]]:
        '''``AWS::GroundStation::DataflowEndpointGroup.EndpointDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-endpointdetails
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", _IResolvable_da3f097b]]], jsii.get(self, "endpointDetails"))

    @endpoint_details.setter
    def endpoint_details(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataflowEndpointGroup.EndpointDetailsProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "endpointDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::GroundStation::DataflowEndpointGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "mtu": "mtu", "name": "name"},
    )
    class DataflowEndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[typing.Union["CfnDataflowEndpointGroup.SocketAddressProperty", _IResolvable_da3f097b]] = None,
            mtu: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param address: ``CfnDataflowEndpointGroup.DataflowEndpointProperty.Address``.
            :param mtu: ``CfnDataflowEndpointGroup.DataflowEndpointProperty.Mtu``.
            :param name: ``CfnDataflowEndpointGroup.DataflowEndpointProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                dataflow_endpoint_property = groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                    address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                        name="name",
                        port=123
                    ),
                    mtu=123,
                    name="name"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if mtu is not None:
                self._values["mtu"] = mtu
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def address(
            self,
        ) -> typing.Optional[typing.Union["CfnDataflowEndpointGroup.SocketAddressProperty", _IResolvable_da3f097b]]:
            '''``CfnDataflowEndpointGroup.DataflowEndpointProperty.Address``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[typing.Union["CfnDataflowEndpointGroup.SocketAddressProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def mtu(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataflowEndpointGroup.DataflowEndpointProperty.Mtu``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-mtu
            '''
            result = self._values.get("mtu")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataflowEndpointGroup.DataflowEndpointProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint": "endpoint", "security_details": "securityDetails"},
    )
    class EndpointDetailsProperty:
        def __init__(
            self,
            *,
            endpoint: typing.Optional[typing.Union["CfnDataflowEndpointGroup.DataflowEndpointProperty", _IResolvable_da3f097b]] = None,
            security_details: typing.Optional[typing.Union["CfnDataflowEndpointGroup.SecurityDetailsProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param endpoint: ``CfnDataflowEndpointGroup.EndpointDetailsProperty.Endpoint``.
            :param security_details: ``CfnDataflowEndpointGroup.EndpointDetailsProperty.SecurityDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                endpoint_details_property = groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                    endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                        address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                            name="name",
                            port=123
                        ),
                        mtu=123,
                        name="name"
                    ),
                    security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if security_details is not None:
                self._values["security_details"] = security_details

        @builtins.property
        def endpoint(
            self,
        ) -> typing.Optional[typing.Union["CfnDataflowEndpointGroup.DataflowEndpointProperty", _IResolvable_da3f097b]]:
            '''``CfnDataflowEndpointGroup.EndpointDetailsProperty.Endpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[typing.Union["CfnDataflowEndpointGroup.DataflowEndpointProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def security_details(
            self,
        ) -> typing.Optional[typing.Union["CfnDataflowEndpointGroup.SecurityDetailsProperty", _IResolvable_da3f097b]]:
            '''``CfnDataflowEndpointGroup.EndpointDetailsProperty.SecurityDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-securitydetails
            '''
            result = self._values.get("security_details")
            return typing.cast(typing.Optional[typing.Union["CfnDataflowEndpointGroup.SecurityDetailsProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class SecurityDetailsProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param role_arn: ``CfnDataflowEndpointGroup.SecurityDetailsProperty.RoleArn``.
            :param security_group_ids: ``CfnDataflowEndpointGroup.SecurityDetailsProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnDataflowEndpointGroup.SecurityDetailsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                security_details_property = groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDataflowEndpointGroup.SecurityDetailsProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataflowEndpointGroup.SecurityDetailsProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataflowEndpointGroup.SecurityDetailsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecurityDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroup.SocketAddressProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "port": "port"},
    )
    class SocketAddressProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param name: ``CfnDataflowEndpointGroup.SocketAddressProperty.Name``.
            :param port: ``CfnDataflowEndpointGroup.SocketAddressProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                socket_address_property = groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                    name="name",
                    port=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataflowEndpointGroup.SocketAddressProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html#cfn-groundstation-dataflowendpointgroup-socketaddress-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataflowEndpointGroup.SocketAddressProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html#cfn-groundstation-dataflowendpointgroup-socketaddress-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SocketAddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_groundstation.CfnDataflowEndpointGroupProps",
    jsii_struct_bases=[],
    name_mapping={"endpoint_details": "endpointDetails", "tags": "tags"},
)
class CfnDataflowEndpointGroupProps:
    def __init__(
        self,
        *,
        endpoint_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, _IResolvable_da3f097b]]],
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GroundStation::DataflowEndpointGroup``.

        :param endpoint_details: ``AWS::GroundStation::DataflowEndpointGroup.EndpointDetails``.
        :param tags: ``AWS::GroundStation::DataflowEndpointGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_groundstation as groundstation
            
            cfn_dataflow_endpoint_group_props = groundstation.CfnDataflowEndpointGroupProps(
                endpoint_details=[groundstation.CfnDataflowEndpointGroup.EndpointDetailsProperty(
                    endpoint=groundstation.CfnDataflowEndpointGroup.DataflowEndpointProperty(
                        address=groundstation.CfnDataflowEndpointGroup.SocketAddressProperty(
                            name="name",
                            port=123
                        ),
                        mtu=123,
                        name="name"
                    ),
                    security_details=groundstation.CfnDataflowEndpointGroup.SecurityDetailsProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )],
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_details": endpoint_details,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def endpoint_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, _IResolvable_da3f097b]]]:
        '''``AWS::GroundStation::DataflowEndpointGroup.EndpointDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-endpointdetails
        '''
        result = self._values.get("endpoint_details")
        assert result is not None, "Required property 'endpoint_details' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDataflowEndpointGroup.EndpointDetailsProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::GroundStation::DataflowEndpointGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataflowEndpointGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMissionProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_groundstation.CfnMissionProfile",
):
    '''A CloudFormation ``AWS::GroundStation::MissionProfile``.

    :cloudformationResource: AWS::GroundStation::MissionProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_groundstation as groundstation
        
        cfn_mission_profile = groundstation.CfnMissionProfile(self, "MyCfnMissionProfile",
            dataflow_edges=[groundstation.CfnMissionProfile.DataflowEdgeProperty(
                destination="destination",
                source="source"
            )],
            minimum_viable_contact_duration_seconds=123,
            name="name",
            tracking_config_arn="trackingConfigArn",
        
            # the properties below are optional
            contact_post_pass_duration_seconds=123,
            contact_pre_pass_duration_seconds=123,
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
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        dataflow_edges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnMissionProfile.DataflowEdgeProperty", _IResolvable_da3f097b]]],
        minimum_viable_contact_duration_seconds: jsii.Number,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        tracking_config_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::GroundStation::MissionProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param contact_post_pass_duration_seconds: ``AWS::GroundStation::MissionProfile.ContactPostPassDurationSeconds``.
        :param contact_pre_pass_duration_seconds: ``AWS::GroundStation::MissionProfile.ContactPrePassDurationSeconds``.
        :param dataflow_edges: ``AWS::GroundStation::MissionProfile.DataflowEdges``.
        :param minimum_viable_contact_duration_seconds: ``AWS::GroundStation::MissionProfile.MinimumViableContactDurationSeconds``.
        :param name: ``AWS::GroundStation::MissionProfile.Name``.
        :param tags: ``AWS::GroundStation::MissionProfile.Tags``.
        :param tracking_config_arn: ``AWS::GroundStation::MissionProfile.TrackingConfigArn``.
        '''
        props = CfnMissionProfileProps(
            contact_post_pass_duration_seconds=contact_post_pass_duration_seconds,
            contact_pre_pass_duration_seconds=contact_pre_pass_duration_seconds,
            dataflow_edges=dataflow_edges,
            minimum_viable_contact_duration_seconds=minimum_viable_contact_duration_seconds,
            name=name,
            tags=tags,
            tracking_config_arn=tracking_config_arn,
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRegion")
    def attr_region(self) -> builtins.str:
        '''
        :cloudformationAttribute: Region
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegion"))

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
    @jsii.member(jsii_name="contactPostPassDurationSeconds")
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GroundStation::MissionProfile.ContactPostPassDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactpostpassdurationseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPostPassDurationSeconds"))

    @contact_post_pass_duration_seconds.setter
    def contact_post_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "contactPostPassDurationSeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactPrePassDurationSeconds")
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GroundStation::MissionProfile.ContactPrePassDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactprepassdurationseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contactPrePassDurationSeconds"))

    @contact_pre_pass_duration_seconds.setter
    def contact_pre_pass_duration_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "contactPrePassDurationSeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataflowEdges")
    def dataflow_edges(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMissionProfile.DataflowEdgeProperty", _IResolvable_da3f097b]]]:
        '''``AWS::GroundStation::MissionProfile.DataflowEdges``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-dataflowedges
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMissionProfile.DataflowEdgeProperty", _IResolvable_da3f097b]]], jsii.get(self, "dataflowEdges"))

    @dataflow_edges.setter
    def dataflow_edges(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMissionProfile.DataflowEdgeProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "dataflowEdges", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minimumViableContactDurationSeconds")
    def minimum_viable_contact_duration_seconds(self) -> jsii.Number:
        '''``AWS::GroundStation::MissionProfile.MinimumViableContactDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-minimumviablecontactdurationseconds
        '''
        return typing.cast(jsii.Number, jsii.get(self, "minimumViableContactDurationSeconds"))

    @minimum_viable_contact_duration_seconds.setter
    def minimum_viable_contact_duration_seconds(self, value: jsii.Number) -> None:
        jsii.set(self, "minimumViableContactDurationSeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::GroundStation::MissionProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::GroundStation::MissionProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trackingConfigArn")
    def tracking_config_arn(self) -> builtins.str:
        '''``AWS::GroundStation::MissionProfile.TrackingConfigArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-trackingconfigarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "trackingConfigArn"))

    @tracking_config_arn.setter
    def tracking_config_arn(self, value: builtins.str) -> None:
        jsii.set(self, "trackingConfigArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_groundstation.CfnMissionProfile.DataflowEdgeProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "source": "source"},
    )
    class DataflowEdgeProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination: ``CfnMissionProfile.DataflowEdgeProperty.Destination``.
            :param source: ``CfnMissionProfile.DataflowEdgeProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_groundstation as groundstation
                
                dataflow_edge_property = groundstation.CfnMissionProfile.DataflowEdgeProperty(
                    destination="destination",
                    source="source"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            '''``CfnMissionProfile.DataflowEdgeProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html#cfn-groundstation-missionprofile-dataflowedge-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''``CfnMissionProfile.DataflowEdgeProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html#cfn-groundstation-missionprofile-dataflowedge-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataflowEdgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_groundstation.CfnMissionProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "contact_post_pass_duration_seconds": "contactPostPassDurationSeconds",
        "contact_pre_pass_duration_seconds": "contactPrePassDurationSeconds",
        "dataflow_edges": "dataflowEdges",
        "minimum_viable_contact_duration_seconds": "minimumViableContactDurationSeconds",
        "name": "name",
        "tags": "tags",
        "tracking_config_arn": "trackingConfigArn",
    },
)
class CfnMissionProfileProps:
    def __init__(
        self,
        *,
        contact_post_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        contact_pre_pass_duration_seconds: typing.Optional[jsii.Number] = None,
        dataflow_edges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnMissionProfile.DataflowEdgeProperty, _IResolvable_da3f097b]]],
        minimum_viable_contact_duration_seconds: jsii.Number,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        tracking_config_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::GroundStation::MissionProfile``.

        :param contact_post_pass_duration_seconds: ``AWS::GroundStation::MissionProfile.ContactPostPassDurationSeconds``.
        :param contact_pre_pass_duration_seconds: ``AWS::GroundStation::MissionProfile.ContactPrePassDurationSeconds``.
        :param dataflow_edges: ``AWS::GroundStation::MissionProfile.DataflowEdges``.
        :param minimum_viable_contact_duration_seconds: ``AWS::GroundStation::MissionProfile.MinimumViableContactDurationSeconds``.
        :param name: ``AWS::GroundStation::MissionProfile.Name``.
        :param tags: ``AWS::GroundStation::MissionProfile.Tags``.
        :param tracking_config_arn: ``AWS::GroundStation::MissionProfile.TrackingConfigArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_groundstation as groundstation
            
            cfn_mission_profile_props = groundstation.CfnMissionProfileProps(
                dataflow_edges=[groundstation.CfnMissionProfile.DataflowEdgeProperty(
                    destination="destination",
                    source="source"
                )],
                minimum_viable_contact_duration_seconds=123,
                name="name",
                tracking_config_arn="trackingConfigArn",
            
                # the properties below are optional
                contact_post_pass_duration_seconds=123,
                contact_pre_pass_duration_seconds=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dataflow_edges": dataflow_edges,
            "minimum_viable_contact_duration_seconds": minimum_viable_contact_duration_seconds,
            "name": name,
            "tracking_config_arn": tracking_config_arn,
        }
        if contact_post_pass_duration_seconds is not None:
            self._values["contact_post_pass_duration_seconds"] = contact_post_pass_duration_seconds
        if contact_pre_pass_duration_seconds is not None:
            self._values["contact_pre_pass_duration_seconds"] = contact_pre_pass_duration_seconds
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def contact_post_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GroundStation::MissionProfile.ContactPostPassDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactpostpassdurationseconds
        '''
        result = self._values.get("contact_post_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def contact_pre_pass_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''``AWS::GroundStation::MissionProfile.ContactPrePassDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactprepassdurationseconds
        '''
        result = self._values.get("contact_pre_pass_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dataflow_edges(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMissionProfile.DataflowEdgeProperty, _IResolvable_da3f097b]]]:
        '''``AWS::GroundStation::MissionProfile.DataflowEdges``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-dataflowedges
        '''
        result = self._values.get("dataflow_edges")
        assert result is not None, "Required property 'dataflow_edges' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMissionProfile.DataflowEdgeProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def minimum_viable_contact_duration_seconds(self) -> jsii.Number:
        '''``AWS::GroundStation::MissionProfile.MinimumViableContactDurationSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-minimumviablecontactdurationseconds
        '''
        result = self._values.get("minimum_viable_contact_duration_seconds")
        assert result is not None, "Required property 'minimum_viable_contact_duration_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::GroundStation::MissionProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::GroundStation::MissionProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def tracking_config_arn(self) -> builtins.str:
        '''``AWS::GroundStation::MissionProfile.TrackingConfigArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-trackingconfigarn
        '''
        result = self._values.get("tracking_config_arn")
        assert result is not None, "Required property 'tracking_config_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMissionProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfig",
    "CfnConfigProps",
    "CfnDataflowEndpointGroup",
    "CfnDataflowEndpointGroupProps",
    "CfnMissionProfile",
    "CfnMissionProfileProps",
]

publication.publish()
