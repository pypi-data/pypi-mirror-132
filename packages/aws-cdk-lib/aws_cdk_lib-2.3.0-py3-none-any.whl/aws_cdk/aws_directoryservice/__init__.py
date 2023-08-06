'''
# AWS Directory Service Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_directoryservice as directoryservice
```

> The construct library for this service is in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package named:
>
> ```
> @aws-cdk/aws-directoryservice-alpha
> ```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DirectoryService](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectoryService.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnMicrosoftAD(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directoryservice.CfnMicrosoftAD",
):
    '''A CloudFormation ``AWS::DirectoryService::MicrosoftAD``.

    :cloudformationResource: AWS::DirectoryService::MicrosoftAD
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directoryservice as directoryservice
        
        cfn_microsoft_aD = directoryservice.CfnMicrosoftAD(self, "MyCfnMicrosoftAD",
            name="name",
            password="password",
            vpc_settings=directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            create_alias=False,
            edition="edition",
            enable_sso=False,
            short_name="shortName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: builtins.str,
        password: builtins.str,
        short_name: typing.Optional[builtins.str] = None,
        vpc_settings: typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _IResolvable_da3f097b],
    ) -> None:
        '''Create a new ``AWS::DirectoryService::MicrosoftAD``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param create_alias: ``AWS::DirectoryService::MicrosoftAD.CreateAlias``.
        :param edition: ``AWS::DirectoryService::MicrosoftAD.Edition``.
        :param enable_sso: ``AWS::DirectoryService::MicrosoftAD.EnableSso``.
        :param name: ``AWS::DirectoryService::MicrosoftAD.Name``.
        :param password: ``AWS::DirectoryService::MicrosoftAD.Password``.
        :param short_name: ``AWS::DirectoryService::MicrosoftAD.ShortName``.
        :param vpc_settings: ``AWS::DirectoryService::MicrosoftAD.VpcSettings``.
        '''
        props = CfnMicrosoftADProps(
            create_alias=create_alias,
            edition=edition,
            enable_sso=enable_sso,
            name=name,
            password=password,
            short_name=short_name,
            vpc_settings=vpc_settings,
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
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''
        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

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
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::DirectoryService::MicrosoftAD.CreateAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "createAlias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="edition")
    def edition(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::MicrosoftAD.Edition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "edition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::DirectoryService::MicrosoftAD.EnableSso``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "enableSso", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::DirectoryService::MicrosoftAD.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''``AWS::DirectoryService::MicrosoftAD.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        jsii.set(self, "password", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::MicrosoftAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "shortName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _IResolvable_da3f097b]:
        '''``AWS::DirectoryService::MicrosoftAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        return typing.cast(typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _IResolvable_da3f097b], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "vpcSettings", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_directoryservice.CfnMicrosoftAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''
            :param subnet_ids: ``CfnMicrosoftAD.VpcSettingsProperty.SubnetIds``.
            :param vpc_id: ``CfnMicrosoftAD.VpcSettingsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_directoryservice as directoryservice
                
                vpc_settings_property = directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''``CfnMicrosoftAD.VpcSettingsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''``CfnMicrosoftAD.VpcSettingsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directoryservice.CfnMicrosoftADProps",
    jsii_struct_bases=[],
    name_mapping={
        "create_alias": "createAlias",
        "edition": "edition",
        "enable_sso": "enableSso",
        "name": "name",
        "password": "password",
        "short_name": "shortName",
        "vpc_settings": "vpcSettings",
    },
)
class CfnMicrosoftADProps:
    def __init__(
        self,
        *,
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: builtins.str,
        password: builtins.str,
        short_name: typing.Optional[builtins.str] = None,
        vpc_settings: typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _IResolvable_da3f097b],
    ) -> None:
        '''Properties for defining a ``AWS::DirectoryService::MicrosoftAD``.

        :param create_alias: ``AWS::DirectoryService::MicrosoftAD.CreateAlias``.
        :param edition: ``AWS::DirectoryService::MicrosoftAD.Edition``.
        :param enable_sso: ``AWS::DirectoryService::MicrosoftAD.EnableSso``.
        :param name: ``AWS::DirectoryService::MicrosoftAD.Name``.
        :param password: ``AWS::DirectoryService::MicrosoftAD.Password``.
        :param short_name: ``AWS::DirectoryService::MicrosoftAD.ShortName``.
        :param vpc_settings: ``AWS::DirectoryService::MicrosoftAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directoryservice as directoryservice
            
            cfn_microsoft_aDProps = directoryservice.CfnMicrosoftADProps(
                name="name",
                password="password",
                vpc_settings=directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                create_alias=False,
                edition="edition",
                enable_sso=False,
                short_name="shortName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "password": password,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if edition is not None:
            self._values["edition"] = edition
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::DirectoryService::MicrosoftAD.CreateAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::MicrosoftAD.Edition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::DirectoryService::MicrosoftAD.EnableSso``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::DirectoryService::MicrosoftAD.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''``AWS::DirectoryService::MicrosoftAD.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::MicrosoftAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _IResolvable_da3f097b]:
        '''``AWS::DirectoryService::MicrosoftAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _IResolvable_da3f097b], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMicrosoftADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSimpleAD(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directoryservice.CfnSimpleAD",
):
    '''A CloudFormation ``AWS::DirectoryService::SimpleAD``.

    :cloudformationResource: AWS::DirectoryService::SimpleAD
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directoryservice as directoryservice
        
        cfn_simple_aD = directoryservice.CfnSimpleAD(self, "MyCfnSimpleAD",
            name="name",
            password="password",
            size="size",
            vpc_settings=directoryservice.CfnSimpleAD.VpcSettingsProperty(
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            create_alias=False,
            description="description",
            enable_sso=False,
            short_name="shortName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: builtins.str,
        password: builtins.str,
        short_name: typing.Optional[builtins.str] = None,
        size: builtins.str,
        vpc_settings: typing.Union["CfnSimpleAD.VpcSettingsProperty", _IResolvable_da3f097b],
    ) -> None:
        '''Create a new ``AWS::DirectoryService::SimpleAD``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param create_alias: ``AWS::DirectoryService::SimpleAD.CreateAlias``.
        :param description: ``AWS::DirectoryService::SimpleAD.Description``.
        :param enable_sso: ``AWS::DirectoryService::SimpleAD.EnableSso``.
        :param name: ``AWS::DirectoryService::SimpleAD.Name``.
        :param password: ``AWS::DirectoryService::SimpleAD.Password``.
        :param short_name: ``AWS::DirectoryService::SimpleAD.ShortName``.
        :param size: ``AWS::DirectoryService::SimpleAD.Size``.
        :param vpc_settings: ``AWS::DirectoryService::SimpleAD.VpcSettings``.
        '''
        props = CfnSimpleADProps(
            create_alias=create_alias,
            description=description,
            enable_sso=enable_sso,
            name=name,
            password=password,
            short_name=short_name,
            size=size,
            vpc_settings=vpc_settings,
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
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''
        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

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
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::DirectoryService::SimpleAD.CreateAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "createAlias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::SimpleAD.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::DirectoryService::SimpleAD.EnableSso``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "enableSso", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        jsii.set(self, "password", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::SimpleAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "shortName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Size``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        jsii.set(self, "size", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union["CfnSimpleAD.VpcSettingsProperty", _IResolvable_da3f097b]:
        '''``AWS::DirectoryService::SimpleAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        return typing.cast(typing.Union["CfnSimpleAD.VpcSettingsProperty", _IResolvable_da3f097b], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union["CfnSimpleAD.VpcSettingsProperty", _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "vpcSettings", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_directoryservice.CfnSimpleAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''
            :param subnet_ids: ``CfnSimpleAD.VpcSettingsProperty.SubnetIds``.
            :param vpc_id: ``CfnSimpleAD.VpcSettingsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_directoryservice as directoryservice
                
                vpc_settings_property = directoryservice.CfnSimpleAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''``CfnSimpleAD.VpcSettingsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''``CfnSimpleAD.VpcSettingsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directoryservice.CfnSimpleADProps",
    jsii_struct_bases=[],
    name_mapping={
        "create_alias": "createAlias",
        "description": "description",
        "enable_sso": "enableSso",
        "name": "name",
        "password": "password",
        "short_name": "shortName",
        "size": "size",
        "vpc_settings": "vpcSettings",
    },
)
class CfnSimpleADProps:
    def __init__(
        self,
        *,
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: builtins.str,
        password: builtins.str,
        short_name: typing.Optional[builtins.str] = None,
        size: builtins.str,
        vpc_settings: typing.Union[CfnSimpleAD.VpcSettingsProperty, _IResolvable_da3f097b],
    ) -> None:
        '''Properties for defining a ``AWS::DirectoryService::SimpleAD``.

        :param create_alias: ``AWS::DirectoryService::SimpleAD.CreateAlias``.
        :param description: ``AWS::DirectoryService::SimpleAD.Description``.
        :param enable_sso: ``AWS::DirectoryService::SimpleAD.EnableSso``.
        :param name: ``AWS::DirectoryService::SimpleAD.Name``.
        :param password: ``AWS::DirectoryService::SimpleAD.Password``.
        :param short_name: ``AWS::DirectoryService::SimpleAD.ShortName``.
        :param size: ``AWS::DirectoryService::SimpleAD.Size``.
        :param vpc_settings: ``AWS::DirectoryService::SimpleAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directoryservice as directoryservice
            
            cfn_simple_aDProps = directoryservice.CfnSimpleADProps(
                name="name",
                password="password",
                size="size",
                vpc_settings=directoryservice.CfnSimpleAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                create_alias=False,
                description="description",
                enable_sso=False,
                short_name="shortName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "password": password,
            "size": size,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if description is not None:
            self._values["description"] = description
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::DirectoryService::SimpleAD.CreateAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::SimpleAD.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::DirectoryService::SimpleAD.EnableSso``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DirectoryService::SimpleAD.ShortName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> builtins.str:
        '''``AWS::DirectoryService::SimpleAD.Size``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[CfnSimpleAD.VpcSettingsProperty, _IResolvable_da3f097b]:
        '''``AWS::DirectoryService::SimpleAD.VpcSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[CfnSimpleAD.VpcSettingsProperty, _IResolvable_da3f097b], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimpleADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMicrosoftAD",
    "CfnMicrosoftADProps",
    "CfnSimpleAD",
    "CfnSimpleADProps",
]

publication.publish()
