'''
# AWS::Kendra Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_kendra as kendra
```

> The construct library for this service is in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package named:
>
> ```
> @aws-cdk/aws-kendra-alpha
> ```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Kendra](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Kendra.html).

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
class CfnDataSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource",
):
    '''A CloudFormation ``AWS::Kendra::DataSource``.

    :cloudformationResource: AWS::Kendra::DataSource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kendra as kendra
        
        cfn_data_source = kendra.CfnDataSource(self, "MyCfnDataSource",
            index_id="indexId",
            name="name",
            type="type",
        
            # the properties below are optional
            data_source_configuration=kendra.CfnDataSource.DataSourceConfigurationProperty(
                confluence_configuration=kendra.CfnDataSource.ConfluenceConfigurationProperty(
                    secret_arn="secretArn",
                    server_url="serverUrl",
                    version="version",
        
                    # the properties below are optional
                    attachment_configuration=kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                        attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        crawl_attachments=False
                    ),
                    blog_configuration=kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                        blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    exclusion_patterns=["exclusionPatterns"],
                    inclusion_patterns=["inclusionPatterns"],
                    page_configuration=kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                        page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    space_configuration=kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                        crawl_archived_spaces=False,
                        crawl_personal_spaces=False,
                        exclude_spaces=["excludeSpaces"],
                        include_spaces=["includeSpaces"],
                        space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                ),
                database_configuration=kendra.CfnDataSource.DatabaseConfigurationProperty(
                    column_configuration=kendra.CfnDataSource.ColumnConfigurationProperty(
                        change_detecting_columns=["changeDetectingColumns"],
                        document_data_column_name="documentDataColumnName",
                        document_id_column_name="documentIdColumnName",
        
                        # the properties below are optional
                        document_title_column_name="documentTitleColumnName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    connection_configuration=kendra.CfnDataSource.ConnectionConfigurationProperty(
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        secret_arn="secretArn",
                        table_name="tableName"
                    ),
                    database_engine_type="databaseEngineType",
        
                    # the properties below are optional
                    acl_configuration=kendra.CfnDataSource.AclConfigurationProperty(
                        allowed_groups_column_name="allowedGroupsColumnName"
                    ),
                    sql_configuration=kendra.CfnDataSource.SqlConfigurationProperty(
                        query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                    ),
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                ),
                google_drive_configuration=kendra.CfnDataSource.GoogleDriveConfigurationProperty(
                    secret_arn="secretArn",
        
                    # the properties below are optional
                    exclude_mime_types=["excludeMimeTypes"],
                    exclude_shared_drives=["excludeSharedDrives"],
                    exclude_user_accounts=["excludeUserAccounts"],
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
        
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"]
                ),
                one_drive_configuration=kendra.CfnDataSource.OneDriveConfigurationProperty(
                    one_drive_users=kendra.CfnDataSource.OneDriveUsersProperty(
                        one_drive_user_list=["oneDriveUserList"],
                        one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    secret_arn="secretArn",
                    tenant_domain="tenantDomain",
        
                    # the properties below are optional
                    disable_local_groups=False,
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
        
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"]
                ),
                s3_configuration=kendra.CfnDataSource.S3DataSourceConfigurationProperty(
                    bucket_name="bucketName",
        
                    # the properties below are optional
                    access_control_list_configuration=kendra.CfnDataSource.AccessControlListConfigurationProperty(
                        key_path="keyPath"
                    ),
                    documents_metadata_configuration=kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                        s3_prefix="s3Prefix"
                    ),
                    exclusion_patterns=["exclusionPatterns"],
                    inclusion_patterns=["inclusionPatterns"],
                    inclusion_prefixes=["inclusionPrefixes"]
                ),
                salesforce_configuration=kendra.CfnDataSource.SalesforceConfigurationProperty(
                    secret_arn="secretArn",
                    server_url="serverUrl",
        
                    # the properties below are optional
                    chatter_feed_configuration=kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
        
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        include_filter_types=["includeFilterTypes"]
                    ),
                    crawl_attachments=False,
                    exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                    include_attachment_file_patterns=["includeAttachmentFilePatterns"],
                    knowledge_article_configuration=kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                        included_states=["includedStates"],
        
                        # the properties below are optional
                        custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                            name="name",
        
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
        
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )],
                        standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
        
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
        
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )
                    ),
                    standard_object_attachment_configuration=kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    standard_object_configurations=[kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                        name="name",
        
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    )]
                ),
                service_now_configuration=kendra.CfnDataSource.ServiceNowConfigurationProperty(
                    host_url="hostUrl",
                    secret_arn="secretArn",
                    service_now_build_version="serviceNowBuildVersion",
        
                    # the properties below are optional
                    authentication_type="authenticationType",
                    knowledge_article_configuration=kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
        
                        # the properties below are optional
                        crawl_attachments=False,
                        document_title_field_name="documentTitleFieldName",
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        filter_query="filterQuery",
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                    ),
                    service_catalog_configuration=kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
        
                        # the properties below are optional
                        crawl_attachments=False,
                        document_title_field_name="documentTitleFieldName",
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                    )
                ),
                share_point_configuration=kendra.CfnDataSource.SharePointConfigurationProperty(
                    secret_arn="secretArn",
                    share_point_version="sharePointVersion",
                    urls=["urls"],
        
                    # the properties below are optional
                    crawl_attachments=False,
                    disable_local_groups=False,
                    document_title_field_name="documentTitleFieldName",
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
        
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"],
                    ssl_certificate_s3_path=kendra.CfnDataSource.S3PathProperty(
                        bucket="bucket",
                        key="key"
                    ),
                    use_change_log=False,
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                ),
                web_crawler_configuration=kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                    urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                        seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                            seed_urls=["seedUrls"],
        
                            # the properties below are optional
                            web_crawler_mode="webCrawlerMode"
                        ),
                        site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                            site_maps=["siteMaps"]
                        )
                    ),
        
                    # the properties below are optional
                    authentication_configuration=kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                        basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                            credentials="credentials",
                            host="host",
                            port=123
                        )]
                    ),
                    crawl_depth=123,
                    max_content_size_per_page_in_mega_bytes=123,
                    max_links_per_page=123,
                    max_urls_per_minute_crawl_rate=123,
                    proxy_configuration=kendra.CfnDataSource.ProxyConfigurationProperty(
                        host="host",
                        port=123,
        
                        # the properties below are optional
                        credentials="credentials"
                    ),
                    url_exclusion_patterns=["urlExclusionPatterns"],
                    url_inclusion_patterns=["urlInclusionPatterns"]
                ),
                work_docs_configuration=kendra.CfnDataSource.WorkDocsConfigurationProperty(
                    organization_id="organizationId",
        
                    # the properties below are optional
                    crawl_comments=False,
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
        
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"],
                    use_change_log=False
                )
            ),
            description="description",
            role_arn="roleArn",
            schedule="schedule",
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
        data_source_configuration: typing.Optional[typing.Union["CfnDataSource.DataSourceConfigurationProperty", _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        index_id: builtins.str,
        name: builtins.str,
        role_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        type: builtins.str,
    ) -> None:
        '''Create a new ``AWS::Kendra::DataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_source_configuration: ``AWS::Kendra::DataSource.DataSourceConfiguration``.
        :param description: ``AWS::Kendra::DataSource.Description``.
        :param index_id: ``AWS::Kendra::DataSource.IndexId``.
        :param name: ``AWS::Kendra::DataSource.Name``.
        :param role_arn: ``AWS::Kendra::DataSource.RoleArn``.
        :param schedule: ``AWS::Kendra::DataSource.Schedule``.
        :param tags: ``AWS::Kendra::DataSource.Tags``.
        :param type: ``AWS::Kendra::DataSource.Type``.
        '''
        props = CfnDataSourceProps(
            data_source_configuration=data_source_configuration,
            description=description,
            index_id=index_id,
            name=name,
            role_arn=role_arn,
            schedule=schedule,
            tags=tags,
            type=type,
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
    @jsii.member(jsii_name="dataSourceConfiguration")
    def data_source_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.DataSourceConfigurationProperty", _IResolvable_da3f097b]]:
        '''``AWS::Kendra::DataSource.DataSourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-datasourceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.DataSourceConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "dataSourceConfiguration"))

    @data_source_configuration.setter
    def data_source_configuration(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.DataSourceConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "dataSourceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::DataSource.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="indexId")
    def index_id(self) -> builtins.str:
        '''``AWS::Kendra::DataSource.IndexId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-indexid
        '''
        return typing.cast(builtins.str, jsii.get(self, "indexId"))

    @index_id.setter
    def index_id(self, value: builtins.str) -> None:
        jsii.set(self, "indexId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Kendra::DataSource.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::DataSource.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::DataSource.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-schedule
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "schedule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::Kendra::DataSource.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::Kendra::DataSource.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.AccessControlListConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"key_path": "keyPath"},
    )
    class AccessControlListConfigurationProperty:
        def __init__(self, *, key_path: typing.Optional[builtins.str] = None) -> None:
            '''
            :param key_path: ``CfnDataSource.AccessControlListConfigurationProperty.KeyPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                access_control_list_configuration_property = kendra.CfnDataSource.AccessControlListConfigurationProperty(
                    key_path="keyPath"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key_path is not None:
                self._values["key_path"] = key_path

        @builtins.property
        def key_path(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.AccessControlListConfigurationProperty.KeyPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html#cfn-kendra-datasource-accesscontrollistconfiguration-keypath
            '''
            result = self._values.get("key_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlListConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.AclConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"allowed_groups_column_name": "allowedGroupsColumnName"},
    )
    class AclConfigurationProperty:
        def __init__(self, *, allowed_groups_column_name: builtins.str) -> None:
            '''
            :param allowed_groups_column_name: ``CfnDataSource.AclConfigurationProperty.AllowedGroupsColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                acl_configuration_property = kendra.CfnDataSource.AclConfigurationProperty(
                    allowed_groups_column_name="allowedGroupsColumnName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "allowed_groups_column_name": allowed_groups_column_name,
            }

        @builtins.property
        def allowed_groups_column_name(self) -> builtins.str:
            '''``CfnDataSource.AclConfigurationProperty.AllowedGroupsColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html#cfn-kendra-datasource-aclconfiguration-allowedgroupscolumnname
            '''
            result = self._values.get("allowed_groups_column_name")
            assert result is not None, "Required property 'allowed_groups_column_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AclConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ColumnConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "change_detecting_columns": "changeDetectingColumns",
            "document_data_column_name": "documentDataColumnName",
            "document_id_column_name": "documentIdColumnName",
            "document_title_column_name": "documentTitleColumnName",
            "field_mappings": "fieldMappings",
        },
    )
    class ColumnConfigurationProperty:
        def __init__(
            self,
            *,
            change_detecting_columns: typing.Sequence[builtins.str],
            document_data_column_name: builtins.str,
            document_id_column_name: builtins.str,
            document_title_column_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param change_detecting_columns: ``CfnDataSource.ColumnConfigurationProperty.ChangeDetectingColumns``.
            :param document_data_column_name: ``CfnDataSource.ColumnConfigurationProperty.DocumentDataColumnName``.
            :param document_id_column_name: ``CfnDataSource.ColumnConfigurationProperty.DocumentIdColumnName``.
            :param document_title_column_name: ``CfnDataSource.ColumnConfigurationProperty.DocumentTitleColumnName``.
            :param field_mappings: ``CfnDataSource.ColumnConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                column_configuration_property = kendra.CfnDataSource.ColumnConfigurationProperty(
                    change_detecting_columns=["changeDetectingColumns"],
                    document_data_column_name="documentDataColumnName",
                    document_id_column_name="documentIdColumnName",
                
                    # the properties below are optional
                    document_title_column_name="documentTitleColumnName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "change_detecting_columns": change_detecting_columns,
                "document_data_column_name": document_data_column_name,
                "document_id_column_name": document_id_column_name,
            }
            if document_title_column_name is not None:
                self._values["document_title_column_name"] = document_title_column_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def change_detecting_columns(self) -> typing.List[builtins.str]:
            '''``CfnDataSource.ColumnConfigurationProperty.ChangeDetectingColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-changedetectingcolumns
            '''
            result = self._values.get("change_detecting_columns")
            assert result is not None, "Required property 'change_detecting_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def document_data_column_name(self) -> builtins.str:
            '''``CfnDataSource.ColumnConfigurationProperty.DocumentDataColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documentdatacolumnname
            '''
            result = self._values.get("document_data_column_name")
            assert result is not None, "Required property 'document_data_column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_id_column_name(self) -> builtins.str:
            '''``CfnDataSource.ColumnConfigurationProperty.DocumentIdColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documentidcolumnname
            '''
            result = self._values.get("document_id_column_name")
            assert result is not None, "Required property 'document_id_column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_column_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ColumnConfigurationProperty.DocumentTitleColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documenttitlecolumnname
            '''
            result = self._values.get("document_title_column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.ColumnConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attachment_field_mappings": "attachmentFieldMappings",
            "crawl_attachments": "crawlAttachments",
        },
    )
    class ConfluenceAttachmentConfigurationProperty:
        def __init__(
            self,
            *,
            attachment_field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param attachment_field_mappings: ``CfnDataSource.ConfluenceAttachmentConfigurationProperty.AttachmentFieldMappings``.
            :param crawl_attachments: ``CfnDataSource.ConfluenceAttachmentConfigurationProperty.CrawlAttachments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_attachment_configuration_property = kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                    attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    crawl_attachments=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attachment_field_mappings is not None:
                self._values["attachment_field_mappings"] = attachment_field_mappings
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments

        @builtins.property
        def attachment_field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.ConfluenceAttachmentConfigurationProperty.AttachmentFieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html#cfn-kendra-datasource-confluenceattachmentconfiguration-attachmentfieldmappings
            '''
            result = self._values.get("attachment_field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.ConfluenceAttachmentConfigurationProperty.CrawlAttachments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html#cfn-kendra-datasource-confluenceattachmentconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceAttachmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "date_field_format": "dateFieldFormat",
            "index_field_name": "indexFieldName",
        },
    )
    class ConfluenceAttachmentToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
            index_field_name: builtins.str,
        ) -> None:
            '''
            :param data_source_field_name: ``CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty.DataSourceFieldName``.
            :param date_field_format: ``CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty.DateFieldFormat``.
            :param index_field_name: ``CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_attachment_to_index_field_mapping_property = kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty.DataSourceFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty.DateFieldFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceAttachmentToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluenceBlogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"blog_field_mappings": "blogFieldMappings"},
    )
    class ConfluenceBlogConfigurationProperty:
        def __init__(
            self,
            *,
            blog_field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param blog_field_mappings: ``CfnDataSource.ConfluenceBlogConfigurationProperty.BlogFieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_blog_configuration_property = kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                    blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if blog_field_mappings is not None:
                self._values["blog_field_mappings"] = blog_field_mappings

        @builtins.property
        def blog_field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.ConfluenceBlogConfigurationProperty.BlogFieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html#cfn-kendra-datasource-confluenceblogconfiguration-blogfieldmappings
            '''
            result = self._values.get("blog_field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceBlogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "date_field_format": "dateFieldFormat",
            "index_field_name": "indexFieldName",
        },
    )
    class ConfluenceBlogToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
            index_field_name: builtins.str,
        ) -> None:
            '''
            :param data_source_field_name: ``CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty.DataSourceFieldName``.
            :param date_field_format: ``CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty.DateFieldFormat``.
            :param index_field_name: ``CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_blog_to_index_field_mapping_property = kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty.DataSourceFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty.DateFieldFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceBlogToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluenceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attachment_configuration": "attachmentConfiguration",
            "blog_configuration": "blogConfiguration",
            "exclusion_patterns": "exclusionPatterns",
            "inclusion_patterns": "inclusionPatterns",
            "page_configuration": "pageConfiguration",
            "secret_arn": "secretArn",
            "server_url": "serverUrl",
            "space_configuration": "spaceConfiguration",
            "version": "version",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class ConfluenceConfigurationProperty:
        def __init__(
            self,
            *,
            attachment_configuration: typing.Optional[typing.Union["CfnDataSource.ConfluenceAttachmentConfigurationProperty", _IResolvable_da3f097b]] = None,
            blog_configuration: typing.Optional[typing.Union["CfnDataSource.ConfluenceBlogConfigurationProperty", _IResolvable_da3f097b]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            page_configuration: typing.Optional[typing.Union["CfnDataSource.ConfluencePageConfigurationProperty", _IResolvable_da3f097b]] = None,
            secret_arn: builtins.str,
            server_url: builtins.str,
            space_configuration: typing.Optional[typing.Union["CfnDataSource.ConfluenceSpaceConfigurationProperty", _IResolvable_da3f097b]] = None,
            version: builtins.str,
            vpc_configuration: typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param attachment_configuration: ``CfnDataSource.ConfluenceConfigurationProperty.AttachmentConfiguration``.
            :param blog_configuration: ``CfnDataSource.ConfluenceConfigurationProperty.BlogConfiguration``.
            :param exclusion_patterns: ``CfnDataSource.ConfluenceConfigurationProperty.ExclusionPatterns``.
            :param inclusion_patterns: ``CfnDataSource.ConfluenceConfigurationProperty.InclusionPatterns``.
            :param page_configuration: ``CfnDataSource.ConfluenceConfigurationProperty.PageConfiguration``.
            :param secret_arn: ``CfnDataSource.ConfluenceConfigurationProperty.SecretArn``.
            :param server_url: ``CfnDataSource.ConfluenceConfigurationProperty.ServerUrl``.
            :param space_configuration: ``CfnDataSource.ConfluenceConfigurationProperty.SpaceConfiguration``.
            :param version: ``CfnDataSource.ConfluenceConfigurationProperty.Version``.
            :param vpc_configuration: ``CfnDataSource.ConfluenceConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_configuration_property = kendra.CfnDataSource.ConfluenceConfigurationProperty(
                    secret_arn="secretArn",
                    server_url="serverUrl",
                    version="version",
                
                    # the properties below are optional
                    attachment_configuration=kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                        attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        crawl_attachments=False
                    ),
                    blog_configuration=kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                        blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    exclusion_patterns=["exclusionPatterns"],
                    inclusion_patterns=["inclusionPatterns"],
                    page_configuration=kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                        page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    space_configuration=kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                        crawl_archived_spaces=False,
                        crawl_personal_spaces=False,
                        exclude_spaces=["excludeSpaces"],
                        include_spaces=["includeSpaces"],
                        space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "secret_arn": secret_arn,
                "server_url": server_url,
                "version": version,
            }
            if attachment_configuration is not None:
                self._values["attachment_configuration"] = attachment_configuration
            if blog_configuration is not None:
                self._values["blog_configuration"] = blog_configuration
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns
            if page_configuration is not None:
                self._values["page_configuration"] = page_configuration
            if space_configuration is not None:
                self._values["space_configuration"] = space_configuration
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def attachment_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ConfluenceAttachmentConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.ConfluenceConfigurationProperty.AttachmentConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-attachmentconfiguration
            '''
            result = self._values.get("attachment_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ConfluenceAttachmentConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def blog_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ConfluenceBlogConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.ConfluenceConfigurationProperty.BlogConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-blogconfiguration
            '''
            result = self._values.get("blog_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ConfluenceBlogConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.ConfluenceConfigurationProperty.ExclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.ConfluenceConfigurationProperty.InclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def page_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ConfluencePageConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.ConfluenceConfigurationProperty.PageConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-pageconfiguration
            '''
            result = self._values.get("page_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ConfluencePageConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceConfigurationProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def server_url(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceConfigurationProperty.ServerUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-serverurl
            '''
            result = self._values.get("server_url")
            assert result is not None, "Required property 'server_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def space_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ConfluenceSpaceConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.ConfluenceConfigurationProperty.SpaceConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-spaceconfiguration
            '''
            result = self._values.get("space_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ConfluenceSpaceConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def version(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceConfigurationProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.ConfluenceConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluencePageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"page_field_mappings": "pageFieldMappings"},
    )
    class ConfluencePageConfigurationProperty:
        def __init__(
            self,
            *,
            page_field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.ConfluencePageToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param page_field_mappings: ``CfnDataSource.ConfluencePageConfigurationProperty.PageFieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_page_configuration_property = kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                    page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if page_field_mappings is not None:
                self._values["page_field_mappings"] = page_field_mappings

        @builtins.property
        def page_field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.ConfluencePageToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.ConfluencePageConfigurationProperty.PageFieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html#cfn-kendra-datasource-confluencepageconfiguration-pagefieldmappings
            '''
            result = self._values.get("page_field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.ConfluencePageToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluencePageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "date_field_format": "dateFieldFormat",
            "index_field_name": "indexFieldName",
        },
    )
    class ConfluencePageToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
            index_field_name: builtins.str,
        ) -> None:
            '''
            :param data_source_field_name: ``CfnDataSource.ConfluencePageToIndexFieldMappingProperty.DataSourceFieldName``.
            :param date_field_format: ``CfnDataSource.ConfluencePageToIndexFieldMappingProperty.DateFieldFormat``.
            :param index_field_name: ``CfnDataSource.ConfluencePageToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_page_to_index_field_mapping_property = kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''``CfnDataSource.ConfluencePageToIndexFieldMappingProperty.DataSourceFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ConfluencePageToIndexFieldMappingProperty.DateFieldFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''``CfnDataSource.ConfluencePageToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluencePageToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crawl_archived_spaces": "crawlArchivedSpaces",
            "crawl_personal_spaces": "crawlPersonalSpaces",
            "exclude_spaces": "excludeSpaces",
            "include_spaces": "includeSpaces",
            "space_field_mappings": "spaceFieldMappings",
        },
    )
    class ConfluenceSpaceConfigurationProperty:
        def __init__(
            self,
            *,
            crawl_archived_spaces: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            crawl_personal_spaces: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            exclude_spaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            include_spaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            space_field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param crawl_archived_spaces: ``CfnDataSource.ConfluenceSpaceConfigurationProperty.CrawlArchivedSpaces``.
            :param crawl_personal_spaces: ``CfnDataSource.ConfluenceSpaceConfigurationProperty.CrawlPersonalSpaces``.
            :param exclude_spaces: ``CfnDataSource.ConfluenceSpaceConfigurationProperty.ExcludeSpaces``.
            :param include_spaces: ``CfnDataSource.ConfluenceSpaceConfigurationProperty.IncludeSpaces``.
            :param space_field_mappings: ``CfnDataSource.ConfluenceSpaceConfigurationProperty.SpaceFieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_space_configuration_property = kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                    crawl_archived_spaces=False,
                    crawl_personal_spaces=False,
                    exclude_spaces=["excludeSpaces"],
                    include_spaces=["includeSpaces"],
                    space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if crawl_archived_spaces is not None:
                self._values["crawl_archived_spaces"] = crawl_archived_spaces
            if crawl_personal_spaces is not None:
                self._values["crawl_personal_spaces"] = crawl_personal_spaces
            if exclude_spaces is not None:
                self._values["exclude_spaces"] = exclude_spaces
            if include_spaces is not None:
                self._values["include_spaces"] = include_spaces
            if space_field_mappings is not None:
                self._values["space_field_mappings"] = space_field_mappings

        @builtins.property
        def crawl_archived_spaces(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.ConfluenceSpaceConfigurationProperty.CrawlArchivedSpaces``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-crawlarchivedspaces
            '''
            result = self._values.get("crawl_archived_spaces")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def crawl_personal_spaces(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.ConfluenceSpaceConfigurationProperty.CrawlPersonalSpaces``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-crawlpersonalspaces
            '''
            result = self._values.get("crawl_personal_spaces")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def exclude_spaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.ConfluenceSpaceConfigurationProperty.ExcludeSpaces``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-excludespaces
            '''
            result = self._values.get("exclude_spaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include_spaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.ConfluenceSpaceConfigurationProperty.IncludeSpaces``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-includespaces
            '''
            result = self._values.get("include_spaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def space_field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.ConfluenceSpaceConfigurationProperty.SpaceFieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-spacefieldmappings
            '''
            result = self._values.get("space_field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceSpaceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "date_field_format": "dateFieldFormat",
            "index_field_name": "indexFieldName",
        },
    )
    class ConfluenceSpaceToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
            index_field_name: builtins.str,
        ) -> None:
            '''
            :param data_source_field_name: ``CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty.DataSourceFieldName``.
            :param date_field_format: ``CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty.DateFieldFormat``.
            :param index_field_name: ``CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                confluence_space_to_index_field_mapping_property = kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty.DataSourceFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty.DateFieldFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''``CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceSpaceToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ConnectionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_host": "databaseHost",
            "database_name": "databaseName",
            "database_port": "databasePort",
            "secret_arn": "secretArn",
            "table_name": "tableName",
        },
    )
    class ConnectionConfigurationProperty:
        def __init__(
            self,
            *,
            database_host: builtins.str,
            database_name: builtins.str,
            database_port: jsii.Number,
            secret_arn: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''
            :param database_host: ``CfnDataSource.ConnectionConfigurationProperty.DatabaseHost``.
            :param database_name: ``CfnDataSource.ConnectionConfigurationProperty.DatabaseName``.
            :param database_port: ``CfnDataSource.ConnectionConfigurationProperty.DatabasePort``.
            :param secret_arn: ``CfnDataSource.ConnectionConfigurationProperty.SecretArn``.
            :param table_name: ``CfnDataSource.ConnectionConfigurationProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                connection_configuration_property = kendra.CfnDataSource.ConnectionConfigurationProperty(
                    database_host="databaseHost",
                    database_name="databaseName",
                    database_port=123,
                    secret_arn="secretArn",
                    table_name="tableName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database_host": database_host,
                "database_name": database_name,
                "database_port": database_port,
                "secret_arn": secret_arn,
                "table_name": table_name,
            }

        @builtins.property
        def database_host(self) -> builtins.str:
            '''``CfnDataSource.ConnectionConfigurationProperty.DatabaseHost``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databasehost
            '''
            result = self._values.get("database_host")
            assert result is not None, "Required property 'database_host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnDataSource.ConnectionConfigurationProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_port(self) -> jsii.Number:
            '''``CfnDataSource.ConnectionConfigurationProperty.DatabasePort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databaseport
            '''
            result = self._values.get("database_port")
            assert result is not None, "Required property 'database_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''``CfnDataSource.ConnectionConfigurationProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''``CfnDataSource.ConnectionConfigurationProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.DataSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "confluence_configuration": "confluenceConfiguration",
            "database_configuration": "databaseConfiguration",
            "google_drive_configuration": "googleDriveConfiguration",
            "one_drive_configuration": "oneDriveConfiguration",
            "s3_configuration": "s3Configuration",
            "salesforce_configuration": "salesforceConfiguration",
            "service_now_configuration": "serviceNowConfiguration",
            "share_point_configuration": "sharePointConfiguration",
            "web_crawler_configuration": "webCrawlerConfiguration",
            "work_docs_configuration": "workDocsConfiguration",
        },
    )
    class DataSourceConfigurationProperty:
        def __init__(
            self,
            *,
            confluence_configuration: typing.Optional[typing.Union["CfnDataSource.ConfluenceConfigurationProperty", _IResolvable_da3f097b]] = None,
            database_configuration: typing.Optional[typing.Union["CfnDataSource.DatabaseConfigurationProperty", _IResolvable_da3f097b]] = None,
            google_drive_configuration: typing.Optional[typing.Union["CfnDataSource.GoogleDriveConfigurationProperty", _IResolvable_da3f097b]] = None,
            one_drive_configuration: typing.Optional[typing.Union["CfnDataSource.OneDriveConfigurationProperty", _IResolvable_da3f097b]] = None,
            s3_configuration: typing.Optional[typing.Union["CfnDataSource.S3DataSourceConfigurationProperty", _IResolvable_da3f097b]] = None,
            salesforce_configuration: typing.Optional[typing.Union["CfnDataSource.SalesforceConfigurationProperty", _IResolvable_da3f097b]] = None,
            service_now_configuration: typing.Optional[typing.Union["CfnDataSource.ServiceNowConfigurationProperty", _IResolvable_da3f097b]] = None,
            share_point_configuration: typing.Optional[typing.Union["CfnDataSource.SharePointConfigurationProperty", _IResolvable_da3f097b]] = None,
            web_crawler_configuration: typing.Optional[typing.Union["CfnDataSource.WebCrawlerConfigurationProperty", _IResolvable_da3f097b]] = None,
            work_docs_configuration: typing.Optional[typing.Union["CfnDataSource.WorkDocsConfigurationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param confluence_configuration: ``CfnDataSource.DataSourceConfigurationProperty.ConfluenceConfiguration``.
            :param database_configuration: ``CfnDataSource.DataSourceConfigurationProperty.DatabaseConfiguration``.
            :param google_drive_configuration: ``CfnDataSource.DataSourceConfigurationProperty.GoogleDriveConfiguration``.
            :param one_drive_configuration: ``CfnDataSource.DataSourceConfigurationProperty.OneDriveConfiguration``.
            :param s3_configuration: ``CfnDataSource.DataSourceConfigurationProperty.S3Configuration``.
            :param salesforce_configuration: ``CfnDataSource.DataSourceConfigurationProperty.SalesforceConfiguration``.
            :param service_now_configuration: ``CfnDataSource.DataSourceConfigurationProperty.ServiceNowConfiguration``.
            :param share_point_configuration: ``CfnDataSource.DataSourceConfigurationProperty.SharePointConfiguration``.
            :param web_crawler_configuration: ``CfnDataSource.DataSourceConfigurationProperty.WebCrawlerConfiguration``.
            :param work_docs_configuration: ``CfnDataSource.DataSourceConfigurationProperty.WorkDocsConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                data_source_configuration_property = kendra.CfnDataSource.DataSourceConfigurationProperty(
                    confluence_configuration=kendra.CfnDataSource.ConfluenceConfigurationProperty(
                        secret_arn="secretArn",
                        server_url="serverUrl",
                        version="version",
                
                        # the properties below are optional
                        attachment_configuration=kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                            attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            crawl_attachments=False
                        ),
                        blog_configuration=kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                            blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        exclusion_patterns=["exclusionPatterns"],
                        inclusion_patterns=["inclusionPatterns"],
                        page_configuration=kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                            page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        space_configuration=kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                            crawl_archived_spaces=False,
                            crawl_personal_spaces=False,
                            exclude_spaces=["excludeSpaces"],
                            include_spaces=["includeSpaces"],
                            space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    database_configuration=kendra.CfnDataSource.DatabaseConfigurationProperty(
                        column_configuration=kendra.CfnDataSource.ColumnConfigurationProperty(
                            change_detecting_columns=["changeDetectingColumns"],
                            document_data_column_name="documentDataColumnName",
                            document_id_column_name="documentIdColumnName",
                
                            # the properties below are optional
                            document_title_column_name="documentTitleColumnName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        connection_configuration=kendra.CfnDataSource.ConnectionConfigurationProperty(
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            secret_arn="secretArn",
                            table_name="tableName"
                        ),
                        database_engine_type="databaseEngineType",
                
                        # the properties below are optional
                        acl_configuration=kendra.CfnDataSource.AclConfigurationProperty(
                            allowed_groups_column_name="allowedGroupsColumnName"
                        ),
                        sql_configuration=kendra.CfnDataSource.SqlConfigurationProperty(
                            query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                        ),
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    google_drive_configuration=kendra.CfnDataSource.GoogleDriveConfigurationProperty(
                        secret_arn="secretArn",
                
                        # the properties below are optional
                        exclude_mime_types=["excludeMimeTypes"],
                        exclude_shared_drives=["excludeSharedDrives"],
                        exclude_user_accounts=["excludeUserAccounts"],
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"]
                    ),
                    one_drive_configuration=kendra.CfnDataSource.OneDriveConfigurationProperty(
                        one_drive_users=kendra.CfnDataSource.OneDriveUsersProperty(
                            one_drive_user_list=["oneDriveUserList"],
                            one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        secret_arn="secretArn",
                        tenant_domain="tenantDomain",
                
                        # the properties below are optional
                        disable_local_groups=False,
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"]
                    ),
                    s3_configuration=kendra.CfnDataSource.S3DataSourceConfigurationProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        access_control_list_configuration=kendra.CfnDataSource.AccessControlListConfigurationProperty(
                            key_path="keyPath"
                        ),
                        documents_metadata_configuration=kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                            s3_prefix="s3Prefix"
                        ),
                        exclusion_patterns=["exclusionPatterns"],
                        inclusion_patterns=["inclusionPatterns"],
                        inclusion_prefixes=["inclusionPrefixes"]
                    ),
                    salesforce_configuration=kendra.CfnDataSource.SalesforceConfigurationProperty(
                        secret_arn="secretArn",
                        server_url="serverUrl",
                
                        # the properties below are optional
                        chatter_feed_configuration=kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            include_filter_types=["includeFilterTypes"]
                        ),
                        crawl_attachments=False,
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"],
                        knowledge_article_configuration=kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                            included_states=["includedStates"],
                
                            # the properties below are optional
                            custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                                document_data_field_name="documentDataFieldName",
                                name="name",
                
                                # the properties below are optional
                                document_title_field_name="documentTitleFieldName",
                                field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                    data_source_field_name="dataSourceFieldName",
                                    index_field_name="indexFieldName",
                
                                    # the properties below are optional
                                    date_field_format="dateFieldFormat"
                                )]
                            )],
                            standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                                document_data_field_name="documentDataFieldName",
                
                                # the properties below are optional
                                document_title_field_name="documentTitleFieldName",
                                field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                    data_source_field_name="dataSourceFieldName",
                                    index_field_name="indexFieldName",
                
                                    # the properties below are optional
                                    date_field_format="dateFieldFormat"
                                )]
                            )
                        ),
                        standard_object_attachment_configuration=kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        standard_object_configurations=[kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                            name="name",
                
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )]
                    ),
                    service_now_configuration=kendra.CfnDataSource.ServiceNowConfigurationProperty(
                        host_url="hostUrl",
                        secret_arn="secretArn",
                        service_now_build_version="serviceNowBuildVersion",
                
                        # the properties below are optional
                        authentication_type="authenticationType",
                        knowledge_article_configuration=kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                
                            # the properties below are optional
                            crawl_attachments=False,
                            document_title_field_name="documentTitleFieldName",
                            exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            filter_query="filterQuery",
                            include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                        ),
                        service_catalog_configuration=kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                
                            # the properties below are optional
                            crawl_attachments=False,
                            document_title_field_name="documentTitleFieldName",
                            exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                        )
                    ),
                    share_point_configuration=kendra.CfnDataSource.SharePointConfigurationProperty(
                        secret_arn="secretArn",
                        share_point_version="sharePointVersion",
                        urls=["urls"],
                
                        # the properties below are optional
                        crawl_attachments=False,
                        disable_local_groups=False,
                        document_title_field_name="documentTitleFieldName",
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"],
                        ssl_certificate_s3_path=kendra.CfnDataSource.S3PathProperty(
                            bucket="bucket",
                            key="key"
                        ),
                        use_change_log=False,
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    web_crawler_configuration=kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                        urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                            seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                                seed_urls=["seedUrls"],
                
                                # the properties below are optional
                                web_crawler_mode="webCrawlerMode"
                            ),
                            site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                                site_maps=["siteMaps"]
                            )
                        ),
                
                        # the properties below are optional
                        authentication_configuration=kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                            basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                                credentials="credentials",
                                host="host",
                                port=123
                            )]
                        ),
                        crawl_depth=123,
                        max_content_size_per_page_in_mega_bytes=123,
                        max_links_per_page=123,
                        max_urls_per_minute_crawl_rate=123,
                        proxy_configuration=kendra.CfnDataSource.ProxyConfigurationProperty(
                            host="host",
                            port=123,
                
                            # the properties below are optional
                            credentials="credentials"
                        ),
                        url_exclusion_patterns=["urlExclusionPatterns"],
                        url_inclusion_patterns=["urlInclusionPatterns"]
                    ),
                    work_docs_configuration=kendra.CfnDataSource.WorkDocsConfigurationProperty(
                        organization_id="organizationId",
                
                        # the properties below are optional
                        crawl_comments=False,
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"],
                        use_change_log=False
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if confluence_configuration is not None:
                self._values["confluence_configuration"] = confluence_configuration
            if database_configuration is not None:
                self._values["database_configuration"] = database_configuration
            if google_drive_configuration is not None:
                self._values["google_drive_configuration"] = google_drive_configuration
            if one_drive_configuration is not None:
                self._values["one_drive_configuration"] = one_drive_configuration
            if s3_configuration is not None:
                self._values["s3_configuration"] = s3_configuration
            if salesforce_configuration is not None:
                self._values["salesforce_configuration"] = salesforce_configuration
            if service_now_configuration is not None:
                self._values["service_now_configuration"] = service_now_configuration
            if share_point_configuration is not None:
                self._values["share_point_configuration"] = share_point_configuration
            if web_crawler_configuration is not None:
                self._values["web_crawler_configuration"] = web_crawler_configuration
            if work_docs_configuration is not None:
                self._values["work_docs_configuration"] = work_docs_configuration

        @builtins.property
        def confluence_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ConfluenceConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.ConfluenceConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-confluenceconfiguration
            '''
            result = self._values.get("confluence_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ConfluenceConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def database_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.DatabaseConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.DatabaseConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-databaseconfiguration
            '''
            result = self._values.get("database_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.DatabaseConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def google_drive_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.GoogleDriveConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.GoogleDriveConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-googledriveconfiguration
            '''
            result = self._values.get("google_drive_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.GoogleDriveConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def one_drive_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.OneDriveConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.OneDriveConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-onedriveconfiguration
            '''
            result = self._values.get("one_drive_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.OneDriveConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.S3DataSourceConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.S3Configuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.S3DataSourceConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def salesforce_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.SalesforceConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.SalesforceConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-salesforceconfiguration
            '''
            result = self._values.get("salesforce_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.SalesforceConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def service_now_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ServiceNowConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.ServiceNowConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-servicenowconfiguration
            '''
            result = self._values.get("service_now_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ServiceNowConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def share_point_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.SharePointConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.SharePointConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-sharepointconfiguration
            '''
            result = self._values.get("share_point_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.SharePointConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def web_crawler_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.WebCrawlerConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.WebCrawlerConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-webcrawlerconfiguration
            '''
            result = self._values.get("web_crawler_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.WebCrawlerConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def work_docs_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.WorkDocsConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DataSourceConfigurationProperty.WorkDocsConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-workdocsconfiguration
            '''
            result = self._values.get("work_docs_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.WorkDocsConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "date_field_format": "dateFieldFormat",
            "index_field_name": "indexFieldName",
        },
    )
    class DataSourceToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
            index_field_name: builtins.str,
        ) -> None:
            '''
            :param data_source_field_name: ``CfnDataSource.DataSourceToIndexFieldMappingProperty.DataSourceFieldName``.
            :param date_field_format: ``CfnDataSource.DataSourceToIndexFieldMappingProperty.DateFieldFormat``.
            :param index_field_name: ``CfnDataSource.DataSourceToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                data_source_to_index_field_mapping_property = kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''``CfnDataSource.DataSourceToIndexFieldMappingProperty.DataSourceFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.DataSourceToIndexFieldMappingProperty.DateFieldFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''``CfnDataSource.DataSourceToIndexFieldMappingProperty.IndexFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.DataSourceVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class DataSourceVpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnDataSource.DataSourceVpcConfigurationProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnDataSource.DataSourceVpcConfigurationProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                data_source_vpc_configuration_property = kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnDataSource.DataSourceVpcConfigurationProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html#cfn-kendra-datasource-datasourcevpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''``CfnDataSource.DataSourceVpcConfigurationProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html#cfn-kendra-datasource-datasourcevpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.DatabaseConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acl_configuration": "aclConfiguration",
            "column_configuration": "columnConfiguration",
            "connection_configuration": "connectionConfiguration",
            "database_engine_type": "databaseEngineType",
            "sql_configuration": "sqlConfiguration",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class DatabaseConfigurationProperty:
        def __init__(
            self,
            *,
            acl_configuration: typing.Optional[typing.Union["CfnDataSource.AclConfigurationProperty", _IResolvable_da3f097b]] = None,
            column_configuration: typing.Union["CfnDataSource.ColumnConfigurationProperty", _IResolvable_da3f097b],
            connection_configuration: typing.Union["CfnDataSource.ConnectionConfigurationProperty", _IResolvable_da3f097b],
            database_engine_type: builtins.str,
            sql_configuration: typing.Optional[typing.Union["CfnDataSource.SqlConfigurationProperty", _IResolvable_da3f097b]] = None,
            vpc_configuration: typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param acl_configuration: ``CfnDataSource.DatabaseConfigurationProperty.AclConfiguration``.
            :param column_configuration: ``CfnDataSource.DatabaseConfigurationProperty.ColumnConfiguration``.
            :param connection_configuration: ``CfnDataSource.DatabaseConfigurationProperty.ConnectionConfiguration``.
            :param database_engine_type: ``CfnDataSource.DatabaseConfigurationProperty.DatabaseEngineType``.
            :param sql_configuration: ``CfnDataSource.DatabaseConfigurationProperty.SqlConfiguration``.
            :param vpc_configuration: ``CfnDataSource.DatabaseConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                database_configuration_property = kendra.CfnDataSource.DatabaseConfigurationProperty(
                    column_configuration=kendra.CfnDataSource.ColumnConfigurationProperty(
                        change_detecting_columns=["changeDetectingColumns"],
                        document_data_column_name="documentDataColumnName",
                        document_id_column_name="documentIdColumnName",
                
                        # the properties below are optional
                        document_title_column_name="documentTitleColumnName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    connection_configuration=kendra.CfnDataSource.ConnectionConfigurationProperty(
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        secret_arn="secretArn",
                        table_name="tableName"
                    ),
                    database_engine_type="databaseEngineType",
                
                    # the properties below are optional
                    acl_configuration=kendra.CfnDataSource.AclConfigurationProperty(
                        allowed_groups_column_name="allowedGroupsColumnName"
                    ),
                    sql_configuration=kendra.CfnDataSource.SqlConfigurationProperty(
                        query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                    ),
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "column_configuration": column_configuration,
                "connection_configuration": connection_configuration,
                "database_engine_type": database_engine_type,
            }
            if acl_configuration is not None:
                self._values["acl_configuration"] = acl_configuration
            if sql_configuration is not None:
                self._values["sql_configuration"] = sql_configuration
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def acl_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.AclConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DatabaseConfigurationProperty.AclConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-aclconfiguration
            '''
            result = self._values.get("acl_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.AclConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def column_configuration(
            self,
        ) -> typing.Union["CfnDataSource.ColumnConfigurationProperty", _IResolvable_da3f097b]:
            '''``CfnDataSource.DatabaseConfigurationProperty.ColumnConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-columnconfiguration
            '''
            result = self._values.get("column_configuration")
            assert result is not None, "Required property 'column_configuration' is missing"
            return typing.cast(typing.Union["CfnDataSource.ColumnConfigurationProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def connection_configuration(
            self,
        ) -> typing.Union["CfnDataSource.ConnectionConfigurationProperty", _IResolvable_da3f097b]:
            '''``CfnDataSource.DatabaseConfigurationProperty.ConnectionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-connectionconfiguration
            '''
            result = self._values.get("connection_configuration")
            assert result is not None, "Required property 'connection_configuration' is missing"
            return typing.cast(typing.Union["CfnDataSource.ConnectionConfigurationProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def database_engine_type(self) -> builtins.str:
            '''``CfnDataSource.DatabaseConfigurationProperty.DatabaseEngineType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-databaseenginetype
            '''
            result = self._values.get("database_engine_type")
            assert result is not None, "Required property 'database_engine_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.SqlConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DatabaseConfigurationProperty.SqlConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-sqlconfiguration
            '''
            result = self._values.get("sql_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.SqlConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.DatabaseConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.DocumentsMetadataConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_prefix": "s3Prefix"},
    )
    class DocumentsMetadataConfigurationProperty:
        def __init__(self, *, s3_prefix: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_prefix: ``CfnDataSource.DocumentsMetadataConfigurationProperty.S3Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                documents_metadata_configuration_property = kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                    s3_prefix="s3Prefix"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_prefix is not None:
                self._values["s3_prefix"] = s3_prefix

        @builtins.property
        def s3_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.DocumentsMetadataConfigurationProperty.S3Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html#cfn-kendra-datasource-documentsmetadataconfiguration-s3prefix
            '''
            result = self._values.get("s3_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentsMetadataConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.GoogleDriveConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exclude_mime_types": "excludeMimeTypes",
            "exclude_shared_drives": "excludeSharedDrives",
            "exclude_user_accounts": "excludeUserAccounts",
            "exclusion_patterns": "exclusionPatterns",
            "field_mappings": "fieldMappings",
            "inclusion_patterns": "inclusionPatterns",
            "secret_arn": "secretArn",
        },
    )
    class GoogleDriveConfigurationProperty:
        def __init__(
            self,
            *,
            exclude_mime_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            exclude_shared_drives: typing.Optional[typing.Sequence[builtins.str]] = None,
            exclude_user_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            secret_arn: builtins.str,
        ) -> None:
            '''
            :param exclude_mime_types: ``CfnDataSource.GoogleDriveConfigurationProperty.ExcludeMimeTypes``.
            :param exclude_shared_drives: ``CfnDataSource.GoogleDriveConfigurationProperty.ExcludeSharedDrives``.
            :param exclude_user_accounts: ``CfnDataSource.GoogleDriveConfigurationProperty.ExcludeUserAccounts``.
            :param exclusion_patterns: ``CfnDataSource.GoogleDriveConfigurationProperty.ExclusionPatterns``.
            :param field_mappings: ``CfnDataSource.GoogleDriveConfigurationProperty.FieldMappings``.
            :param inclusion_patterns: ``CfnDataSource.GoogleDriveConfigurationProperty.InclusionPatterns``.
            :param secret_arn: ``CfnDataSource.GoogleDriveConfigurationProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                google_drive_configuration_property = kendra.CfnDataSource.GoogleDriveConfigurationProperty(
                    secret_arn="secretArn",
                
                    # the properties below are optional
                    exclude_mime_types=["excludeMimeTypes"],
                    exclude_shared_drives=["excludeSharedDrives"],
                    exclude_user_accounts=["excludeUserAccounts"],
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "secret_arn": secret_arn,
            }
            if exclude_mime_types is not None:
                self._values["exclude_mime_types"] = exclude_mime_types
            if exclude_shared_drives is not None:
                self._values["exclude_shared_drives"] = exclude_shared_drives
            if exclude_user_accounts is not None:
                self._values["exclude_user_accounts"] = exclude_user_accounts
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns

        @builtins.property
        def exclude_mime_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.GoogleDriveConfigurationProperty.ExcludeMimeTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludemimetypes
            '''
            result = self._values.get("exclude_mime_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def exclude_shared_drives(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.GoogleDriveConfigurationProperty.ExcludeSharedDrives``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludeshareddrives
            '''
            result = self._values.get("exclude_shared_drives")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def exclude_user_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.GoogleDriveConfigurationProperty.ExcludeUserAccounts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludeuseraccounts
            '''
            result = self._values.get("exclude_user_accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.GoogleDriveConfigurationProperty.ExclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.GoogleDriveConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.GoogleDriveConfigurationProperty.InclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''``CfnDataSource.GoogleDriveConfigurationProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GoogleDriveConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.OneDriveConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "disable_local_groups": "disableLocalGroups",
            "exclusion_patterns": "exclusionPatterns",
            "field_mappings": "fieldMappings",
            "inclusion_patterns": "inclusionPatterns",
            "one_drive_users": "oneDriveUsers",
            "secret_arn": "secretArn",
            "tenant_domain": "tenantDomain",
        },
    )
    class OneDriveConfigurationProperty:
        def __init__(
            self,
            *,
            disable_local_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            one_drive_users: typing.Union["CfnDataSource.OneDriveUsersProperty", _IResolvable_da3f097b],
            secret_arn: builtins.str,
            tenant_domain: builtins.str,
        ) -> None:
            '''
            :param disable_local_groups: ``CfnDataSource.OneDriveConfigurationProperty.DisableLocalGroups``.
            :param exclusion_patterns: ``CfnDataSource.OneDriveConfigurationProperty.ExclusionPatterns``.
            :param field_mappings: ``CfnDataSource.OneDriveConfigurationProperty.FieldMappings``.
            :param inclusion_patterns: ``CfnDataSource.OneDriveConfigurationProperty.InclusionPatterns``.
            :param one_drive_users: ``CfnDataSource.OneDriveConfigurationProperty.OneDriveUsers``.
            :param secret_arn: ``CfnDataSource.OneDriveConfigurationProperty.SecretArn``.
            :param tenant_domain: ``CfnDataSource.OneDriveConfigurationProperty.TenantDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                one_drive_configuration_property = kendra.CfnDataSource.OneDriveConfigurationProperty(
                    one_drive_users=kendra.CfnDataSource.OneDriveUsersProperty(
                        one_drive_user_list=["oneDriveUserList"],
                        one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    secret_arn="secretArn",
                    tenant_domain="tenantDomain",
                
                    # the properties below are optional
                    disable_local_groups=False,
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "one_drive_users": one_drive_users,
                "secret_arn": secret_arn,
                "tenant_domain": tenant_domain,
            }
            if disable_local_groups is not None:
                self._values["disable_local_groups"] = disable_local_groups
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns

        @builtins.property
        def disable_local_groups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.OneDriveConfigurationProperty.DisableLocalGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-disablelocalgroups
            '''
            result = self._values.get("disable_local_groups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.OneDriveConfigurationProperty.ExclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.OneDriveConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.OneDriveConfigurationProperty.InclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def one_drive_users(
            self,
        ) -> typing.Union["CfnDataSource.OneDriveUsersProperty", _IResolvable_da3f097b]:
            '''``CfnDataSource.OneDriveConfigurationProperty.OneDriveUsers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-onedriveusers
            '''
            result = self._values.get("one_drive_users")
            assert result is not None, "Required property 'one_drive_users' is missing"
            return typing.cast(typing.Union["CfnDataSource.OneDriveUsersProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''``CfnDataSource.OneDriveConfigurationProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tenant_domain(self) -> builtins.str:
            '''``CfnDataSource.OneDriveConfigurationProperty.TenantDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-tenantdomain
            '''
            result = self._values.get("tenant_domain")
            assert result is not None, "Required property 'tenant_domain' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OneDriveConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.OneDriveUsersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "one_drive_user_list": "oneDriveUserList",
            "one_drive_user_s3_path": "oneDriveUserS3Path",
        },
    )
    class OneDriveUsersProperty:
        def __init__(
            self,
            *,
            one_drive_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            one_drive_user_s3_path: typing.Optional[typing.Union["CfnDataSource.S3PathProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param one_drive_user_list: ``CfnDataSource.OneDriveUsersProperty.OneDriveUserList``.
            :param one_drive_user_s3_path: ``CfnDataSource.OneDriveUsersProperty.OneDriveUserS3Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                one_drive_users_property = kendra.CfnDataSource.OneDriveUsersProperty(
                    one_drive_user_list=["oneDriveUserList"],
                    one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                        bucket="bucket",
                        key="key"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if one_drive_user_list is not None:
                self._values["one_drive_user_list"] = one_drive_user_list
            if one_drive_user_s3_path is not None:
                self._values["one_drive_user_s3_path"] = one_drive_user_s3_path

        @builtins.property
        def one_drive_user_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.OneDriveUsersProperty.OneDriveUserList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html#cfn-kendra-datasource-onedriveusers-onedriveuserlist
            '''
            result = self._values.get("one_drive_user_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def one_drive_user_s3_path(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.S3PathProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.OneDriveUsersProperty.OneDriveUserS3Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html#cfn-kendra-datasource-onedriveusers-onedriveusers3path
            '''
            result = self._values.get("one_drive_user_s3_path")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.S3PathProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OneDriveUsersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ProxyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"credentials": "credentials", "host": "host", "port": "port"},
    )
    class ProxyConfigurationProperty:
        def __init__(
            self,
            *,
            credentials: typing.Optional[builtins.str] = None,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param credentials: ``CfnDataSource.ProxyConfigurationProperty.Credentials``.
            :param host: ``CfnDataSource.ProxyConfigurationProperty.Host``.
            :param port: ``CfnDataSource.ProxyConfigurationProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                proxy_configuration_property = kendra.CfnDataSource.ProxyConfigurationProperty(
                    host="host",
                    port=123,
                
                    # the properties below are optional
                    credentials="credentials"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "host": host,
                "port": port,
            }
            if credentials is not None:
                self._values["credentials"] = credentials

        @builtins.property
        def credentials(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ProxyConfigurationProperty.Credentials``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-credentials
            '''
            result = self._values.get("credentials")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.ProxyConfigurationProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.ProxyConfigurationProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProxyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.S3DataSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_control_list_configuration": "accessControlListConfiguration",
            "bucket_name": "bucketName",
            "documents_metadata_configuration": "documentsMetadataConfiguration",
            "exclusion_patterns": "exclusionPatterns",
            "inclusion_patterns": "inclusionPatterns",
            "inclusion_prefixes": "inclusionPrefixes",
        },
    )
    class S3DataSourceConfigurationProperty:
        def __init__(
            self,
            *,
            access_control_list_configuration: typing.Optional[typing.Union["CfnDataSource.AccessControlListConfigurationProperty", _IResolvable_da3f097b]] = None,
            bucket_name: builtins.str,
            documents_metadata_configuration: typing.Optional[typing.Union["CfnDataSource.DocumentsMetadataConfigurationProperty", _IResolvable_da3f097b]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param access_control_list_configuration: ``CfnDataSource.S3DataSourceConfigurationProperty.AccessControlListConfiguration``.
            :param bucket_name: ``CfnDataSource.S3DataSourceConfigurationProperty.BucketName``.
            :param documents_metadata_configuration: ``CfnDataSource.S3DataSourceConfigurationProperty.DocumentsMetadataConfiguration``.
            :param exclusion_patterns: ``CfnDataSource.S3DataSourceConfigurationProperty.ExclusionPatterns``.
            :param inclusion_patterns: ``CfnDataSource.S3DataSourceConfigurationProperty.InclusionPatterns``.
            :param inclusion_prefixes: ``CfnDataSource.S3DataSourceConfigurationProperty.InclusionPrefixes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                s3_data_source_configuration_property = kendra.CfnDataSource.S3DataSourceConfigurationProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    access_control_list_configuration=kendra.CfnDataSource.AccessControlListConfigurationProperty(
                        key_path="keyPath"
                    ),
                    documents_metadata_configuration=kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                        s3_prefix="s3Prefix"
                    ),
                    exclusion_patterns=["exclusionPatterns"],
                    inclusion_patterns=["inclusionPatterns"],
                    inclusion_prefixes=["inclusionPrefixes"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if access_control_list_configuration is not None:
                self._values["access_control_list_configuration"] = access_control_list_configuration
            if documents_metadata_configuration is not None:
                self._values["documents_metadata_configuration"] = documents_metadata_configuration
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns
            if inclusion_prefixes is not None:
                self._values["inclusion_prefixes"] = inclusion_prefixes

        @builtins.property
        def access_control_list_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.AccessControlListConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.S3DataSourceConfigurationProperty.AccessControlListConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-accesscontrollistconfiguration
            '''
            result = self._values.get("access_control_list_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.AccessControlListConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''``CfnDataSource.S3DataSourceConfigurationProperty.BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def documents_metadata_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.DocumentsMetadataConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.S3DataSourceConfigurationProperty.DocumentsMetadataConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-documentsmetadataconfiguration
            '''
            result = self._values.get("documents_metadata_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.DocumentsMetadataConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.S3DataSourceConfigurationProperty.ExclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.S3DataSourceConfigurationProperty.InclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def inclusion_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.S3DataSourceConfigurationProperty.InclusionPrefixes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-inclusionprefixes
            '''
            result = self._values.get("inclusion_prefixes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DataSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.S3PathProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3PathProperty:
        def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
            '''
            :param bucket: ``CfnDataSource.S3PathProperty.Bucket``.
            :param key: ``CfnDataSource.S3PathProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                s3_path_property = kendra.CfnDataSource.S3PathProperty(
                    bucket="bucket",
                    key="key"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''``CfnDataSource.S3PathProperty.Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html#cfn-kendra-datasource-s3path-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnDataSource.S3PathProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html#cfn-kendra-datasource-s3path-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3PathProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
            "include_filter_types": "includeFilterTypes",
        },
    )
    class SalesforceChatterFeedConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            include_filter_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param document_data_field_name: ``CfnDataSource.SalesforceChatterFeedConfigurationProperty.DocumentDataFieldName``.
            :param document_title_field_name: ``CfnDataSource.SalesforceChatterFeedConfigurationProperty.DocumentTitleFieldName``.
            :param field_mappings: ``CfnDataSource.SalesforceChatterFeedConfigurationProperty.FieldMappings``.
            :param include_filter_types: ``CfnDataSource.SalesforceChatterFeedConfigurationProperty.IncludeFilterTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                salesforce_chatter_feed_configuration_property = kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                
                    # the properties below are optional
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    include_filter_types=["includeFilterTypes"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
            }
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if include_filter_types is not None:
                self._values["include_filter_types"] = include_filter_types

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''``CfnDataSource.SalesforceChatterFeedConfigurationProperty.DocumentDataFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.SalesforceChatterFeedConfigurationProperty.DocumentTitleFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.SalesforceChatterFeedConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def include_filter_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.SalesforceChatterFeedConfigurationProperty.IncludeFilterTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-includefiltertypes
            '''
            result = self._values.get("include_filter_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceChatterFeedConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SalesforceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "chatter_feed_configuration": "chatterFeedConfiguration",
            "crawl_attachments": "crawlAttachments",
            "exclude_attachment_file_patterns": "excludeAttachmentFilePatterns",
            "include_attachment_file_patterns": "includeAttachmentFilePatterns",
            "knowledge_article_configuration": "knowledgeArticleConfiguration",
            "secret_arn": "secretArn",
            "server_url": "serverUrl",
            "standard_object_attachment_configuration": "standardObjectAttachmentConfiguration",
            "standard_object_configurations": "standardObjectConfigurations",
        },
    )
    class SalesforceConfigurationProperty:
        def __init__(
            self,
            *,
            chatter_feed_configuration: typing.Optional[typing.Union["CfnDataSource.SalesforceChatterFeedConfigurationProperty", _IResolvable_da3f097b]] = None,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            knowledge_article_configuration: typing.Optional[typing.Union["CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty", _IResolvable_da3f097b]] = None,
            secret_arn: builtins.str,
            server_url: builtins.str,
            standard_object_attachment_configuration: typing.Optional[typing.Union["CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty", _IResolvable_da3f097b]] = None,
            standard_object_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.SalesforceStandardObjectConfigurationProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param chatter_feed_configuration: ``CfnDataSource.SalesforceConfigurationProperty.ChatterFeedConfiguration``.
            :param crawl_attachments: ``CfnDataSource.SalesforceConfigurationProperty.CrawlAttachments``.
            :param exclude_attachment_file_patterns: ``CfnDataSource.SalesforceConfigurationProperty.ExcludeAttachmentFilePatterns``.
            :param include_attachment_file_patterns: ``CfnDataSource.SalesforceConfigurationProperty.IncludeAttachmentFilePatterns``.
            :param knowledge_article_configuration: ``CfnDataSource.SalesforceConfigurationProperty.KnowledgeArticleConfiguration``.
            :param secret_arn: ``CfnDataSource.SalesforceConfigurationProperty.SecretArn``.
            :param server_url: ``CfnDataSource.SalesforceConfigurationProperty.ServerUrl``.
            :param standard_object_attachment_configuration: ``CfnDataSource.SalesforceConfigurationProperty.StandardObjectAttachmentConfiguration``.
            :param standard_object_configurations: ``CfnDataSource.SalesforceConfigurationProperty.StandardObjectConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                salesforce_configuration_property = kendra.CfnDataSource.SalesforceConfigurationProperty(
                    secret_arn="secretArn",
                    server_url="serverUrl",
                
                    # the properties below are optional
                    chatter_feed_configuration=kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        include_filter_types=["includeFilterTypes"]
                    ),
                    crawl_attachments=False,
                    exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                    include_attachment_file_patterns=["includeAttachmentFilePatterns"],
                    knowledge_article_configuration=kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                        included_states=["includedStates"],
                
                        # the properties below are optional
                        custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                            name="name",
                
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )],
                        standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )
                    ),
                    standard_object_attachment_configuration=kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    standard_object_configurations=[kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                        name="name",
                
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "secret_arn": secret_arn,
                "server_url": server_url,
            }
            if chatter_feed_configuration is not None:
                self._values["chatter_feed_configuration"] = chatter_feed_configuration
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments
            if exclude_attachment_file_patterns is not None:
                self._values["exclude_attachment_file_patterns"] = exclude_attachment_file_patterns
            if include_attachment_file_patterns is not None:
                self._values["include_attachment_file_patterns"] = include_attachment_file_patterns
            if knowledge_article_configuration is not None:
                self._values["knowledge_article_configuration"] = knowledge_article_configuration
            if standard_object_attachment_configuration is not None:
                self._values["standard_object_attachment_configuration"] = standard_object_attachment_configuration
            if standard_object_configurations is not None:
                self._values["standard_object_configurations"] = standard_object_configurations

        @builtins.property
        def chatter_feed_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.SalesforceChatterFeedConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.SalesforceConfigurationProperty.ChatterFeedConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-chatterfeedconfiguration
            '''
            result = self._values.get("chatter_feed_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.SalesforceChatterFeedConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.SalesforceConfigurationProperty.CrawlAttachments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def exclude_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.SalesforceConfigurationProperty.ExcludeAttachmentFilePatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-excludeattachmentfilepatterns
            '''
            result = self._values.get("exclude_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.SalesforceConfigurationProperty.IncludeAttachmentFilePatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-includeattachmentfilepatterns
            '''
            result = self._values.get("include_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def knowledge_article_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.SalesforceConfigurationProperty.KnowledgeArticleConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-knowledgearticleconfiguration
            '''
            result = self._values.get("knowledge_article_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''``CfnDataSource.SalesforceConfigurationProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def server_url(self) -> builtins.str:
            '''``CfnDataSource.SalesforceConfigurationProperty.ServerUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-serverurl
            '''
            result = self._values.get("server_url")
            assert result is not None, "Required property 'server_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def standard_object_attachment_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.SalesforceConfigurationProperty.StandardObjectAttachmentConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-standardobjectattachmentconfiguration
            '''
            result = self._values.get("standard_object_attachment_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def standard_object_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.SalesforceStandardObjectConfigurationProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.SalesforceConfigurationProperty.StandardObjectConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-standardobjectconfigurations
            '''
            result = self._values.get("standard_object_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.SalesforceStandardObjectConfigurationProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
            "name": "name",
        },
    )
    class SalesforceCustomKnowledgeArticleTypeConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            name: builtins.str,
        ) -> None:
            '''
            :param document_data_field_name: ``CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty.DocumentDataFieldName``.
            :param document_title_field_name: ``CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty.DocumentTitleFieldName``.
            :param field_mappings: ``CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty.FieldMappings``.
            :param name: ``CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                salesforce_custom_knowledge_article_type_configuration_property = kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                    name="name",
                
                    # the properties below are optional
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
                "name": name,
            }
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''``CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty.DocumentDataFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty.DocumentTitleFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceCustomKnowledgeArticleTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_knowledge_article_type_configurations": "customKnowledgeArticleTypeConfigurations",
            "included_states": "includedStates",
            "standard_knowledge_article_type_configuration": "standardKnowledgeArticleTypeConfiguration",
        },
    )
    class SalesforceKnowledgeArticleConfigurationProperty:
        def __init__(
            self,
            *,
            custom_knowledge_article_type_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty", _IResolvable_da3f097b]]]] = None,
            included_states: typing.Sequence[builtins.str],
            standard_knowledge_article_type_configuration: typing.Optional[typing.Union["CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param custom_knowledge_article_type_configurations: ``CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty.CustomKnowledgeArticleTypeConfigurations``.
            :param included_states: ``CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty.IncludedStates``.
            :param standard_knowledge_article_type_configuration: ``CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty.StandardKnowledgeArticleTypeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                salesforce_knowledge_article_configuration_property = kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                    included_states=["includedStates"],
                
                    # the properties below are optional
                    custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                        name="name",
                
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    )],
                    standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "included_states": included_states,
            }
            if custom_knowledge_article_type_configurations is not None:
                self._values["custom_knowledge_article_type_configurations"] = custom_knowledge_article_type_configurations
            if standard_knowledge_article_type_configuration is not None:
                self._values["standard_knowledge_article_type_configuration"] = standard_knowledge_article_type_configuration

        @builtins.property
        def custom_knowledge_article_type_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty.CustomKnowledgeArticleTypeConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-customknowledgearticletypeconfigurations
            '''
            result = self._values.get("custom_knowledge_article_type_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def included_states(self) -> typing.List[builtins.str]:
            '''``CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty.IncludedStates``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-includedstates
            '''
            result = self._values.get("included_states")
            assert result is not None, "Required property 'included_states' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def standard_knowledge_article_type_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty.StandardKnowledgeArticleTypeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-standardknowledgearticletypeconfiguration
            '''
            result = self._values.get("standard_knowledge_article_type_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceKnowledgeArticleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
        },
    )
    class SalesforceStandardKnowledgeArticleTypeConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param document_data_field_name: ``CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty.DocumentDataFieldName``.
            :param document_title_field_name: ``CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty.DocumentTitleFieldName``.
            :param field_mappings: ``CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                salesforce_standard_knowledge_article_type_configuration_property = kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                
                    # the properties below are optional
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
            }
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''``CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty.DocumentDataFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty.DocumentTitleFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceStandardKnowledgeArticleTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
        },
    )
    class SalesforceStandardObjectAttachmentConfigurationProperty:
        def __init__(
            self,
            *,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param document_title_field_name: ``CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty.DocumentTitleFieldName``.
            :param field_mappings: ``CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                salesforce_standard_object_attachment_configuration_property = kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty.DocumentTitleFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceStandardObjectAttachmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
            "name": "name",
        },
    )
    class SalesforceStandardObjectConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            name: builtins.str,
        ) -> None:
            '''
            :param document_data_field_name: ``CfnDataSource.SalesforceStandardObjectConfigurationProperty.DocumentDataFieldName``.
            :param document_title_field_name: ``CfnDataSource.SalesforceStandardObjectConfigurationProperty.DocumentTitleFieldName``.
            :param field_mappings: ``CfnDataSource.SalesforceStandardObjectConfigurationProperty.FieldMappings``.
            :param name: ``CfnDataSource.SalesforceStandardObjectConfigurationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                salesforce_standard_object_configuration_property = kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                    name="name",
                
                    # the properties below are optional
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
                "name": name,
            }
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''``CfnDataSource.SalesforceStandardObjectConfigurationProperty.DocumentDataFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.SalesforceStandardObjectConfigurationProperty.DocumentTitleFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.SalesforceStandardObjectConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDataSource.SalesforceStandardObjectConfigurationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceStandardObjectConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ServiceNowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_type": "authenticationType",
            "host_url": "hostUrl",
            "knowledge_article_configuration": "knowledgeArticleConfiguration",
            "secret_arn": "secretArn",
            "service_catalog_configuration": "serviceCatalogConfiguration",
            "service_now_build_version": "serviceNowBuildVersion",
        },
    )
    class ServiceNowConfigurationProperty:
        def __init__(
            self,
            *,
            authentication_type: typing.Optional[builtins.str] = None,
            host_url: builtins.str,
            knowledge_article_configuration: typing.Optional[typing.Union["CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty", _IResolvable_da3f097b]] = None,
            secret_arn: builtins.str,
            service_catalog_configuration: typing.Optional[typing.Union["CfnDataSource.ServiceNowServiceCatalogConfigurationProperty", _IResolvable_da3f097b]] = None,
            service_now_build_version: builtins.str,
        ) -> None:
            '''
            :param authentication_type: ``CfnDataSource.ServiceNowConfigurationProperty.AuthenticationType``.
            :param host_url: ``CfnDataSource.ServiceNowConfigurationProperty.HostUrl``.
            :param knowledge_article_configuration: ``CfnDataSource.ServiceNowConfigurationProperty.KnowledgeArticleConfiguration``.
            :param secret_arn: ``CfnDataSource.ServiceNowConfigurationProperty.SecretArn``.
            :param service_catalog_configuration: ``CfnDataSource.ServiceNowConfigurationProperty.ServiceCatalogConfiguration``.
            :param service_now_build_version: ``CfnDataSource.ServiceNowConfigurationProperty.ServiceNowBuildVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                service_now_configuration_property = kendra.CfnDataSource.ServiceNowConfigurationProperty(
                    host_url="hostUrl",
                    secret_arn="secretArn",
                    service_now_build_version="serviceNowBuildVersion",
                
                    # the properties below are optional
                    authentication_type="authenticationType",
                    knowledge_article_configuration=kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                
                        # the properties below are optional
                        crawl_attachments=False,
                        document_title_field_name="documentTitleFieldName",
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        filter_query="filterQuery",
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                    ),
                    service_catalog_configuration=kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                
                        # the properties below are optional
                        crawl_attachments=False,
                        document_title_field_name="documentTitleFieldName",
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "host_url": host_url,
                "secret_arn": secret_arn,
                "service_now_build_version": service_now_build_version,
            }
            if authentication_type is not None:
                self._values["authentication_type"] = authentication_type
            if knowledge_article_configuration is not None:
                self._values["knowledge_article_configuration"] = knowledge_article_configuration
            if service_catalog_configuration is not None:
                self._values["service_catalog_configuration"] = service_catalog_configuration

        @builtins.property
        def authentication_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ServiceNowConfigurationProperty.AuthenticationType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-authenticationtype
            '''
            result = self._values.get("authentication_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def host_url(self) -> builtins.str:
            '''``CfnDataSource.ServiceNowConfigurationProperty.HostUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-hosturl
            '''
            result = self._values.get("host_url")
            assert result is not None, "Required property 'host_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def knowledge_article_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.ServiceNowConfigurationProperty.KnowledgeArticleConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-knowledgearticleconfiguration
            '''
            result = self._values.get("knowledge_article_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''``CfnDataSource.ServiceNowConfigurationProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_catalog_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ServiceNowServiceCatalogConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.ServiceNowConfigurationProperty.ServiceCatalogConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-servicecatalogconfiguration
            '''
            result = self._values.get("service_catalog_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ServiceNowServiceCatalogConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def service_now_build_version(self) -> builtins.str:
            '''``CfnDataSource.ServiceNowConfigurationProperty.ServiceNowBuildVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-servicenowbuildversion
            '''
            result = self._values.get("service_now_build_version")
            assert result is not None, "Required property 'service_now_build_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crawl_attachments": "crawlAttachments",
            "document_data_field_name": "documentDataFieldName",
            "document_title_field_name": "documentTitleFieldName",
            "exclude_attachment_file_patterns": "excludeAttachmentFilePatterns",
            "field_mappings": "fieldMappings",
            "filter_query": "filterQuery",
            "include_attachment_file_patterns": "includeAttachmentFilePatterns",
        },
    )
    class ServiceNowKnowledgeArticleConfigurationProperty:
        def __init__(
            self,
            *,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            document_data_field_name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            filter_query: typing.Optional[builtins.str] = None,
            include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param crawl_attachments: ``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.CrawlAttachments``.
            :param document_data_field_name: ``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.DocumentDataFieldName``.
            :param document_title_field_name: ``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.DocumentTitleFieldName``.
            :param exclude_attachment_file_patterns: ``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.ExcludeAttachmentFilePatterns``.
            :param field_mappings: ``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.FieldMappings``.
            :param filter_query: ``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.FilterQuery``.
            :param include_attachment_file_patterns: ``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.IncludeAttachmentFilePatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                service_now_knowledge_article_configuration_property = kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                
                    # the properties below are optional
                    crawl_attachments=False,
                    document_title_field_name="documentTitleFieldName",
                    exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    filter_query="filterQuery",
                    include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
            }
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if exclude_attachment_file_patterns is not None:
                self._values["exclude_attachment_file_patterns"] = exclude_attachment_file_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if filter_query is not None:
                self._values["filter_query"] = filter_query
            if include_attachment_file_patterns is not None:
                self._values["include_attachment_file_patterns"] = include_attachment_file_patterns

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.CrawlAttachments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.DocumentDataFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.DocumentTitleFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclude_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.ExcludeAttachmentFilePatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-excludeattachmentfilepatterns
            '''
            result = self._values.get("exclude_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def filter_query(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.FilterQuery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-filterquery
            '''
            result = self._values.get("filter_query")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def include_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty.IncludeAttachmentFilePatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-includeattachmentfilepatterns
            '''
            result = self._values.get("include_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowKnowledgeArticleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crawl_attachments": "crawlAttachments",
            "document_data_field_name": "documentDataFieldName",
            "document_title_field_name": "documentTitleFieldName",
            "exclude_attachment_file_patterns": "excludeAttachmentFilePatterns",
            "field_mappings": "fieldMappings",
            "include_attachment_file_patterns": "includeAttachmentFilePatterns",
        },
    )
    class ServiceNowServiceCatalogConfigurationProperty:
        def __init__(
            self,
            *,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            document_data_field_name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param crawl_attachments: ``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.CrawlAttachments``.
            :param document_data_field_name: ``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.DocumentDataFieldName``.
            :param document_title_field_name: ``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.DocumentTitleFieldName``.
            :param exclude_attachment_file_patterns: ``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.ExcludeAttachmentFilePatterns``.
            :param field_mappings: ``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.FieldMappings``.
            :param include_attachment_file_patterns: ``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.IncludeAttachmentFilePatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                service_now_service_catalog_configuration_property = kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                
                    # the properties below are optional
                    crawl_attachments=False,
                    document_title_field_name="documentTitleFieldName",
                    exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
            }
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if exclude_attachment_file_patterns is not None:
                self._values["exclude_attachment_file_patterns"] = exclude_attachment_file_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if include_attachment_file_patterns is not None:
                self._values["include_attachment_file_patterns"] = include_attachment_file_patterns

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.CrawlAttachments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.DocumentDataFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.DocumentTitleFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclude_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.ExcludeAttachmentFilePatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-excludeattachmentfilepatterns
            '''
            result = self._values.get("exclude_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def include_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.ServiceNowServiceCatalogConfigurationProperty.IncludeAttachmentFilePatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-includeattachmentfilepatterns
            '''
            result = self._values.get("include_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowServiceCatalogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SharePointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crawl_attachments": "crawlAttachments",
            "disable_local_groups": "disableLocalGroups",
            "document_title_field_name": "documentTitleFieldName",
            "exclusion_patterns": "exclusionPatterns",
            "field_mappings": "fieldMappings",
            "inclusion_patterns": "inclusionPatterns",
            "secret_arn": "secretArn",
            "share_point_version": "sharePointVersion",
            "ssl_certificate_s3_path": "sslCertificateS3Path",
            "urls": "urls",
            "use_change_log": "useChangeLog",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class SharePointConfigurationProperty:
        def __init__(
            self,
            *,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            disable_local_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            document_title_field_name: typing.Optional[builtins.str] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            secret_arn: builtins.str,
            share_point_version: builtins.str,
            ssl_certificate_s3_path: typing.Optional[typing.Union["CfnDataSource.S3PathProperty", _IResolvable_da3f097b]] = None,
            urls: typing.Sequence[builtins.str],
            use_change_log: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            vpc_configuration: typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param crawl_attachments: ``CfnDataSource.SharePointConfigurationProperty.CrawlAttachments``.
            :param disable_local_groups: ``CfnDataSource.SharePointConfigurationProperty.DisableLocalGroups``.
            :param document_title_field_name: ``CfnDataSource.SharePointConfigurationProperty.DocumentTitleFieldName``.
            :param exclusion_patterns: ``CfnDataSource.SharePointConfigurationProperty.ExclusionPatterns``.
            :param field_mappings: ``CfnDataSource.SharePointConfigurationProperty.FieldMappings``.
            :param inclusion_patterns: ``CfnDataSource.SharePointConfigurationProperty.InclusionPatterns``.
            :param secret_arn: ``CfnDataSource.SharePointConfigurationProperty.SecretArn``.
            :param share_point_version: ``CfnDataSource.SharePointConfigurationProperty.SharePointVersion``.
            :param ssl_certificate_s3_path: ``CfnDataSource.SharePointConfigurationProperty.SslCertificateS3Path``.
            :param urls: ``CfnDataSource.SharePointConfigurationProperty.Urls``.
            :param use_change_log: ``CfnDataSource.SharePointConfigurationProperty.UseChangeLog``.
            :param vpc_configuration: ``CfnDataSource.SharePointConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                share_point_configuration_property = kendra.CfnDataSource.SharePointConfigurationProperty(
                    secret_arn="secretArn",
                    share_point_version="sharePointVersion",
                    urls=["urls"],
                
                    # the properties below are optional
                    crawl_attachments=False,
                    disable_local_groups=False,
                    document_title_field_name="documentTitleFieldName",
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"],
                    ssl_certificate_s3_path=kendra.CfnDataSource.S3PathProperty(
                        bucket="bucket",
                        key="key"
                    ),
                    use_change_log=False,
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "secret_arn": secret_arn,
                "share_point_version": share_point_version,
                "urls": urls,
            }
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments
            if disable_local_groups is not None:
                self._values["disable_local_groups"] = disable_local_groups
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns
            if ssl_certificate_s3_path is not None:
                self._values["ssl_certificate_s3_path"] = ssl_certificate_s3_path
            if use_change_log is not None:
                self._values["use_change_log"] = use_change_log
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.SharePointConfigurationProperty.CrawlAttachments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def disable_local_groups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.SharePointConfigurationProperty.DisableLocalGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-disablelocalgroups
            '''
            result = self._values.get("disable_local_groups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.SharePointConfigurationProperty.DocumentTitleFieldName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.SharePointConfigurationProperty.ExclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.SharePointConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.SharePointConfigurationProperty.InclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''``CfnDataSource.SharePointConfigurationProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def share_point_version(self) -> builtins.str:
            '''``CfnDataSource.SharePointConfigurationProperty.SharePointVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-sharepointversion
            '''
            result = self._values.get("share_point_version")
            assert result is not None, "Required property 'share_point_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ssl_certificate_s3_path(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.S3PathProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.SharePointConfigurationProperty.SslCertificateS3Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-sslcertificates3path
            '''
            result = self._values.get("ssl_certificate_s3_path")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.S3PathProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def urls(self) -> typing.List[builtins.str]:
            '''``CfnDataSource.SharePointConfigurationProperty.Urls``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-urls
            '''
            result = self._values.get("urls")
            assert result is not None, "Required property 'urls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def use_change_log(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.SharePointConfigurationProperty.UseChangeLog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-usechangelog
            '''
            result = self._values.get("use_change_log")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.SharePointConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SharePointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.SqlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query_identifiers_enclosing_option": "queryIdentifiersEnclosingOption",
        },
    )
    class SqlConfigurationProperty:
        def __init__(
            self,
            *,
            query_identifiers_enclosing_option: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param query_identifiers_enclosing_option: ``CfnDataSource.SqlConfigurationProperty.QueryIdentifiersEnclosingOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                sql_configuration_property = kendra.CfnDataSource.SqlConfigurationProperty(
                    query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if query_identifiers_enclosing_option is not None:
                self._values["query_identifiers_enclosing_option"] = query_identifiers_enclosing_option

        @builtins.property
        def query_identifiers_enclosing_option(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.SqlConfigurationProperty.QueryIdentifiersEnclosingOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html#cfn-kendra-datasource-sqlconfiguration-queryidentifiersenclosingoption
            '''
            result = self._values.get("query_identifiers_enclosing_option")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"basic_authentication": "basicAuthentication"},
    )
    class WebCrawlerAuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            basic_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.WebCrawlerBasicAuthenticationProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param basic_authentication: ``CfnDataSource.WebCrawlerAuthenticationConfigurationProperty.BasicAuthentication``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                web_crawler_authentication_configuration_property = kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                    basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                        credentials="credentials",
                        host="host",
                        port=123
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if basic_authentication is not None:
                self._values["basic_authentication"] = basic_authentication

        @builtins.property
        def basic_authentication(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.WebCrawlerBasicAuthenticationProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.WebCrawlerAuthenticationConfigurationProperty.BasicAuthentication``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html#cfn-kendra-datasource-webcrawlerauthenticationconfiguration-basicauthentication
            '''
            result = self._values.get("basic_authentication")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.WebCrawlerBasicAuthenticationProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerAuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"credentials": "credentials", "host": "host", "port": "port"},
    )
    class WebCrawlerBasicAuthenticationProperty:
        def __init__(
            self,
            *,
            credentials: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''
            :param credentials: ``CfnDataSource.WebCrawlerBasicAuthenticationProperty.Credentials``.
            :param host: ``CfnDataSource.WebCrawlerBasicAuthenticationProperty.Host``.
            :param port: ``CfnDataSource.WebCrawlerBasicAuthenticationProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                web_crawler_basic_authentication_property = kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                    credentials="credentials",
                    host="host",
                    port=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "credentials": credentials,
                "host": host,
                "port": port,
            }

        @builtins.property
        def credentials(self) -> builtins.str:
            '''``CfnDataSource.WebCrawlerBasicAuthenticationProperty.Credentials``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-credentials
            '''
            result = self._values.get("credentials")
            assert result is not None, "Required property 'credentials' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''``CfnDataSource.WebCrawlerBasicAuthenticationProperty.Host``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''``CfnDataSource.WebCrawlerBasicAuthenticationProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerBasicAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.WebCrawlerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "crawl_depth": "crawlDepth",
            "max_content_size_per_page_in_mega_bytes": "maxContentSizePerPageInMegaBytes",
            "max_links_per_page": "maxLinksPerPage",
            "max_urls_per_minute_crawl_rate": "maxUrlsPerMinuteCrawlRate",
            "proxy_configuration": "proxyConfiguration",
            "url_exclusion_patterns": "urlExclusionPatterns",
            "url_inclusion_patterns": "urlInclusionPatterns",
            "urls": "urls",
        },
    )
    class WebCrawlerConfigurationProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Optional[typing.Union["CfnDataSource.WebCrawlerAuthenticationConfigurationProperty", _IResolvable_da3f097b]] = None,
            crawl_depth: typing.Optional[jsii.Number] = None,
            max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
            max_links_per_page: typing.Optional[jsii.Number] = None,
            max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
            proxy_configuration: typing.Optional[typing.Union["CfnDataSource.ProxyConfigurationProperty", _IResolvable_da3f097b]] = None,
            url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            urls: typing.Union["CfnDataSource.WebCrawlerUrlsProperty", _IResolvable_da3f097b],
        ) -> None:
            '''
            :param authentication_configuration: ``CfnDataSource.WebCrawlerConfigurationProperty.AuthenticationConfiguration``.
            :param crawl_depth: ``CfnDataSource.WebCrawlerConfigurationProperty.CrawlDepth``.
            :param max_content_size_per_page_in_mega_bytes: ``CfnDataSource.WebCrawlerConfigurationProperty.MaxContentSizePerPageInMegaBytes``.
            :param max_links_per_page: ``CfnDataSource.WebCrawlerConfigurationProperty.MaxLinksPerPage``.
            :param max_urls_per_minute_crawl_rate: ``CfnDataSource.WebCrawlerConfigurationProperty.MaxUrlsPerMinuteCrawlRate``.
            :param proxy_configuration: ``CfnDataSource.WebCrawlerConfigurationProperty.ProxyConfiguration``.
            :param url_exclusion_patterns: ``CfnDataSource.WebCrawlerConfigurationProperty.UrlExclusionPatterns``.
            :param url_inclusion_patterns: ``CfnDataSource.WebCrawlerConfigurationProperty.UrlInclusionPatterns``.
            :param urls: ``CfnDataSource.WebCrawlerConfigurationProperty.Urls``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                web_crawler_configuration_property = kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                    urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                        seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                            seed_urls=["seedUrls"],
                
                            # the properties below are optional
                            web_crawler_mode="webCrawlerMode"
                        ),
                        site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                            site_maps=["siteMaps"]
                        )
                    ),
                
                    # the properties below are optional
                    authentication_configuration=kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                        basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                            credentials="credentials",
                            host="host",
                            port=123
                        )]
                    ),
                    crawl_depth=123,
                    max_content_size_per_page_in_mega_bytes=123,
                    max_links_per_page=123,
                    max_urls_per_minute_crawl_rate=123,
                    proxy_configuration=kendra.CfnDataSource.ProxyConfigurationProperty(
                        host="host",
                        port=123,
                
                        # the properties below are optional
                        credentials="credentials"
                    ),
                    url_exclusion_patterns=["urlExclusionPatterns"],
                    url_inclusion_patterns=["urlInclusionPatterns"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "urls": urls,
            }
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if crawl_depth is not None:
                self._values["crawl_depth"] = crawl_depth
            if max_content_size_per_page_in_mega_bytes is not None:
                self._values["max_content_size_per_page_in_mega_bytes"] = max_content_size_per_page_in_mega_bytes
            if max_links_per_page is not None:
                self._values["max_links_per_page"] = max_links_per_page
            if max_urls_per_minute_crawl_rate is not None:
                self._values["max_urls_per_minute_crawl_rate"] = max_urls_per_minute_crawl_rate
            if proxy_configuration is not None:
                self._values["proxy_configuration"] = proxy_configuration
            if url_exclusion_patterns is not None:
                self._values["url_exclusion_patterns"] = url_exclusion_patterns
            if url_inclusion_patterns is not None:
                self._values["url_inclusion_patterns"] = url_inclusion_patterns

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.WebCrawlerAuthenticationConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.AuthenticationConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.WebCrawlerAuthenticationConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def crawl_depth(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.CrawlDepth``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-crawldepth
            '''
            result = self._values.get("crawl_depth")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_content_size_per_page_in_mega_bytes(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.MaxContentSizePerPageInMegaBytes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxcontentsizeperpageinmegabytes
            '''
            result = self._values.get("max_content_size_per_page_in_mega_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_links_per_page(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.MaxLinksPerPage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxlinksperpage
            '''
            result = self._values.get("max_links_per_page")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_urls_per_minute_crawl_rate(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.MaxUrlsPerMinuteCrawlRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxurlsperminutecrawlrate
            '''
            result = self._values.get("max_urls_per_minute_crawl_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def proxy_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.ProxyConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.ProxyConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-proxyconfiguration
            '''
            result = self._values.get("proxy_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.ProxyConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def url_exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.UrlExclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urlexclusionpatterns
            '''
            result = self._values.get("url_exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def url_inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.UrlInclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urlinclusionpatterns
            '''
            result = self._values.get("url_inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def urls(
            self,
        ) -> typing.Union["CfnDataSource.WebCrawlerUrlsProperty", _IResolvable_da3f097b]:
            '''``CfnDataSource.WebCrawlerConfigurationProperty.Urls``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urls
            '''
            result = self._values.get("urls")
            assert result is not None, "Required property 'urls' is missing"
            return typing.cast(typing.Union["CfnDataSource.WebCrawlerUrlsProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"seed_urls": "seedUrls", "web_crawler_mode": "webCrawlerMode"},
    )
    class WebCrawlerSeedUrlConfigurationProperty:
        def __init__(
            self,
            *,
            seed_urls: typing.Sequence[builtins.str],
            web_crawler_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param seed_urls: ``CfnDataSource.WebCrawlerSeedUrlConfigurationProperty.SeedUrls``.
            :param web_crawler_mode: ``CfnDataSource.WebCrawlerSeedUrlConfigurationProperty.WebCrawlerMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                web_crawler_seed_url_configuration_property = kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                    seed_urls=["seedUrls"],
                
                    # the properties below are optional
                    web_crawler_mode="webCrawlerMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "seed_urls": seed_urls,
            }
            if web_crawler_mode is not None:
                self._values["web_crawler_mode"] = web_crawler_mode

        @builtins.property
        def seed_urls(self) -> typing.List[builtins.str]:
            '''``CfnDataSource.WebCrawlerSeedUrlConfigurationProperty.SeedUrls``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html#cfn-kendra-datasource-webcrawlerseedurlconfiguration-seedurls
            '''
            result = self._values.get("seed_urls")
            assert result is not None, "Required property 'seed_urls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def web_crawler_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDataSource.WebCrawlerSeedUrlConfigurationProperty.WebCrawlerMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html#cfn-kendra-datasource-webcrawlerseedurlconfiguration-webcrawlermode
            '''
            result = self._values.get("web_crawler_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerSeedUrlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"site_maps": "siteMaps"},
    )
    class WebCrawlerSiteMapsConfigurationProperty:
        def __init__(self, *, site_maps: typing.Sequence[builtins.str]) -> None:
            '''
            :param site_maps: ``CfnDataSource.WebCrawlerSiteMapsConfigurationProperty.SiteMaps``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                web_crawler_site_maps_configuration_property = kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                    site_maps=["siteMaps"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "site_maps": site_maps,
            }

        @builtins.property
        def site_maps(self) -> typing.List[builtins.str]:
            '''``CfnDataSource.WebCrawlerSiteMapsConfigurationProperty.SiteMaps``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html#cfn-kendra-datasource-webcrawlersitemapsconfiguration-sitemaps
            '''
            result = self._values.get("site_maps")
            assert result is not None, "Required property 'site_maps' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerSiteMapsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.WebCrawlerUrlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "seed_url_configuration": "seedUrlConfiguration",
            "site_maps_configuration": "siteMapsConfiguration",
        },
    )
    class WebCrawlerUrlsProperty:
        def __init__(
            self,
            *,
            seed_url_configuration: typing.Optional[typing.Union["CfnDataSource.WebCrawlerSeedUrlConfigurationProperty", _IResolvable_da3f097b]] = None,
            site_maps_configuration: typing.Optional[typing.Union["CfnDataSource.WebCrawlerSiteMapsConfigurationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param seed_url_configuration: ``CfnDataSource.WebCrawlerUrlsProperty.SeedUrlConfiguration``.
            :param site_maps_configuration: ``CfnDataSource.WebCrawlerUrlsProperty.SiteMapsConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                web_crawler_urls_property = kendra.CfnDataSource.WebCrawlerUrlsProperty(
                    seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                        seed_urls=["seedUrls"],
                
                        # the properties below are optional
                        web_crawler_mode="webCrawlerMode"
                    ),
                    site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                        site_maps=["siteMaps"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if seed_url_configuration is not None:
                self._values["seed_url_configuration"] = seed_url_configuration
            if site_maps_configuration is not None:
                self._values["site_maps_configuration"] = site_maps_configuration

        @builtins.property
        def seed_url_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.WebCrawlerSeedUrlConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.WebCrawlerUrlsProperty.SeedUrlConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html#cfn-kendra-datasource-webcrawlerurls-seedurlconfiguration
            '''
            result = self._values.get("seed_url_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.WebCrawlerSeedUrlConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def site_maps_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.WebCrawlerSiteMapsConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnDataSource.WebCrawlerUrlsProperty.SiteMapsConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html#cfn-kendra-datasource-webcrawlerurls-sitemapsconfiguration
            '''
            result = self._values.get("site_maps_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnDataSource.WebCrawlerSiteMapsConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerUrlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnDataSource.WorkDocsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crawl_comments": "crawlComments",
            "exclusion_patterns": "exclusionPatterns",
            "field_mappings": "fieldMappings",
            "inclusion_patterns": "inclusionPatterns",
            "organization_id": "organizationId",
            "use_change_log": "useChangeLog",
        },
    )
    class WorkDocsConfigurationProperty:
        def __init__(
            self,
            *,
            crawl_comments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            organization_id: builtins.str,
            use_change_log: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param crawl_comments: ``CfnDataSource.WorkDocsConfigurationProperty.CrawlComments``.
            :param exclusion_patterns: ``CfnDataSource.WorkDocsConfigurationProperty.ExclusionPatterns``.
            :param field_mappings: ``CfnDataSource.WorkDocsConfigurationProperty.FieldMappings``.
            :param inclusion_patterns: ``CfnDataSource.WorkDocsConfigurationProperty.InclusionPatterns``.
            :param organization_id: ``CfnDataSource.WorkDocsConfigurationProperty.OrganizationId``.
            :param use_change_log: ``CfnDataSource.WorkDocsConfigurationProperty.UseChangeLog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                work_docs_configuration_property = kendra.CfnDataSource.WorkDocsConfigurationProperty(
                    organization_id="organizationId",
                
                    # the properties below are optional
                    crawl_comments=False,
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"],
                    use_change_log=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "organization_id": organization_id,
            }
            if crawl_comments is not None:
                self._values["crawl_comments"] = crawl_comments
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns
            if use_change_log is not None:
                self._values["use_change_log"] = use_change_log

        @builtins.property
        def crawl_comments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.WorkDocsConfigurationProperty.CrawlComments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-crawlcomments
            '''
            result = self._values.get("crawl_comments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.WorkDocsConfigurationProperty.ExclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]]:
            '''``CfnDataSource.WorkDocsConfigurationProperty.FieldMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataSource.WorkDocsConfigurationProperty.InclusionPatterns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def organization_id(self) -> builtins.str:
            '''``CfnDataSource.WorkDocsConfigurationProperty.OrganizationId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-organizationid
            '''
            result = self._values.get("organization_id")
            assert result is not None, "Required property 'organization_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def use_change_log(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnDataSource.WorkDocsConfigurationProperty.UseChangeLog``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-usechangelog
            '''
            result = self._values.get("use_change_log")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkDocsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kendra.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_configuration": "dataSourceConfiguration",
        "description": "description",
        "index_id": "indexId",
        "name": "name",
        "role_arn": "roleArn",
        "schedule": "schedule",
        "tags": "tags",
        "type": "type",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        data_source_configuration: typing.Optional[typing.Union[CfnDataSource.DataSourceConfigurationProperty, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        index_id: builtins.str,
        name: builtins.str,
        role_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        type: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::Kendra::DataSource``.

        :param data_source_configuration: ``AWS::Kendra::DataSource.DataSourceConfiguration``.
        :param description: ``AWS::Kendra::DataSource.Description``.
        :param index_id: ``AWS::Kendra::DataSource.IndexId``.
        :param name: ``AWS::Kendra::DataSource.Name``.
        :param role_arn: ``AWS::Kendra::DataSource.RoleArn``.
        :param schedule: ``AWS::Kendra::DataSource.Schedule``.
        :param tags: ``AWS::Kendra::DataSource.Tags``.
        :param type: ``AWS::Kendra::DataSource.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kendra as kendra
            
            cfn_data_source_props = kendra.CfnDataSourceProps(
                index_id="indexId",
                name="name",
                type="type",
            
                # the properties below are optional
                data_source_configuration=kendra.CfnDataSource.DataSourceConfigurationProperty(
                    confluence_configuration=kendra.CfnDataSource.ConfluenceConfigurationProperty(
                        secret_arn="secretArn",
                        server_url="serverUrl",
                        version="version",
            
                        # the properties below are optional
                        attachment_configuration=kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                            attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            crawl_attachments=False
                        ),
                        blog_configuration=kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                            blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        exclusion_patterns=["exclusionPatterns"],
                        inclusion_patterns=["inclusionPatterns"],
                        page_configuration=kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                            page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        space_configuration=kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                            crawl_archived_spaces=False,
                            crawl_personal_spaces=False,
                            exclude_spaces=["excludeSpaces"],
                            include_spaces=["includeSpaces"],
                            space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    database_configuration=kendra.CfnDataSource.DatabaseConfigurationProperty(
                        column_configuration=kendra.CfnDataSource.ColumnConfigurationProperty(
                            change_detecting_columns=["changeDetectingColumns"],
                            document_data_column_name="documentDataColumnName",
                            document_id_column_name="documentIdColumnName",
            
                            # the properties below are optional
                            document_title_column_name="documentTitleColumnName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        connection_configuration=kendra.CfnDataSource.ConnectionConfigurationProperty(
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            secret_arn="secretArn",
                            table_name="tableName"
                        ),
                        database_engine_type="databaseEngineType",
            
                        # the properties below are optional
                        acl_configuration=kendra.CfnDataSource.AclConfigurationProperty(
                            allowed_groups_column_name="allowedGroupsColumnName"
                        ),
                        sql_configuration=kendra.CfnDataSource.SqlConfigurationProperty(
                            query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                        ),
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    google_drive_configuration=kendra.CfnDataSource.GoogleDriveConfigurationProperty(
                        secret_arn="secretArn",
            
                        # the properties below are optional
                        exclude_mime_types=["excludeMimeTypes"],
                        exclude_shared_drives=["excludeSharedDrives"],
                        exclude_user_accounts=["excludeUserAccounts"],
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
            
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"]
                    ),
                    one_drive_configuration=kendra.CfnDataSource.OneDriveConfigurationProperty(
                        one_drive_users=kendra.CfnDataSource.OneDriveUsersProperty(
                            one_drive_user_list=["oneDriveUserList"],
                            one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        secret_arn="secretArn",
                        tenant_domain="tenantDomain",
            
                        # the properties below are optional
                        disable_local_groups=False,
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
            
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"]
                    ),
                    s3_configuration=kendra.CfnDataSource.S3DataSourceConfigurationProperty(
                        bucket_name="bucketName",
            
                        # the properties below are optional
                        access_control_list_configuration=kendra.CfnDataSource.AccessControlListConfigurationProperty(
                            key_path="keyPath"
                        ),
                        documents_metadata_configuration=kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                            s3_prefix="s3Prefix"
                        ),
                        exclusion_patterns=["exclusionPatterns"],
                        inclusion_patterns=["inclusionPatterns"],
                        inclusion_prefixes=["inclusionPrefixes"]
                    ),
                    salesforce_configuration=kendra.CfnDataSource.SalesforceConfigurationProperty(
                        secret_arn="secretArn",
                        server_url="serverUrl",
            
                        # the properties below are optional
                        chatter_feed_configuration=kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
            
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            include_filter_types=["includeFilterTypes"]
                        ),
                        crawl_attachments=False,
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"],
                        knowledge_article_configuration=kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                            included_states=["includedStates"],
            
                            # the properties below are optional
                            custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                                document_data_field_name="documentDataFieldName",
                                name="name",
            
                                # the properties below are optional
                                document_title_field_name="documentTitleFieldName",
                                field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                    data_source_field_name="dataSourceFieldName",
                                    index_field_name="indexFieldName",
            
                                    # the properties below are optional
                                    date_field_format="dateFieldFormat"
                                )]
                            )],
                            standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                                document_data_field_name="documentDataFieldName",
            
                                # the properties below are optional
                                document_title_field_name="documentTitleFieldName",
                                field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                    data_source_field_name="dataSourceFieldName",
                                    index_field_name="indexFieldName",
            
                                    # the properties below are optional
                                    date_field_format="dateFieldFormat"
                                )]
                            )
                        ),
                        standard_object_attachment_configuration=kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        standard_object_configurations=[kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                            name="name",
            
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )]
                    ),
                    service_now_configuration=kendra.CfnDataSource.ServiceNowConfigurationProperty(
                        host_url="hostUrl",
                        secret_arn="secretArn",
                        service_now_build_version="serviceNowBuildVersion",
            
                        # the properties below are optional
                        authentication_type="authenticationType",
                        knowledge_article_configuration=kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
            
                            # the properties below are optional
                            crawl_attachments=False,
                            document_title_field_name="documentTitleFieldName",
                            exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            filter_query="filterQuery",
                            include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                        ),
                        service_catalog_configuration=kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
            
                            # the properties below are optional
                            crawl_attachments=False,
                            document_title_field_name="documentTitleFieldName",
                            exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                        )
                    ),
                    share_point_configuration=kendra.CfnDataSource.SharePointConfigurationProperty(
                        secret_arn="secretArn",
                        share_point_version="sharePointVersion",
                        urls=["urls"],
            
                        # the properties below are optional
                        crawl_attachments=False,
                        disable_local_groups=False,
                        document_title_field_name="documentTitleFieldName",
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
            
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"],
                        ssl_certificate_s3_path=kendra.CfnDataSource.S3PathProperty(
                            bucket="bucket",
                            key="key"
                        ),
                        use_change_log=False,
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    web_crawler_configuration=kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                        urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                            seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                                seed_urls=["seedUrls"],
            
                                # the properties below are optional
                                web_crawler_mode="webCrawlerMode"
                            ),
                            site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                                site_maps=["siteMaps"]
                            )
                        ),
            
                        # the properties below are optional
                        authentication_configuration=kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                            basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                                credentials="credentials",
                                host="host",
                                port=123
                            )]
                        ),
                        crawl_depth=123,
                        max_content_size_per_page_in_mega_bytes=123,
                        max_links_per_page=123,
                        max_urls_per_minute_crawl_rate=123,
                        proxy_configuration=kendra.CfnDataSource.ProxyConfigurationProperty(
                            host="host",
                            port=123,
            
                            # the properties below are optional
                            credentials="credentials"
                        ),
                        url_exclusion_patterns=["urlExclusionPatterns"],
                        url_inclusion_patterns=["urlInclusionPatterns"]
                    ),
                    work_docs_configuration=kendra.CfnDataSource.WorkDocsConfigurationProperty(
                        organization_id="organizationId",
            
                        # the properties below are optional
                        crawl_comments=False,
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
            
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"],
                        use_change_log=False
                    )
                ),
                description="description",
                role_arn="roleArn",
                schedule="schedule",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "index_id": index_id,
            "name": name,
            "type": type,
        }
        if data_source_configuration is not None:
            self._values["data_source_configuration"] = data_source_configuration
        if description is not None:
            self._values["description"] = description
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if schedule is not None:
            self._values["schedule"] = schedule
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.DataSourceConfigurationProperty, _IResolvable_da3f097b]]:
        '''``AWS::Kendra::DataSource.DataSourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-datasourceconfiguration
        '''
        result = self._values.get("data_source_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.DataSourceConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::DataSource.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''``AWS::Kendra::DataSource.IndexId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-indexid
        '''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Kendra::DataSource.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::DataSource.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::DataSource.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::Kendra::DataSource.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::Kendra::DataSource.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFaq(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kendra.CfnFaq",
):
    '''A CloudFormation ``AWS::Kendra::Faq``.

    :cloudformationResource: AWS::Kendra::Faq
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kendra as kendra
        
        cfn_faq = kendra.CfnFaq(self, "MyCfnFaq",
            index_id="indexId",
            name="name",
            role_arn="roleArn",
            s3_path=kendra.CfnFaq.S3PathProperty(
                bucket="bucket",
                key="key"
            ),
        
            # the properties below are optional
            description="description",
            file_format="fileFormat",
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
        description: typing.Optional[builtins.str] = None,
        file_format: typing.Optional[builtins.str] = None,
        index_id: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        s3_path: typing.Union["CfnFaq.S3PathProperty", _IResolvable_da3f097b],
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::Kendra::Faq``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::Kendra::Faq.Description``.
        :param file_format: ``AWS::Kendra::Faq.FileFormat``.
        :param index_id: ``AWS::Kendra::Faq.IndexId``.
        :param name: ``AWS::Kendra::Faq.Name``.
        :param role_arn: ``AWS::Kendra::Faq.RoleArn``.
        :param s3_path: ``AWS::Kendra::Faq.S3Path``.
        :param tags: ``AWS::Kendra::Faq.Tags``.
        '''
        props = CfnFaqProps(
            description=description,
            file_format=file_format,
            index_id=index_id,
            name=name,
            role_arn=role_arn,
            s3_path=s3_path,
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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::Faq.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileFormat")
    def file_format(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::Faq.FileFormat``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileFormat"))

    @file_format.setter
    def file_format(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "fileFormat", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="indexId")
    def index_id(self) -> builtins.str:
        '''``AWS::Kendra::Faq.IndexId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
        '''
        return typing.cast(builtins.str, jsii.get(self, "indexId"))

    @index_id.setter
    def index_id(self, value: builtins.str) -> None:
        jsii.set(self, "indexId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Kendra::Faq.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::Kendra::Faq.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3Path")
    def s3_path(self) -> typing.Union["CfnFaq.S3PathProperty", _IResolvable_da3f097b]:
        '''``AWS::Kendra::Faq.S3Path``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
        '''
        return typing.cast(typing.Union["CfnFaq.S3PathProperty", _IResolvable_da3f097b], jsii.get(self, "s3Path"))

    @s3_path.setter
    def s3_path(
        self,
        value: typing.Union["CfnFaq.S3PathProperty", _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "s3Path", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::Kendra::Faq.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnFaq.S3PathProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3PathProperty:
        def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
            '''
            :param bucket: ``CfnFaq.S3PathProperty.Bucket``.
            :param key: ``CfnFaq.S3PathProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                s3_path_property = kendra.CfnFaq.S3PathProperty(
                    bucket="bucket",
                    key="key"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''``CfnFaq.S3PathProperty.Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html#cfn-kendra-faq-s3path-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnFaq.S3PathProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html#cfn-kendra-faq-s3path-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3PathProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kendra.CfnFaqProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "file_format": "fileFormat",
        "index_id": "indexId",
        "name": "name",
        "role_arn": "roleArn",
        "s3_path": "s3Path",
        "tags": "tags",
    },
)
class CfnFaqProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        file_format: typing.Optional[builtins.str] = None,
        index_id: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        s3_path: typing.Union[CfnFaq.S3PathProperty, _IResolvable_da3f097b],
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Kendra::Faq``.

        :param description: ``AWS::Kendra::Faq.Description``.
        :param file_format: ``AWS::Kendra::Faq.FileFormat``.
        :param index_id: ``AWS::Kendra::Faq.IndexId``.
        :param name: ``AWS::Kendra::Faq.Name``.
        :param role_arn: ``AWS::Kendra::Faq.RoleArn``.
        :param s3_path: ``AWS::Kendra::Faq.S3Path``.
        :param tags: ``AWS::Kendra::Faq.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kendra as kendra
            
            cfn_faq_props = kendra.CfnFaqProps(
                index_id="indexId",
                name="name",
                role_arn="roleArn",
                s3_path=kendra.CfnFaq.S3PathProperty(
                    bucket="bucket",
                    key="key"
                ),
            
                # the properties below are optional
                description="description",
                file_format="fileFormat",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "index_id": index_id,
            "name": name,
            "role_arn": role_arn,
            "s3_path": s3_path,
        }
        if description is not None:
            self._values["description"] = description
        if file_format is not None:
            self._values["file_format"] = file_format
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::Faq.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_format(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::Faq.FileFormat``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
        '''
        result = self._values.get("file_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''``AWS::Kendra::Faq.IndexId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
        '''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Kendra::Faq.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::Kendra::Faq.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_path(self) -> typing.Union[CfnFaq.S3PathProperty, _IResolvable_da3f097b]:
        '''``AWS::Kendra::Faq.S3Path``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
        '''
        result = self._values.get("s3_path")
        assert result is not None, "Required property 's3_path' is missing"
        return typing.cast(typing.Union[CfnFaq.S3PathProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::Kendra::Faq.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFaqProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIndex(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kendra.CfnIndex",
):
    '''A CloudFormation ``AWS::Kendra::Index``.

    :cloudformationResource: AWS::Kendra::Index
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kendra as kendra
        
        cfn_index = kendra.CfnIndex(self, "MyCfnIndex",
            edition="edition",
            name="name",
            role_arn="roleArn",
        
            # the properties below are optional
            capacity_units=kendra.CfnIndex.CapacityUnitsConfigurationProperty(
                query_capacity_units=123,
                storage_capacity_units=123
            ),
            description="description",
            document_metadata_configurations=[kendra.CfnIndex.DocumentMetadataConfigurationProperty(
                name="name",
                type="type",
        
                # the properties below are optional
                relevance=kendra.CfnIndex.RelevanceProperty(
                    duration="duration",
                    freshness=False,
                    importance=123,
                    rank_order="rankOrder",
                    value_importance_items=[kendra.CfnIndex.ValueImportanceItemProperty(
                        key="key",
                        value=123
                    )]
                ),
                search=kendra.CfnIndex.SearchProperty(
                    displayable=False,
                    facetable=False,
                    searchable=False,
                    sortable=False
                )
            )],
            server_side_encryption_configuration=kendra.CfnIndex.ServerSideEncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_context_policy="userContextPolicy",
            user_token_configurations=[kendra.CfnIndex.UserTokenConfigurationProperty(
                json_token_type_configuration=kendra.CfnIndex.JsonTokenTypeConfigurationProperty(
                    group_attribute_field="groupAttributeField",
                    user_name_attribute_field="userNameAttributeField"
                ),
                jwt_token_type_configuration=kendra.CfnIndex.JwtTokenTypeConfigurationProperty(
                    key_location="keyLocation",
        
                    # the properties below are optional
                    claim_regex="claimRegex",
                    group_attribute_field="groupAttributeField",
                    issuer="issuer",
                    secret_manager_arn="secretManagerArn",
                    url="url",
                    user_name_attribute_field="userNameAttributeField"
                )
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        capacity_units: typing.Optional[typing.Union["CfnIndex.CapacityUnitsConfigurationProperty", _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        document_metadata_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnIndex.DocumentMetadataConfigurationProperty", _IResolvable_da3f097b]]]] = None,
        edition: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        server_side_encryption_configuration: typing.Optional[typing.Union["CfnIndex.ServerSideEncryptionConfigurationProperty", _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        user_context_policy: typing.Optional[builtins.str] = None,
        user_token_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnIndex.UserTokenConfigurationProperty", _IResolvable_da3f097b]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Kendra::Index``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param capacity_units: ``AWS::Kendra::Index.CapacityUnits``.
        :param description: ``AWS::Kendra::Index.Description``.
        :param document_metadata_configurations: ``AWS::Kendra::Index.DocumentMetadataConfigurations``.
        :param edition: ``AWS::Kendra::Index.Edition``.
        :param name: ``AWS::Kendra::Index.Name``.
        :param role_arn: ``AWS::Kendra::Index.RoleArn``.
        :param server_side_encryption_configuration: ``AWS::Kendra::Index.ServerSideEncryptionConfiguration``.
        :param tags: ``AWS::Kendra::Index.Tags``.
        :param user_context_policy: ``AWS::Kendra::Index.UserContextPolicy``.
        :param user_token_configurations: ``AWS::Kendra::Index.UserTokenConfigurations``.
        '''
        props = CfnIndexProps(
            capacity_units=capacity_units,
            description=description,
            document_metadata_configurations=document_metadata_configurations,
            edition=edition,
            name=name,
            role_arn=role_arn,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
            user_context_policy=user_context_policy,
            user_token_configurations=user_token_configurations,
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
    @jsii.member(jsii_name="capacityUnits")
    def capacity_units(
        self,
    ) -> typing.Optional[typing.Union["CfnIndex.CapacityUnitsConfigurationProperty", _IResolvable_da3f097b]]:
        '''``AWS::Kendra::Index.CapacityUnits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-capacityunits
        '''
        return typing.cast(typing.Optional[typing.Union["CfnIndex.CapacityUnitsConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "capacityUnits"))

    @capacity_units.setter
    def capacity_units(
        self,
        value: typing.Optional[typing.Union["CfnIndex.CapacityUnitsConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "capacityUnits", value)

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
        '''``AWS::Kendra::Index.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="documentMetadataConfigurations")
    def document_metadata_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnIndex.DocumentMetadataConfigurationProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::Kendra::Index.DocumentMetadataConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-documentmetadataconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnIndex.DocumentMetadataConfigurationProperty", _IResolvable_da3f097b]]]], jsii.get(self, "documentMetadataConfigurations"))

    @document_metadata_configurations.setter
    def document_metadata_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnIndex.DocumentMetadataConfigurationProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "documentMetadataConfigurations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="edition")
    def edition(self) -> builtins.str:
        '''``AWS::Kendra::Index.Edition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-edition
        '''
        return typing.cast(builtins.str, jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: builtins.str) -> None:
        jsii.set(self, "edition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Kendra::Index.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::Kendra::Index.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnIndex.ServerSideEncryptionConfigurationProperty", _IResolvable_da3f097b]]:
        '''``AWS::Kendra::Index.ServerSideEncryptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-serversideencryptionconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnIndex.ServerSideEncryptionConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "serverSideEncryptionConfiguration"))

    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(
        self,
        value: typing.Optional[typing.Union["CfnIndex.ServerSideEncryptionConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "serverSideEncryptionConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::Kendra::Index.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userContextPolicy")
    def user_context_policy(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::Index.UserContextPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usercontextpolicy
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userContextPolicy"))

    @user_context_policy.setter
    def user_context_policy(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "userContextPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userTokenConfigurations")
    def user_token_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnIndex.UserTokenConfigurationProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::Kendra::Index.UserTokenConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usertokenconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnIndex.UserTokenConfigurationProperty", _IResolvable_da3f097b]]]], jsii.get(self, "userTokenConfigurations"))

    @user_token_configurations.setter
    def user_token_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnIndex.UserTokenConfigurationProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "userTokenConfigurations", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.CapacityUnitsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query_capacity_units": "queryCapacityUnits",
            "storage_capacity_units": "storageCapacityUnits",
        },
    )
    class CapacityUnitsConfigurationProperty:
        def __init__(
            self,
            *,
            query_capacity_units: jsii.Number,
            storage_capacity_units: jsii.Number,
        ) -> None:
            '''
            :param query_capacity_units: ``CfnIndex.CapacityUnitsConfigurationProperty.QueryCapacityUnits``.
            :param storage_capacity_units: ``CfnIndex.CapacityUnitsConfigurationProperty.StorageCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                capacity_units_configuration_property = kendra.CfnIndex.CapacityUnitsConfigurationProperty(
                    query_capacity_units=123,
                    storage_capacity_units=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "query_capacity_units": query_capacity_units,
                "storage_capacity_units": storage_capacity_units,
            }

        @builtins.property
        def query_capacity_units(self) -> jsii.Number:
            '''``CfnIndex.CapacityUnitsConfigurationProperty.QueryCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html#cfn-kendra-index-capacityunitsconfiguration-querycapacityunits
            '''
            result = self._values.get("query_capacity_units")
            assert result is not None, "Required property 'query_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def storage_capacity_units(self) -> jsii.Number:
            '''``CfnIndex.CapacityUnitsConfigurationProperty.StorageCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html#cfn-kendra-index-capacityunitsconfiguration-storagecapacityunits
            '''
            result = self._values.get("storage_capacity_units")
            assert result is not None, "Required property 'storage_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityUnitsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.DocumentMetadataConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "relevance": "relevance",
            "search": "search",
            "type": "type",
        },
    )
    class DocumentMetadataConfigurationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            relevance: typing.Optional[typing.Union["CfnIndex.RelevanceProperty", _IResolvable_da3f097b]] = None,
            search: typing.Optional[typing.Union["CfnIndex.SearchProperty", _IResolvable_da3f097b]] = None,
            type: builtins.str,
        ) -> None:
            '''
            :param name: ``CfnIndex.DocumentMetadataConfigurationProperty.Name``.
            :param relevance: ``CfnIndex.DocumentMetadataConfigurationProperty.Relevance``.
            :param search: ``CfnIndex.DocumentMetadataConfigurationProperty.Search``.
            :param type: ``CfnIndex.DocumentMetadataConfigurationProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                document_metadata_configuration_property = kendra.CfnIndex.DocumentMetadataConfigurationProperty(
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    relevance=kendra.CfnIndex.RelevanceProperty(
                        duration="duration",
                        freshness=False,
                        importance=123,
                        rank_order="rankOrder",
                        value_importance_items=[kendra.CfnIndex.ValueImportanceItemProperty(
                            key="key",
                            value=123
                        )]
                    ),
                    search=kendra.CfnIndex.SearchProperty(
                        displayable=False,
                        facetable=False,
                        searchable=False,
                        sortable=False
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if relevance is not None:
                self._values["relevance"] = relevance
            if search is not None:
                self._values["search"] = search

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnIndex.DocumentMetadataConfigurationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def relevance(
            self,
        ) -> typing.Optional[typing.Union["CfnIndex.RelevanceProperty", _IResolvable_da3f097b]]:
            '''``CfnIndex.DocumentMetadataConfigurationProperty.Relevance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-relevance
            '''
            result = self._values.get("relevance")
            return typing.cast(typing.Optional[typing.Union["CfnIndex.RelevanceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def search(
            self,
        ) -> typing.Optional[typing.Union["CfnIndex.SearchProperty", _IResolvable_da3f097b]]:
            '''``CfnIndex.DocumentMetadataConfigurationProperty.Search``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-search
            '''
            result = self._values.get("search")
            return typing.cast(typing.Optional[typing.Union["CfnIndex.SearchProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnIndex.DocumentMetadataConfigurationProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentMetadataConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.JsonTokenTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "group_attribute_field": "groupAttributeField",
            "user_name_attribute_field": "userNameAttributeField",
        },
    )
    class JsonTokenTypeConfigurationProperty:
        def __init__(
            self,
            *,
            group_attribute_field: builtins.str,
            user_name_attribute_field: builtins.str,
        ) -> None:
            '''
            :param group_attribute_field: ``CfnIndex.JsonTokenTypeConfigurationProperty.GroupAttributeField``.
            :param user_name_attribute_field: ``CfnIndex.JsonTokenTypeConfigurationProperty.UserNameAttributeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                json_token_type_configuration_property = kendra.CfnIndex.JsonTokenTypeConfigurationProperty(
                    group_attribute_field="groupAttributeField",
                    user_name_attribute_field="userNameAttributeField"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "group_attribute_field": group_attribute_field,
                "user_name_attribute_field": user_name_attribute_field,
            }

        @builtins.property
        def group_attribute_field(self) -> builtins.str:
            '''``CfnIndex.JsonTokenTypeConfigurationProperty.GroupAttributeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html#cfn-kendra-index-jsontokentypeconfiguration-groupattributefield
            '''
            result = self._values.get("group_attribute_field")
            assert result is not None, "Required property 'group_attribute_field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_name_attribute_field(self) -> builtins.str:
            '''``CfnIndex.JsonTokenTypeConfigurationProperty.UserNameAttributeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html#cfn-kendra-index-jsontokentypeconfiguration-usernameattributefield
            '''
            result = self._values.get("user_name_attribute_field")
            assert result is not None, "Required property 'user_name_attribute_field' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonTokenTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.JwtTokenTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "claim_regex": "claimRegex",
            "group_attribute_field": "groupAttributeField",
            "issuer": "issuer",
            "key_location": "keyLocation",
            "secret_manager_arn": "secretManagerArn",
            "url": "url",
            "user_name_attribute_field": "userNameAttributeField",
        },
    )
    class JwtTokenTypeConfigurationProperty:
        def __init__(
            self,
            *,
            claim_regex: typing.Optional[builtins.str] = None,
            group_attribute_field: typing.Optional[builtins.str] = None,
            issuer: typing.Optional[builtins.str] = None,
            key_location: builtins.str,
            secret_manager_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            user_name_attribute_field: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param claim_regex: ``CfnIndex.JwtTokenTypeConfigurationProperty.ClaimRegex``.
            :param group_attribute_field: ``CfnIndex.JwtTokenTypeConfigurationProperty.GroupAttributeField``.
            :param issuer: ``CfnIndex.JwtTokenTypeConfigurationProperty.Issuer``.
            :param key_location: ``CfnIndex.JwtTokenTypeConfigurationProperty.KeyLocation``.
            :param secret_manager_arn: ``CfnIndex.JwtTokenTypeConfigurationProperty.SecretManagerArn``.
            :param url: ``CfnIndex.JwtTokenTypeConfigurationProperty.URL``.
            :param user_name_attribute_field: ``CfnIndex.JwtTokenTypeConfigurationProperty.UserNameAttributeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                jwt_token_type_configuration_property = kendra.CfnIndex.JwtTokenTypeConfigurationProperty(
                    key_location="keyLocation",
                
                    # the properties below are optional
                    claim_regex="claimRegex",
                    group_attribute_field="groupAttributeField",
                    issuer="issuer",
                    secret_manager_arn="secretManagerArn",
                    url="url",
                    user_name_attribute_field="userNameAttributeField"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key_location": key_location,
            }
            if claim_regex is not None:
                self._values["claim_regex"] = claim_regex
            if group_attribute_field is not None:
                self._values["group_attribute_field"] = group_attribute_field
            if issuer is not None:
                self._values["issuer"] = issuer
            if secret_manager_arn is not None:
                self._values["secret_manager_arn"] = secret_manager_arn
            if url is not None:
                self._values["url"] = url
            if user_name_attribute_field is not None:
                self._values["user_name_attribute_field"] = user_name_attribute_field

        @builtins.property
        def claim_regex(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.JwtTokenTypeConfigurationProperty.ClaimRegex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-claimregex
            '''
            result = self._values.get("claim_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def group_attribute_field(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.JwtTokenTypeConfigurationProperty.GroupAttributeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-groupattributefield
            '''
            result = self._values.get("group_attribute_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def issuer(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.JwtTokenTypeConfigurationProperty.Issuer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-issuer
            '''
            result = self._values.get("issuer")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_location(self) -> builtins.str:
            '''``CfnIndex.JwtTokenTypeConfigurationProperty.KeyLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-keylocation
            '''
            result = self._values.get("key_location")
            assert result is not None, "Required property 'key_location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_manager_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.JwtTokenTypeConfigurationProperty.SecretManagerArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.JwtTokenTypeConfigurationProperty.URL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_name_attribute_field(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.JwtTokenTypeConfigurationProperty.UserNameAttributeField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-usernameattributefield
            '''
            result = self._values.get("user_name_attribute_field")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JwtTokenTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.RelevanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "duration": "duration",
            "freshness": "freshness",
            "importance": "importance",
            "rank_order": "rankOrder",
            "value_importance_items": "valueImportanceItems",
        },
    )
    class RelevanceProperty:
        def __init__(
            self,
            *,
            duration: typing.Optional[builtins.str] = None,
            freshness: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            importance: typing.Optional[jsii.Number] = None,
            rank_order: typing.Optional[builtins.str] = None,
            value_importance_items: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnIndex.ValueImportanceItemProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''
            :param duration: ``CfnIndex.RelevanceProperty.Duration``.
            :param freshness: ``CfnIndex.RelevanceProperty.Freshness``.
            :param importance: ``CfnIndex.RelevanceProperty.Importance``.
            :param rank_order: ``CfnIndex.RelevanceProperty.RankOrder``.
            :param value_importance_items: ``CfnIndex.RelevanceProperty.ValueImportanceItems``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                relevance_property = kendra.CfnIndex.RelevanceProperty(
                    duration="duration",
                    freshness=False,
                    importance=123,
                    rank_order="rankOrder",
                    value_importance_items=[kendra.CfnIndex.ValueImportanceItemProperty(
                        key="key",
                        value=123
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if duration is not None:
                self._values["duration"] = duration
            if freshness is not None:
                self._values["freshness"] = freshness
            if importance is not None:
                self._values["importance"] = importance
            if rank_order is not None:
                self._values["rank_order"] = rank_order
            if value_importance_items is not None:
                self._values["value_importance_items"] = value_importance_items

        @builtins.property
        def duration(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.RelevanceProperty.Duration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-duration
            '''
            result = self._values.get("duration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def freshness(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnIndex.RelevanceProperty.Freshness``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-freshness
            '''
            result = self._values.get("freshness")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def importance(self) -> typing.Optional[jsii.Number]:
            '''``CfnIndex.RelevanceProperty.Importance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-importance
            '''
            result = self._values.get("importance")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rank_order(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.RelevanceProperty.RankOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-rankorder
            '''
            result = self._values.get("rank_order")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value_importance_items(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnIndex.ValueImportanceItemProperty", _IResolvable_da3f097b]]]]:
            '''``CfnIndex.RelevanceProperty.ValueImportanceItems``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-valueimportanceitems
            '''
            result = self._values.get("value_importance_items")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnIndex.ValueImportanceItemProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelevanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.SearchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "displayable": "displayable",
            "facetable": "facetable",
            "searchable": "searchable",
            "sortable": "sortable",
        },
    )
    class SearchProperty:
        def __init__(
            self,
            *,
            displayable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            facetable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            searchable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            sortable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param displayable: ``CfnIndex.SearchProperty.Displayable``.
            :param facetable: ``CfnIndex.SearchProperty.Facetable``.
            :param searchable: ``CfnIndex.SearchProperty.Searchable``.
            :param sortable: ``CfnIndex.SearchProperty.Sortable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                search_property = kendra.CfnIndex.SearchProperty(
                    displayable=False,
                    facetable=False,
                    searchable=False,
                    sortable=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if displayable is not None:
                self._values["displayable"] = displayable
            if facetable is not None:
                self._values["facetable"] = facetable
            if searchable is not None:
                self._values["searchable"] = searchable
            if sortable is not None:
                self._values["sortable"] = sortable

        @builtins.property
        def displayable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnIndex.SearchProperty.Displayable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-displayable
            '''
            result = self._values.get("displayable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def facetable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnIndex.SearchProperty.Facetable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-facetable
            '''
            result = self._values.get("facetable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def searchable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnIndex.SearchProperty.Searchable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-searchable
            '''
            result = self._values.get("searchable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def sortable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``CfnIndex.SearchProperty.Sortable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-sortable
            '''
            result = self._values.get("sortable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SearchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.ServerSideEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class ServerSideEncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''
            :param kms_key_id: ``CfnIndex.ServerSideEncryptionConfigurationProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                server_side_encryption_configuration_property = kendra.CfnIndex.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.ServerSideEncryptionConfigurationProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html#cfn-kendra-index-serversideencryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.UserTokenConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "json_token_type_configuration": "jsonTokenTypeConfiguration",
            "jwt_token_type_configuration": "jwtTokenTypeConfiguration",
        },
    )
    class UserTokenConfigurationProperty:
        def __init__(
            self,
            *,
            json_token_type_configuration: typing.Optional[typing.Union["CfnIndex.JsonTokenTypeConfigurationProperty", _IResolvable_da3f097b]] = None,
            jwt_token_type_configuration: typing.Optional[typing.Union["CfnIndex.JwtTokenTypeConfigurationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param json_token_type_configuration: ``CfnIndex.UserTokenConfigurationProperty.JsonTokenTypeConfiguration``.
            :param jwt_token_type_configuration: ``CfnIndex.UserTokenConfigurationProperty.JwtTokenTypeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                user_token_configuration_property = kendra.CfnIndex.UserTokenConfigurationProperty(
                    json_token_type_configuration=kendra.CfnIndex.JsonTokenTypeConfigurationProperty(
                        group_attribute_field="groupAttributeField",
                        user_name_attribute_field="userNameAttributeField"
                    ),
                    jwt_token_type_configuration=kendra.CfnIndex.JwtTokenTypeConfigurationProperty(
                        key_location="keyLocation",
                
                        # the properties below are optional
                        claim_regex="claimRegex",
                        group_attribute_field="groupAttributeField",
                        issuer="issuer",
                        secret_manager_arn="secretManagerArn",
                        url="url",
                        user_name_attribute_field="userNameAttributeField"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if json_token_type_configuration is not None:
                self._values["json_token_type_configuration"] = json_token_type_configuration
            if jwt_token_type_configuration is not None:
                self._values["jwt_token_type_configuration"] = jwt_token_type_configuration

        @builtins.property
        def json_token_type_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnIndex.JsonTokenTypeConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnIndex.UserTokenConfigurationProperty.JsonTokenTypeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html#cfn-kendra-index-usertokenconfiguration-jsontokentypeconfiguration
            '''
            result = self._values.get("json_token_type_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnIndex.JsonTokenTypeConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def jwt_token_type_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnIndex.JwtTokenTypeConfigurationProperty", _IResolvable_da3f097b]]:
            '''``CfnIndex.UserTokenConfigurationProperty.JwtTokenTypeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html#cfn-kendra-index-usertokenconfiguration-jwttokentypeconfiguration
            '''
            result = self._values.get("jwt_token_type_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnIndex.JwtTokenTypeConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserTokenConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kendra.CfnIndex.ValueImportanceItemProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ValueImportanceItemProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param key: ``CfnIndex.ValueImportanceItemProperty.Key``.
            :param value: ``CfnIndex.ValueImportanceItemProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kendra as kendra
                
                value_importance_item_property = kendra.CfnIndex.ValueImportanceItemProperty(
                    key="key",
                    value=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnIndex.ValueImportanceItemProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html#cfn-kendra-index-valueimportanceitem-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''``CfnIndex.ValueImportanceItemProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html#cfn-kendra-index-valueimportanceitem-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValueImportanceItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kendra.CfnIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_units": "capacityUnits",
        "description": "description",
        "document_metadata_configurations": "documentMetadataConfigurations",
        "edition": "edition",
        "name": "name",
        "role_arn": "roleArn",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
        "user_context_policy": "userContextPolicy",
        "user_token_configurations": "userTokenConfigurations",
    },
)
class CfnIndexProps:
    def __init__(
        self,
        *,
        capacity_units: typing.Optional[typing.Union[CfnIndex.CapacityUnitsConfigurationProperty, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        document_metadata_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnIndex.DocumentMetadataConfigurationProperty, _IResolvable_da3f097b]]]] = None,
        edition: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        server_side_encryption_configuration: typing.Optional[typing.Union[CfnIndex.ServerSideEncryptionConfigurationProperty, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        user_context_policy: typing.Optional[builtins.str] = None,
        user_token_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnIndex.UserTokenConfigurationProperty, _IResolvable_da3f097b]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Kendra::Index``.

        :param capacity_units: ``AWS::Kendra::Index.CapacityUnits``.
        :param description: ``AWS::Kendra::Index.Description``.
        :param document_metadata_configurations: ``AWS::Kendra::Index.DocumentMetadataConfigurations``.
        :param edition: ``AWS::Kendra::Index.Edition``.
        :param name: ``AWS::Kendra::Index.Name``.
        :param role_arn: ``AWS::Kendra::Index.RoleArn``.
        :param server_side_encryption_configuration: ``AWS::Kendra::Index.ServerSideEncryptionConfiguration``.
        :param tags: ``AWS::Kendra::Index.Tags``.
        :param user_context_policy: ``AWS::Kendra::Index.UserContextPolicy``.
        :param user_token_configurations: ``AWS::Kendra::Index.UserTokenConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kendra as kendra
            
            cfn_index_props = kendra.CfnIndexProps(
                edition="edition",
                name="name",
                role_arn="roleArn",
            
                # the properties below are optional
                capacity_units=kendra.CfnIndex.CapacityUnitsConfigurationProperty(
                    query_capacity_units=123,
                    storage_capacity_units=123
                ),
                description="description",
                document_metadata_configurations=[kendra.CfnIndex.DocumentMetadataConfigurationProperty(
                    name="name",
                    type="type",
            
                    # the properties below are optional
                    relevance=kendra.CfnIndex.RelevanceProperty(
                        duration="duration",
                        freshness=False,
                        importance=123,
                        rank_order="rankOrder",
                        value_importance_items=[kendra.CfnIndex.ValueImportanceItemProperty(
                            key="key",
                            value=123
                        )]
                    ),
                    search=kendra.CfnIndex.SearchProperty(
                        displayable=False,
                        facetable=False,
                        searchable=False,
                        sortable=False
                    )
                )],
                server_side_encryption_configuration=kendra.CfnIndex.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_context_policy="userContextPolicy",
                user_token_configurations=[kendra.CfnIndex.UserTokenConfigurationProperty(
                    json_token_type_configuration=kendra.CfnIndex.JsonTokenTypeConfigurationProperty(
                        group_attribute_field="groupAttributeField",
                        user_name_attribute_field="userNameAttributeField"
                    ),
                    jwt_token_type_configuration=kendra.CfnIndex.JwtTokenTypeConfigurationProperty(
                        key_location="keyLocation",
            
                        # the properties below are optional
                        claim_regex="claimRegex",
                        group_attribute_field="groupAttributeField",
                        issuer="issuer",
                        secret_manager_arn="secretManagerArn",
                        url="url",
                        user_name_attribute_field="userNameAttributeField"
                    )
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "edition": edition,
            "name": name,
            "role_arn": role_arn,
        }
        if capacity_units is not None:
            self._values["capacity_units"] = capacity_units
        if description is not None:
            self._values["description"] = description
        if document_metadata_configurations is not None:
            self._values["document_metadata_configurations"] = document_metadata_configurations
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags
        if user_context_policy is not None:
            self._values["user_context_policy"] = user_context_policy
        if user_token_configurations is not None:
            self._values["user_token_configurations"] = user_token_configurations

    @builtins.property
    def capacity_units(
        self,
    ) -> typing.Optional[typing.Union[CfnIndex.CapacityUnitsConfigurationProperty, _IResolvable_da3f097b]]:
        '''``AWS::Kendra::Index.CapacityUnits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-capacityunits
        '''
        result = self._values.get("capacity_units")
        return typing.cast(typing.Optional[typing.Union[CfnIndex.CapacityUnitsConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::Index.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_metadata_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnIndex.DocumentMetadataConfigurationProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::Kendra::Index.DocumentMetadataConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-documentmetadataconfigurations
        '''
        result = self._values.get("document_metadata_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnIndex.DocumentMetadataConfigurationProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def edition(self) -> builtins.str:
        '''``AWS::Kendra::Index.Edition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-edition
        '''
        result = self._values.get("edition")
        assert result is not None, "Required property 'edition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Kendra::Index.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::Kendra::Index.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnIndex.ServerSideEncryptionConfigurationProperty, _IResolvable_da3f097b]]:
        '''``AWS::Kendra::Index.ServerSideEncryptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-serversideencryptionconfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnIndex.ServerSideEncryptionConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::Kendra::Index.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_context_policy(self) -> typing.Optional[builtins.str]:
        '''``AWS::Kendra::Index.UserContextPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usercontextpolicy
        '''
        result = self._values.get("user_context_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_token_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnIndex.UserTokenConfigurationProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::Kendra::Index.UserTokenConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usertokenconfigurations
        '''
        result = self._values.get("user_token_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnIndex.UserTokenConfigurationProperty, _IResolvable_da3f097b]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnFaq",
    "CfnFaqProps",
    "CfnIndex",
    "CfnIndexProps",
]

publication.publish()
