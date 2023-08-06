'''
# Amazon DynamoDB Construct Library

Here is a minimal deployable DynamoDB table definition:

```python
table = dynamodb.Table(self, "Table",
    partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING)
)
```

## Importing existing tables

To import an existing table into your CDK application, use the `Table.fromTableName`, `Table.fromTableArn` or `Table.fromTableAttributes`
factory method. This method accepts table name or table ARN which describes the properties of an already
existing table:

```python
# user is of type User

table = dynamodb.Table.from_table_arn(self, "ImportedTable", "arn:aws:dynamodb:us-east-1:111111111:table/my-table")
# now you can just call methods on the table
table.grant_read_write_data(user)
```

If you intend to use the `tableStreamArn` (including indirectly, for example by creating an
`@aws-cdk/aws-lambda-event-source.DynamoEventSource` on the imported table), you *must* use the
`Table.fromTableAttributes` method and the `tableStreamArn` property *must* be populated.

## Keys

When a table is defined, you must define it's schema using the `partitionKey`
(required) and `sortKey` (optional) properties.

## Billing Mode

DynamoDB supports two billing modes:

* PROVISIONED - the default mode where the table and global secondary indexes have configured read and write capacity.
* PAY_PER_REQUEST - on-demand pricing and scaling. You only pay for what you use and there is no read and write capacity for the table or its global secondary indexes.

```python
table = dynamodb.Table(self, "Table",
    partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
)
```

Further reading:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.

## Configure AutoScaling for your table

You can have DynamoDB automatically raise and lower the read and write capacities
of your table by setting up autoscaling. You can use this to either keep your
tables at a desired utilization level, or by scaling up and down at pre-configured
times of the day:

Auto-scaling is only relevant for tables with the billing mode, PROVISIONED.

[Example of configuring autoscaling](test/integ.autoscaling.lit.ts)

Further reading:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html
https://aws.amazon.com/blogs/database/how-to-use-aws-cloudformation-to-configure-auto-scaling-for-amazon-dynamodb-tables-and-indexes/

## Amazon DynamoDB Global Tables

You can create DynamoDB Global Tables by setting the `replicationRegions` property on a `Table`:

```python
global_table = dynamodb.Table(self, "Table",
    partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    replication_regions=["us-east-1", "us-east-2", "us-west-2"]
)
```

When doing so, a CloudFormation Custom Resource will be added to the stack in order to create the replica tables in the
selected regions.

The default billing mode for Global Tables is `PAY_PER_REQUEST`.
If you want to use `PROVISIONED`,
you have to make sure write auto-scaling is enabled for that Table:

```python
global_table = dynamodb.Table(self, "Table",
    partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    replication_regions=["us-east-1", "us-east-2", "us-west-2"],
    billing_mode=dynamodb.BillingMode.PROVISIONED
)

global_table.auto_scale_write_capacity(
    min_capacity=1,
    max_capacity=10
).scale_on_utilization(target_utilization_percent=75)
```

When adding a replica region for a large table, you might want to increase the
timeout for the replication operation:

```python
global_table = dynamodb.Table(self, "Table",
    partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    replication_regions=["us-east-1", "us-east-2", "us-west-2"],
    replication_timeout=Duration.hours(2)
)
```

## Encryption

All user data stored in Amazon DynamoDB is fully encrypted at rest. When creating a new table, you can choose to encrypt using the following customer master keys (CMK) to encrypt your table:

* AWS owned CMK - By default, all tables are encrypted under an AWS owned customer master key (CMK) in the DynamoDB service account (no additional charges apply).
* AWS managed CMK - AWS KMS keys (one per region) are created in your account, managed, and used on your behalf by AWS DynamoDB (AWS KMS charges apply).
* Customer managed CMK - You have full control over the KMS key used to encrypt the DynamoDB Table (AWS KMS charges apply).

Creating a Table encrypted with a customer managed CMK:

```python
table = dynamodb.Table(self, "MyTable",
    partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    encryption=dynamodb.TableEncryption.CUSTOMER_MANAGED
)

# You can access the CMK that was added to the stack on your behalf by the Table construct via:
table_encryption_key = table.encryption_key
```

You can also supply your own key:

```python
import monocdk as kms


encryption_key = kms.Key(self, "Key",
    enable_key_rotation=True
)
table = dynamodb.Table(self, "MyTable",
    partition_key=kms.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    encryption=dynamodb.TableEncryption.CUSTOMER_MANAGED,
    encryption_key=encryption_key
)
```

In order to use the AWS managed CMK instead, change the code to:

```python
table = dynamodb.Table(self, "MyTable",
    partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    encryption=dynamodb.TableEncryption.AWS_MANAGED
)
```

## Get schema of table or secondary indexes

To get the partition key and sort key of the table or indexes you have configured:

```python
# table is of type Table

schema = table.schema()
partition_key = schema.partition_key
sort_key = schema.sort_key
```

## Kinesis Stream

A Kinesis Data Stream can be configured on the DynamoDB table to capture item-level changes.

```python
import monocdk as kinesis


stream = kinesis.Stream(self, "Stream")

table = dynamodb.Table(self, "Table",
    partition_key=kinesis.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
    kinesis_stream=stream
)
```
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
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    Duration as _Duration_070aa057,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResource as _IResource_8c1dbbbd,
    RemovalPolicy as _RemovalPolicy_c97e7a20,
    Resource as _Resource_abff4495,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..aws_applicationautoscaling import (
    BaseTargetTrackingProps as _BaseTargetTrackingProps_e4402570,
    ScalingSchedule as _ScalingSchedule_6c3fc38f,
    Schedule as _Schedule_c2a5a45d,
)
from ..aws_cloudwatch import (
    IMetric as _IMetric_5db43d61,
    Metric as _Metric_5b2b8e58,
    MetricOptions as _MetricOptions_1c185ae8,
    Unit as _Unit_113c79f9,
)
from ..aws_iam import Grant as _Grant_bcb5eae7, IGrantable as _IGrantable_4c5a91d1
from ..aws_kinesis import IStream as _IStream_14c6ec7f
from ..aws_kms import IKey as _IKey_36930160


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.Attribute",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class Attribute:
    def __init__(self, *, name: builtins.str, type: "AttributeType") -> None:
        '''(experimental) Represents an attribute for describing the key schema for the table and indexes.

        :param name: (experimental) The name of an attribute.
        :param type: (experimental) The data type of an attribute.

        :stability: experimental

        Example::

            global_table = dynamodb.Table(self, "Table",
                partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
                replication_regions=["us-east-1", "us-east-2", "us-west-2"],
                billing_mode=dynamodb.BillingMode.PROVISIONED
            )
            
            global_table.auto_scale_write_capacity(
                min_capacity=1,
                max_capacity=10
            ).scale_on_utilization(target_utilization_percent=75)
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The name of an attribute.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "AttributeType":
        '''(experimental) The data type of an attribute.

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("AttributeType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Attribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_dynamodb.AttributeType")
class AttributeType(enum.Enum):
    '''(experimental) Data types for attributes within a table.

    :see: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes
    :stability: experimental

    Example::

        global_table = dynamodb.Table(self, "Table",
            partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            replication_regions=["us-east-1", "us-east-2", "us-west-2"],
            billing_mode=dynamodb.BillingMode.PROVISIONED
        )
        
        global_table.auto_scale_write_capacity(
            min_capacity=1,
            max_capacity=10
        ).scale_on_utilization(target_utilization_percent=75)
    '''

    BINARY = "BINARY"
    '''(experimental) Up to 400KiB of binary data (which must be encoded as base64 before sending to DynamoDB).

    :stability: experimental
    '''
    NUMBER = "NUMBER"
    '''(experimental) Numeric values made of up to 38 digits (positive, negative or zero).

    :stability: experimental
    '''
    STRING = "STRING"
    '''(experimental) Up to 400KiB of UTF-8 encoded text.

    :stability: experimental
    '''


@jsii.enum(jsii_type="monocdk.aws_dynamodb.BillingMode")
class BillingMode(enum.Enum):
    '''(experimental) DynamoDB's Read/Write capacity modes.

    :stability: experimental

    Example::

        table = dynamodb.Table(self, "Table",
            partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )
    '''

    PAY_PER_REQUEST = "PAY_PER_REQUEST"
    '''(experimental) Pay only for what you use.

    You don't configure Read/Write capacity units.

    :stability: experimental
    '''
    PROVISIONED = "PROVISIONED"
    '''(experimental) Explicitly specified Read/Write capacity units.

    :stability: experimental
    '''


@jsii.implements(_IInspectable_82c04a63)
class CfnGlobalTable(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dynamodb.CfnGlobalTable",
):
    '''A CloudFormation ``AWS::DynamoDB::GlobalTable``.

    :cloudformationResource: AWS::DynamoDB::GlobalTable
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_dynamodb as dynamodb
        
        cfn_global_table = dynamodb.CfnGlobalTable(self, "MyCfnGlobalTable",
            attribute_definitions=[dynamodb.CfnGlobalTable.AttributeDefinitionProperty(
                attribute_name="attributeName",
                attribute_type="attributeType"
            )],
            key_schema=[dynamodb.CfnGlobalTable.KeySchemaProperty(
                attribute_name="attributeName",
                key_type="keyType"
            )],
            replicas=[dynamodb.CfnGlobalTable.ReplicaSpecificationProperty(
                region="region",
        
                # the properties below are optional
                contributor_insights_specification=dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty(
                    enabled=False
                ),
                global_secondary_indexes=[dynamodb.CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty(
                    index_name="indexName",
        
                    # the properties below are optional
                    contributor_insights_specification=dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty(
                        enabled=False
                    ),
                    read_provisioned_throughput_settings=dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty(
                        read_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                            max_capacity=123,
                            min_capacity=123,
                            target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                                target_value=123,
        
                                # the properties below are optional
                                disable_scale_in=False,
                                scale_in_cooldown=123,
                                scale_out_cooldown=123
                            ),
        
                            # the properties below are optional
                            seed_capacity=123
                        ),
                        read_capacity_units=123
                    )
                )],
                point_in_time_recovery_specification=dynamodb.CfnGlobalTable.PointInTimeRecoverySpecificationProperty(
                    point_in_time_recovery_enabled=False
                ),
                read_provisioned_throughput_settings=dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty(
                    read_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                        max_capacity=123,
                        min_capacity=123,
                        target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                            target_value=123,
        
                            # the properties below are optional
                            disable_scale_in=False,
                            scale_in_cooldown=123,
                            scale_out_cooldown=123
                        ),
        
                        # the properties below are optional
                        seed_capacity=123
                    ),
                    read_capacity_units=123
                ),
                sse_specification=dynamodb.CfnGlobalTable.ReplicaSSESpecificationProperty(
                    kms_master_key_id="kmsMasterKeyId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )],
        
            # the properties below are optional
            billing_mode="billingMode",
            global_secondary_indexes=[dynamodb.CfnGlobalTable.GlobalSecondaryIndexProperty(
                index_name="indexName",
                key_schema=[dynamodb.CfnGlobalTable.KeySchemaProperty(
                    attribute_name="attributeName",
                    key_type="keyType"
                )],
                projection=dynamodb.CfnGlobalTable.ProjectionProperty(
                    non_key_attributes=["nonKeyAttributes"],
                    projection_type="projectionType"
                ),
        
                # the properties below are optional
                write_provisioned_throughput_settings=dynamodb.CfnGlobalTable.WriteProvisionedThroughputSettingsProperty(
                    write_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                        max_capacity=123,
                        min_capacity=123,
                        target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                            target_value=123,
        
                            # the properties below are optional
                            disable_scale_in=False,
                            scale_in_cooldown=123,
                            scale_out_cooldown=123
                        ),
        
                        # the properties below are optional
                        seed_capacity=123
                    )
                )
            )],
            local_secondary_indexes=[dynamodb.CfnGlobalTable.LocalSecondaryIndexProperty(
                index_name="indexName",
                key_schema=[dynamodb.CfnGlobalTable.KeySchemaProperty(
                    attribute_name="attributeName",
                    key_type="keyType"
                )],
                projection=dynamodb.CfnGlobalTable.ProjectionProperty(
                    non_key_attributes=["nonKeyAttributes"],
                    projection_type="projectionType"
                )
            )],
            sse_specification=dynamodb.CfnGlobalTable.SSESpecificationProperty(
                sse_enabled=False,
        
                # the properties below are optional
                sse_type="sseType"
            ),
            stream_specification=dynamodb.CfnGlobalTable.StreamSpecificationProperty(
                stream_view_type="streamViewType"
            ),
            table_name="tableName",
            time_to_live_specification=dynamodb.CfnGlobalTable.TimeToLiveSpecificationProperty(
                enabled=False,
        
                # the properties below are optional
                attribute_name="attributeName"
            ),
            write_provisioned_throughput_settings=dynamodb.CfnGlobalTable.WriteProvisionedThroughputSettingsProperty(
                write_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                    max_capacity=123,
                    min_capacity=123,
                    target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                        target_value=123,
        
                        # the properties below are optional
                        disable_scale_in=False,
                        scale_in_cooldown=123,
                        scale_out_cooldown=123
                    ),
        
                    # the properties below are optional
                    seed_capacity=123
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        attribute_definitions: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnGlobalTable.AttributeDefinitionProperty", _IResolvable_a771d0ef]]],
        billing_mode: typing.Optional[builtins.str] = None,
        global_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnGlobalTable.GlobalSecondaryIndexProperty", _IResolvable_a771d0ef]]]] = None,
        key_schema: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]],
        local_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnGlobalTable.LocalSecondaryIndexProperty", _IResolvable_a771d0ef]]]] = None,
        replicas: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnGlobalTable.ReplicaSpecificationProperty", _IResolvable_a771d0ef]]],
        sse_specification: typing.Optional[typing.Union["CfnGlobalTable.SSESpecificationProperty", _IResolvable_a771d0ef]] = None,
        stream_specification: typing.Optional[typing.Union["CfnGlobalTable.StreamSpecificationProperty", _IResolvable_a771d0ef]] = None,
        table_name: typing.Optional[builtins.str] = None,
        time_to_live_specification: typing.Optional[typing.Union["CfnGlobalTable.TimeToLiveSpecificationProperty", _IResolvable_a771d0ef]] = None,
        write_provisioned_throughput_settings: typing.Optional[typing.Union["CfnGlobalTable.WriteProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::DynamoDB::GlobalTable``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param attribute_definitions: ``AWS::DynamoDB::GlobalTable.AttributeDefinitions``.
        :param billing_mode: ``AWS::DynamoDB::GlobalTable.BillingMode``.
        :param global_secondary_indexes: ``AWS::DynamoDB::GlobalTable.GlobalSecondaryIndexes``.
        :param key_schema: ``AWS::DynamoDB::GlobalTable.KeySchema``.
        :param local_secondary_indexes: ``AWS::DynamoDB::GlobalTable.LocalSecondaryIndexes``.
        :param replicas: ``AWS::DynamoDB::GlobalTable.Replicas``.
        :param sse_specification: ``AWS::DynamoDB::GlobalTable.SSESpecification``.
        :param stream_specification: ``AWS::DynamoDB::GlobalTable.StreamSpecification``.
        :param table_name: ``AWS::DynamoDB::GlobalTable.TableName``.
        :param time_to_live_specification: ``AWS::DynamoDB::GlobalTable.TimeToLiveSpecification``.
        :param write_provisioned_throughput_settings: ``AWS::DynamoDB::GlobalTable.WriteProvisionedThroughputSettings``.
        '''
        props = CfnGlobalTableProps(
            attribute_definitions=attribute_definitions,
            billing_mode=billing_mode,
            global_secondary_indexes=global_secondary_indexes,
            key_schema=key_schema,
            local_secondary_indexes=local_secondary_indexes,
            replicas=replicas,
            sse_specification=sse_specification,
            stream_specification=stream_specification,
            table_name=table_name,
            time_to_live_specification=time_to_live_specification,
            write_provisioned_throughput_settings=write_provisioned_throughput_settings,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attributeDefinitions")
    def attribute_definitions(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.AttributeDefinitionProperty", _IResolvable_a771d0ef]]]:
        '''``AWS::DynamoDB::GlobalTable.AttributeDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-attributedefinitions
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.AttributeDefinitionProperty", _IResolvable_a771d0ef]]], jsii.get(self, "attributeDefinitions"))

    @attribute_definitions.setter
    def attribute_definitions(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.AttributeDefinitionProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        jsii.set(self, "attributeDefinitions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStreamArn")
    def attr_stream_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: StreamArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStreamArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTableId")
    def attr_table_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: TableId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTableId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="billingMode")
    def billing_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::GlobalTable.BillingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-billingmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingMode"))

    @billing_mode.setter
    def billing_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "billingMode", value)

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
    @jsii.member(jsii_name="globalSecondaryIndexes")
    def global_secondary_indexes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.GlobalSecondaryIndexProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::GlobalTable.GlobalSecondaryIndexes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-globalsecondaryindexes
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.GlobalSecondaryIndexProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "globalSecondaryIndexes"))

    @global_secondary_indexes.setter
    def global_secondary_indexes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.GlobalSecondaryIndexProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "globalSecondaryIndexes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keySchema")
    def key_schema(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]]:
        '''``AWS::DynamoDB::GlobalTable.KeySchema``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-keyschema
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]], jsii.get(self, "keySchema"))

    @key_schema.setter
    def key_schema(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        jsii.set(self, "keySchema", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="localSecondaryIndexes")
    def local_secondary_indexes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.LocalSecondaryIndexProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::GlobalTable.LocalSecondaryIndexes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-localsecondaryindexes
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.LocalSecondaryIndexProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "localSecondaryIndexes"))

    @local_secondary_indexes.setter
    def local_secondary_indexes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.LocalSecondaryIndexProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "localSecondaryIndexes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicas")
    def replicas(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.ReplicaSpecificationProperty", _IResolvable_a771d0ef]]]:
        '''``AWS::DynamoDB::GlobalTable.Replicas``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-replicas
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.ReplicaSpecificationProperty", _IResolvable_a771d0ef]]], jsii.get(self, "replicas"))

    @replicas.setter
    def replicas(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.ReplicaSpecificationProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        jsii.set(self, "replicas", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sseSpecification")
    def sse_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnGlobalTable.SSESpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::GlobalTable.SSESpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-ssespecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.SSESpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "sseSpecification"))

    @sse_specification.setter
    def sse_specification(
        self,
        value: typing.Optional[typing.Union["CfnGlobalTable.SSESpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "sseSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="streamSpecification")
    def stream_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnGlobalTable.StreamSpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::GlobalTable.StreamSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-streamspecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.StreamSpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "streamSpecification"))

    @stream_specification.setter
    def stream_specification(
        self,
        value: typing.Optional[typing.Union["CfnGlobalTable.StreamSpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "streamSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::GlobalTable.TableName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-tablename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tableName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeToLiveSpecification")
    def time_to_live_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnGlobalTable.TimeToLiveSpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::GlobalTable.TimeToLiveSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-timetolivespecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.TimeToLiveSpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "timeToLiveSpecification"))

    @time_to_live_specification.setter
    def time_to_live_specification(
        self,
        value: typing.Optional[typing.Union["CfnGlobalTable.TimeToLiveSpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "timeToLiveSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="writeProvisionedThroughputSettings")
    def write_provisioned_throughput_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnGlobalTable.WriteProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::GlobalTable.WriteProvisionedThroughputSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.WriteProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "writeProvisionedThroughputSettings"))

    @write_provisioned_throughput_settings.setter
    def write_provisioned_throughput_settings(
        self,
        value: typing.Optional[typing.Union["CfnGlobalTable.WriteProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "writeProvisionedThroughputSettings", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.AttributeDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_name": "attributeName",
            "attribute_type": "attributeType",
        },
    )
    class AttributeDefinitionProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            attribute_type: builtins.str,
        ) -> None:
            '''
            :param attribute_name: ``CfnGlobalTable.AttributeDefinitionProperty.AttributeName``.
            :param attribute_type: ``CfnGlobalTable.AttributeDefinitionProperty.AttributeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                attribute_definition_property = dynamodb.CfnGlobalTable.AttributeDefinitionProperty(
                    attribute_name="attributeName",
                    attribute_type="attributeType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attribute_name": attribute_name,
                "attribute_type": attribute_type,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''``CfnGlobalTable.AttributeDefinitionProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html#cfn-dynamodb-globaltable-attributedefinition-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute_type(self) -> builtins.str:
            '''``CfnGlobalTable.AttributeDefinitionProperty.AttributeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html#cfn-dynamodb-globaltable-attributedefinition-attributetype
            '''
            result = self._values.get("attribute_type")
            assert result is not None, "Required property 'attribute_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_capacity": "maxCapacity",
            "min_capacity": "minCapacity",
            "seed_capacity": "seedCapacity",
            "target_tracking_scaling_policy_configuration": "targetTrackingScalingPolicyConfiguration",
        },
    )
    class CapacityAutoScalingSettingsProperty:
        def __init__(
            self,
            *,
            max_capacity: jsii.Number,
            min_capacity: jsii.Number,
            seed_capacity: typing.Optional[jsii.Number] = None,
            target_tracking_scaling_policy_configuration: typing.Union["CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param max_capacity: ``CfnGlobalTable.CapacityAutoScalingSettingsProperty.MaxCapacity``.
            :param min_capacity: ``CfnGlobalTable.CapacityAutoScalingSettingsProperty.MinCapacity``.
            :param seed_capacity: ``CfnGlobalTable.CapacityAutoScalingSettingsProperty.SeedCapacity``.
            :param target_tracking_scaling_policy_configuration: ``CfnGlobalTable.CapacityAutoScalingSettingsProperty.TargetTrackingScalingPolicyConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                capacity_auto_scaling_settings_property = dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                    max_capacity=123,
                    min_capacity=123,
                    target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                        target_value=123,
                
                        # the properties below are optional
                        disable_scale_in=False,
                        scale_in_cooldown=123,
                        scale_out_cooldown=123
                    ),
                
                    # the properties below are optional
                    seed_capacity=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_capacity": max_capacity,
                "min_capacity": min_capacity,
                "target_tracking_scaling_policy_configuration": target_tracking_scaling_policy_configuration,
            }
            if seed_capacity is not None:
                self._values["seed_capacity"] = seed_capacity

        @builtins.property
        def max_capacity(self) -> jsii.Number:
            '''``CfnGlobalTable.CapacityAutoScalingSettingsProperty.MaxCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-maxcapacity
            '''
            result = self._values.get("max_capacity")
            assert result is not None, "Required property 'max_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_capacity(self) -> jsii.Number:
            '''``CfnGlobalTable.CapacityAutoScalingSettingsProperty.MinCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-mincapacity
            '''
            result = self._values.get("min_capacity")
            assert result is not None, "Required property 'min_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def seed_capacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnGlobalTable.CapacityAutoScalingSettingsProperty.SeedCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-seedcapacity
            '''
            result = self._values.get("seed_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def target_tracking_scaling_policy_configuration(
            self,
        ) -> typing.Union["CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]:
            '''``CfnGlobalTable.CapacityAutoScalingSettingsProperty.TargetTrackingScalingPolicyConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-targettrackingscalingpolicyconfiguration
            '''
            result = self._values.get("target_tracking_scaling_policy_configuration")
            assert result is not None, "Required property 'target_tracking_scaling_policy_configuration' is missing"
            return typing.cast(typing.Union["CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityAutoScalingSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class ContributorInsightsSpecificationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param enabled: ``CfnGlobalTable.ContributorInsightsSpecificationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                contributor_insights_specification_property = dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty(
                    enabled=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
            '''``CfnGlobalTable.ContributorInsightsSpecificationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html#cfn-dynamodb-globaltable-contributorinsightsspecification-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContributorInsightsSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.GlobalSecondaryIndexProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "key_schema": "keySchema",
            "projection": "projection",
            "write_provisioned_throughput_settings": "writeProvisionedThroughputSettings",
        },
    )
    class GlobalSecondaryIndexProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            key_schema: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]],
            projection: typing.Union["CfnGlobalTable.ProjectionProperty", _IResolvable_a771d0ef],
            write_provisioned_throughput_settings: typing.Optional[typing.Union["CfnGlobalTable.WriteProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param index_name: ``CfnGlobalTable.GlobalSecondaryIndexProperty.IndexName``.
            :param key_schema: ``CfnGlobalTable.GlobalSecondaryIndexProperty.KeySchema``.
            :param projection: ``CfnGlobalTable.GlobalSecondaryIndexProperty.Projection``.
            :param write_provisioned_throughput_settings: ``CfnGlobalTable.GlobalSecondaryIndexProperty.WriteProvisionedThroughputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                global_secondary_index_property = dynamodb.CfnGlobalTable.GlobalSecondaryIndexProperty(
                    index_name="indexName",
                    key_schema=[dynamodb.CfnGlobalTable.KeySchemaProperty(
                        attribute_name="attributeName",
                        key_type="keyType"
                    )],
                    projection=dynamodb.CfnGlobalTable.ProjectionProperty(
                        non_key_attributes=["nonKeyAttributes"],
                        projection_type="projectionType"
                    ),
                
                    # the properties below are optional
                    write_provisioned_throughput_settings=dynamodb.CfnGlobalTable.WriteProvisionedThroughputSettingsProperty(
                        write_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                            max_capacity=123,
                            min_capacity=123,
                            target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                                target_value=123,
                
                                # the properties below are optional
                                disable_scale_in=False,
                                scale_in_cooldown=123,
                                scale_out_cooldown=123
                            ),
                
                            # the properties below are optional
                            seed_capacity=123
                        )
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "index_name": index_name,
                "key_schema": key_schema,
                "projection": projection,
            }
            if write_provisioned_throughput_settings is not None:
                self._values["write_provisioned_throughput_settings"] = write_provisioned_throughput_settings

        @builtins.property
        def index_name(self) -> builtins.str:
            '''``CfnGlobalTable.GlobalSecondaryIndexProperty.IndexName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_schema(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]]:
            '''``CfnGlobalTable.GlobalSecondaryIndexProperty.KeySchema``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-keyschema
            '''
            result = self._values.get("key_schema")
            assert result is not None, "Required property 'key_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def projection(
            self,
        ) -> typing.Union["CfnGlobalTable.ProjectionProperty", _IResolvable_a771d0ef]:
            '''``CfnGlobalTable.GlobalSecondaryIndexProperty.Projection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-projection
            '''
            result = self._values.get("projection")
            assert result is not None, "Required property 'projection' is missing"
            return typing.cast(typing.Union["CfnGlobalTable.ProjectionProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def write_provisioned_throughput_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.WriteProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.GlobalSecondaryIndexProperty.WriteProvisionedThroughputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-writeprovisionedthroughputsettings
            '''
            result = self._values.get("write_provisioned_throughput_settings")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.WriteProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlobalSecondaryIndexProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.KeySchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_name": "attributeName", "key_type": "keyType"},
    )
    class KeySchemaProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            key_type: builtins.str,
        ) -> None:
            '''
            :param attribute_name: ``CfnGlobalTable.KeySchemaProperty.AttributeName``.
            :param key_type: ``CfnGlobalTable.KeySchemaProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                key_schema_property = dynamodb.CfnGlobalTable.KeySchemaProperty(
                    attribute_name="attributeName",
                    key_type="keyType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attribute_name": attribute_name,
                "key_type": key_type,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''``CfnGlobalTable.KeySchemaProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html#cfn-dynamodb-globaltable-keyschema-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_type(self) -> builtins.str:
            '''``CfnGlobalTable.KeySchemaProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html#cfn-dynamodb-globaltable-keyschema-keytype
            '''
            result = self._values.get("key_type")
            assert result is not None, "Required property 'key_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeySchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.LocalSecondaryIndexProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "key_schema": "keySchema",
            "projection": "projection",
        },
    )
    class LocalSecondaryIndexProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            key_schema: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]],
            projection: typing.Union["CfnGlobalTable.ProjectionProperty", _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param index_name: ``CfnGlobalTable.LocalSecondaryIndexProperty.IndexName``.
            :param key_schema: ``CfnGlobalTable.LocalSecondaryIndexProperty.KeySchema``.
            :param projection: ``CfnGlobalTable.LocalSecondaryIndexProperty.Projection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                local_secondary_index_property = dynamodb.CfnGlobalTable.LocalSecondaryIndexProperty(
                    index_name="indexName",
                    key_schema=[dynamodb.CfnGlobalTable.KeySchemaProperty(
                        attribute_name="attributeName",
                        key_type="keyType"
                    )],
                    projection=dynamodb.CfnGlobalTable.ProjectionProperty(
                        non_key_attributes=["nonKeyAttributes"],
                        projection_type="projectionType"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "index_name": index_name,
                "key_schema": key_schema,
                "projection": projection,
            }

        @builtins.property
        def index_name(self) -> builtins.str:
            '''``CfnGlobalTable.LocalSecondaryIndexProperty.IndexName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_schema(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]]:
            '''``CfnGlobalTable.LocalSecondaryIndexProperty.KeySchema``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-keyschema
            '''
            result = self._values.get("key_schema")
            assert result is not None, "Required property 'key_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.KeySchemaProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def projection(
            self,
        ) -> typing.Union["CfnGlobalTable.ProjectionProperty", _IResolvable_a771d0ef]:
            '''``CfnGlobalTable.LocalSecondaryIndexProperty.Projection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-projection
            '''
            result = self._values.get("projection")
            assert result is not None, "Required property 'projection' is missing"
            return typing.cast(typing.Union["CfnGlobalTable.ProjectionProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalSecondaryIndexProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.PointInTimeRecoverySpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"point_in_time_recovery_enabled": "pointInTimeRecoveryEnabled"},
    )
    class PointInTimeRecoverySpecificationProperty:
        def __init__(
            self,
            *,
            point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param point_in_time_recovery_enabled: ``CfnGlobalTable.PointInTimeRecoverySpecificationProperty.PointInTimeRecoveryEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                point_in_time_recovery_specification_property = dynamodb.CfnGlobalTable.PointInTimeRecoverySpecificationProperty(
                    point_in_time_recovery_enabled=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if point_in_time_recovery_enabled is not None:
                self._values["point_in_time_recovery_enabled"] = point_in_time_recovery_enabled

        @builtins.property
        def point_in_time_recovery_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.PointInTimeRecoverySpecificationProperty.PointInTimeRecoveryEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html#cfn-dynamodb-globaltable-pointintimerecoveryspecification-pointintimerecoveryenabled
            '''
            result = self._values.get("point_in_time_recovery_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PointInTimeRecoverySpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.ProjectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "non_key_attributes": "nonKeyAttributes",
            "projection_type": "projectionType",
        },
    )
    class ProjectionProperty:
        def __init__(
            self,
            *,
            non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
            projection_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param non_key_attributes: ``CfnGlobalTable.ProjectionProperty.NonKeyAttributes``.
            :param projection_type: ``CfnGlobalTable.ProjectionProperty.ProjectionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                projection_property = dynamodb.CfnGlobalTable.ProjectionProperty(
                    non_key_attributes=["nonKeyAttributes"],
                    projection_type="projectionType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if non_key_attributes is not None:
                self._values["non_key_attributes"] = non_key_attributes
            if projection_type is not None:
                self._values["projection_type"] = projection_type

        @builtins.property
        def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnGlobalTable.ProjectionProperty.NonKeyAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html#cfn-dynamodb-globaltable-projection-nonkeyattributes
            '''
            result = self._values.get("non_key_attributes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def projection_type(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalTable.ProjectionProperty.ProjectionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html#cfn-dynamodb-globaltable-projection-projectiontype
            '''
            result = self._values.get("projection_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProjectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "read_capacity_auto_scaling_settings": "readCapacityAutoScalingSettings",
            "read_capacity_units": "readCapacityUnits",
        },
    )
    class ReadProvisionedThroughputSettingsProperty:
        def __init__(
            self,
            *,
            read_capacity_auto_scaling_settings: typing.Optional[typing.Union["CfnGlobalTable.CapacityAutoScalingSettingsProperty", _IResolvable_a771d0ef]] = None,
            read_capacity_units: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param read_capacity_auto_scaling_settings: ``CfnGlobalTable.ReadProvisionedThroughputSettingsProperty.ReadCapacityAutoScalingSettings``.
            :param read_capacity_units: ``CfnGlobalTable.ReadProvisionedThroughputSettingsProperty.ReadCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                read_provisioned_throughput_settings_property = dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty(
                    read_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                        max_capacity=123,
                        min_capacity=123,
                        target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                            target_value=123,
                
                            # the properties below are optional
                            disable_scale_in=False,
                            scale_in_cooldown=123,
                            scale_out_cooldown=123
                        ),
                
                        # the properties below are optional
                        seed_capacity=123
                    ),
                    read_capacity_units=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if read_capacity_auto_scaling_settings is not None:
                self._values["read_capacity_auto_scaling_settings"] = read_capacity_auto_scaling_settings
            if read_capacity_units is not None:
                self._values["read_capacity_units"] = read_capacity_units

        @builtins.property
        def read_capacity_auto_scaling_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.CapacityAutoScalingSettingsProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.ReadProvisionedThroughputSettingsProperty.ReadCapacityAutoScalingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityautoscalingsettings
            '''
            result = self._values.get("read_capacity_auto_scaling_settings")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.CapacityAutoScalingSettingsProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def read_capacity_units(self) -> typing.Optional[jsii.Number]:
            '''``CfnGlobalTable.ReadProvisionedThroughputSettingsProperty.ReadCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityunits
            '''
            result = self._values.get("read_capacity_units")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReadProvisionedThroughputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "contributor_insights_specification": "contributorInsightsSpecification",
            "index_name": "indexName",
            "read_provisioned_throughput_settings": "readProvisionedThroughputSettings",
        },
    )
    class ReplicaGlobalSecondaryIndexSpecificationProperty:
        def __init__(
            self,
            *,
            contributor_insights_specification: typing.Optional[typing.Union["CfnGlobalTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]] = None,
            index_name: builtins.str,
            read_provisioned_throughput_settings: typing.Optional[typing.Union["CfnGlobalTable.ReadProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param contributor_insights_specification: ``CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty.ContributorInsightsSpecification``.
            :param index_name: ``CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty.IndexName``.
            :param read_provisioned_throughput_settings: ``CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty.ReadProvisionedThroughputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                replica_global_secondary_index_specification_property = dynamodb.CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty(
                    index_name="indexName",
                
                    # the properties below are optional
                    contributor_insights_specification=dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty(
                        enabled=False
                    ),
                    read_provisioned_throughput_settings=dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty(
                        read_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                            max_capacity=123,
                            min_capacity=123,
                            target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                                target_value=123,
                
                                # the properties below are optional
                                disable_scale_in=False,
                                scale_in_cooldown=123,
                                scale_out_cooldown=123
                            ),
                
                            # the properties below are optional
                            seed_capacity=123
                        ),
                        read_capacity_units=123
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "index_name": index_name,
            }
            if contributor_insights_specification is not None:
                self._values["contributor_insights_specification"] = contributor_insights_specification
            if read_provisioned_throughput_settings is not None:
                self._values["read_provisioned_throughput_settings"] = read_provisioned_throughput_settings

        @builtins.property
        def contributor_insights_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty.ContributorInsightsSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-contributorinsightsspecification
            '''
            result = self._values.get("contributor_insights_specification")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def index_name(self) -> builtins.str:
            '''``CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty.IndexName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def read_provisioned_throughput_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.ReadProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty.ReadProvisionedThroughputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readprovisionedthroughputsettings
            '''
            result = self._values.get("read_provisioned_throughput_settings")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.ReadProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicaGlobalSecondaryIndexSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.ReplicaSSESpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_master_key_id": "kmsMasterKeyId"},
    )
    class ReplicaSSESpecificationProperty:
        def __init__(self, *, kms_master_key_id: builtins.str) -> None:
            '''
            :param kms_master_key_id: ``CfnGlobalTable.ReplicaSSESpecificationProperty.KMSMasterKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                replica_sSESpecification_property = dynamodb.CfnGlobalTable.ReplicaSSESpecificationProperty(
                    kms_master_key_id="kmsMasterKeyId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "kms_master_key_id": kms_master_key_id,
            }

        @builtins.property
        def kms_master_key_id(self) -> builtins.str:
            '''``CfnGlobalTable.ReplicaSSESpecificationProperty.KMSMasterKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html#cfn-dynamodb-globaltable-replicassespecification-kmsmasterkeyid
            '''
            result = self._values.get("kms_master_key_id")
            assert result is not None, "Required property 'kms_master_key_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicaSSESpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.ReplicaSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "contributor_insights_specification": "contributorInsightsSpecification",
            "global_secondary_indexes": "globalSecondaryIndexes",
            "point_in_time_recovery_specification": "pointInTimeRecoverySpecification",
            "read_provisioned_throughput_settings": "readProvisionedThroughputSettings",
            "region": "region",
            "sse_specification": "sseSpecification",
            "tags": "tags",
        },
    )
    class ReplicaSpecificationProperty:
        def __init__(
            self,
            *,
            contributor_insights_specification: typing.Optional[typing.Union["CfnGlobalTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]] = None,
            global_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty", _IResolvable_a771d0ef]]]] = None,
            point_in_time_recovery_specification: typing.Optional[typing.Union["CfnGlobalTable.PointInTimeRecoverySpecificationProperty", _IResolvable_a771d0ef]] = None,
            read_provisioned_throughput_settings: typing.Optional[typing.Union["CfnGlobalTable.ReadProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]] = None,
            region: builtins.str,
            sse_specification: typing.Optional[typing.Union["CfnGlobalTable.ReplicaSSESpecificationProperty", _IResolvable_a771d0ef]] = None,
            tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        ) -> None:
            '''
            :param contributor_insights_specification: ``CfnGlobalTable.ReplicaSpecificationProperty.ContributorInsightsSpecification``.
            :param global_secondary_indexes: ``CfnGlobalTable.ReplicaSpecificationProperty.GlobalSecondaryIndexes``.
            :param point_in_time_recovery_specification: ``CfnGlobalTable.ReplicaSpecificationProperty.PointInTimeRecoverySpecification``.
            :param read_provisioned_throughput_settings: ``CfnGlobalTable.ReplicaSpecificationProperty.ReadProvisionedThroughputSettings``.
            :param region: ``CfnGlobalTable.ReplicaSpecificationProperty.Region``.
            :param sse_specification: ``CfnGlobalTable.ReplicaSpecificationProperty.SSESpecification``.
            :param tags: ``CfnGlobalTable.ReplicaSpecificationProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                replica_specification_property = dynamodb.CfnGlobalTable.ReplicaSpecificationProperty(
                    region="region",
                
                    # the properties below are optional
                    contributor_insights_specification=dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty(
                        enabled=False
                    ),
                    global_secondary_indexes=[dynamodb.CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty(
                        index_name="indexName",
                
                        # the properties below are optional
                        contributor_insights_specification=dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty(
                            enabled=False
                        ),
                        read_provisioned_throughput_settings=dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty(
                            read_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                                max_capacity=123,
                                min_capacity=123,
                                target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                                    target_value=123,
                
                                    # the properties below are optional
                                    disable_scale_in=False,
                                    scale_in_cooldown=123,
                                    scale_out_cooldown=123
                                ),
                
                                # the properties below are optional
                                seed_capacity=123
                            ),
                            read_capacity_units=123
                        )
                    )],
                    point_in_time_recovery_specification=dynamodb.CfnGlobalTable.PointInTimeRecoverySpecificationProperty(
                        point_in_time_recovery_enabled=False
                    ),
                    read_provisioned_throughput_settings=dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty(
                        read_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                            max_capacity=123,
                            min_capacity=123,
                            target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                                target_value=123,
                
                                # the properties below are optional
                                disable_scale_in=False,
                                scale_in_cooldown=123,
                                scale_out_cooldown=123
                            ),
                
                            # the properties below are optional
                            seed_capacity=123
                        ),
                        read_capacity_units=123
                    ),
                    sse_specification=dynamodb.CfnGlobalTable.ReplicaSSESpecificationProperty(
                        kms_master_key_id="kmsMasterKeyId"
                    ),
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "region": region,
            }
            if contributor_insights_specification is not None:
                self._values["contributor_insights_specification"] = contributor_insights_specification
            if global_secondary_indexes is not None:
                self._values["global_secondary_indexes"] = global_secondary_indexes
            if point_in_time_recovery_specification is not None:
                self._values["point_in_time_recovery_specification"] = point_in_time_recovery_specification
            if read_provisioned_throughput_settings is not None:
                self._values["read_provisioned_throughput_settings"] = read_provisioned_throughput_settings
            if sse_specification is not None:
                self._values["sse_specification"] = sse_specification
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def contributor_insights_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.ReplicaSpecificationProperty.ContributorInsightsSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-contributorinsightsspecification
            '''
            result = self._values.get("contributor_insights_specification")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def global_secondary_indexes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty", _IResolvable_a771d0ef]]]]:
            '''``CfnGlobalTable.ReplicaSpecificationProperty.GlobalSecondaryIndexes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-globalsecondaryindexes
            '''
            result = self._values.get("global_secondary_indexes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty", _IResolvable_a771d0ef]]]], result)

        @builtins.property
        def point_in_time_recovery_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.PointInTimeRecoverySpecificationProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.ReplicaSpecificationProperty.PointInTimeRecoverySpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-pointintimerecoveryspecification
            '''
            result = self._values.get("point_in_time_recovery_specification")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.PointInTimeRecoverySpecificationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def read_provisioned_throughput_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.ReadProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.ReplicaSpecificationProperty.ReadProvisionedThroughputSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-readprovisionedthroughputsettings
            '''
            result = self._values.get("read_provisioned_throughput_settings")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.ReadProvisionedThroughputSettingsProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def region(self) -> builtins.str:
            '''``CfnGlobalTable.ReplicaSpecificationProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sse_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.ReplicaSSESpecificationProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.ReplicaSpecificationProperty.SSESpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-ssespecification
            '''
            result = self._values.get("sse_specification")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.ReplicaSSESpecificationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
            '''``CfnGlobalTable.ReplicaSpecificationProperty.Tags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicaSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.SSESpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"sse_enabled": "sseEnabled", "sse_type": "sseType"},
    )
    class SSESpecificationProperty:
        def __init__(
            self,
            *,
            sse_enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
            sse_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param sse_enabled: ``CfnGlobalTable.SSESpecificationProperty.SSEEnabled``.
            :param sse_type: ``CfnGlobalTable.SSESpecificationProperty.SSEType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                s_sESpecification_property = dynamodb.CfnGlobalTable.SSESpecificationProperty(
                    sse_enabled=False,
                
                    # the properties below are optional
                    sse_type="sseType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "sse_enabled": sse_enabled,
            }
            if sse_type is not None:
                self._values["sse_type"] = sse_type

        @builtins.property
        def sse_enabled(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
            '''``CfnGlobalTable.SSESpecificationProperty.SSEEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-sseenabled
            '''
            result = self._values.get("sse_enabled")
            assert result is not None, "Required property 'sse_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], result)

        @builtins.property
        def sse_type(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalTable.SSESpecificationProperty.SSEType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-ssetype
            '''
            result = self._values.get("sse_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SSESpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.StreamSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"stream_view_type": "streamViewType"},
    )
    class StreamSpecificationProperty:
        def __init__(self, *, stream_view_type: builtins.str) -> None:
            '''
            :param stream_view_type: ``CfnGlobalTable.StreamSpecificationProperty.StreamViewType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                stream_specification_property = dynamodb.CfnGlobalTable.StreamSpecificationProperty(
                    stream_view_type="streamViewType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "stream_view_type": stream_view_type,
            }

        @builtins.property
        def stream_view_type(self) -> builtins.str:
            '''``CfnGlobalTable.StreamSpecificationProperty.StreamViewType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html#cfn-dynamodb-globaltable-streamspecification-streamviewtype
            '''
            result = self._values.get("stream_view_type")
            assert result is not None, "Required property 'stream_view_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "disable_scale_in": "disableScaleIn",
            "scale_in_cooldown": "scaleInCooldown",
            "scale_out_cooldown": "scaleOutCooldown",
            "target_value": "targetValue",
        },
    )
    class TargetTrackingScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            disable_scale_in: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            scale_in_cooldown: typing.Optional[jsii.Number] = None,
            scale_out_cooldown: typing.Optional[jsii.Number] = None,
            target_value: jsii.Number,
        ) -> None:
            '''
            :param disable_scale_in: ``CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty.DisableScaleIn``.
            :param scale_in_cooldown: ``CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty.ScaleInCooldown``.
            :param scale_out_cooldown: ``CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty.ScaleOutCooldown``.
            :param target_value: ``CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty.TargetValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                target_tracking_scaling_policy_configuration_property = dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                    target_value=123,
                
                    # the properties below are optional
                    disable_scale_in=False,
                    scale_in_cooldown=123,
                    scale_out_cooldown=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "target_value": target_value,
            }
            if disable_scale_in is not None:
                self._values["disable_scale_in"] = disable_scale_in
            if scale_in_cooldown is not None:
                self._values["scale_in_cooldown"] = scale_in_cooldown
            if scale_out_cooldown is not None:
                self._values["scale_out_cooldown"] = scale_out_cooldown

        @builtins.property
        def disable_scale_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty.DisableScaleIn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-disablescalein
            '''
            result = self._values.get("disable_scale_in")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
            '''``CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty.ScaleInCooldown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleincooldown
            '''
            result = self._values.get("scale_in_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
            '''``CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty.ScaleOutCooldown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleoutcooldown
            '''
            result = self._values.get("scale_out_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''``CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty.TargetValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.TimeToLiveSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_name": "attributeName", "enabled": "enabled"},
    )
    class TimeToLiveSpecificationProperty:
        def __init__(
            self,
            *,
            attribute_name: typing.Optional[builtins.str] = None,
            enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param attribute_name: ``CfnGlobalTable.TimeToLiveSpecificationProperty.AttributeName``.
            :param enabled: ``CfnGlobalTable.TimeToLiveSpecificationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                time_to_live_specification_property = dynamodb.CfnGlobalTable.TimeToLiveSpecificationProperty(
                    enabled=False,
                
                    # the properties below are optional
                    attribute_name="attributeName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }
            if attribute_name is not None:
                self._values["attribute_name"] = attribute_name

        @builtins.property
        def attribute_name(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalTable.TimeToLiveSpecificationProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html#cfn-dynamodb-globaltable-timetolivespecification-attributename
            '''
            result = self._values.get("attribute_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
            '''``CfnGlobalTable.TimeToLiveSpecificationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html#cfn-dynamodb-globaltable-timetolivespecification-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeToLiveSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnGlobalTable.WriteProvisionedThroughputSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "write_capacity_auto_scaling_settings": "writeCapacityAutoScalingSettings",
        },
    )
    class WriteProvisionedThroughputSettingsProperty:
        def __init__(
            self,
            *,
            write_capacity_auto_scaling_settings: typing.Optional[typing.Union["CfnGlobalTable.CapacityAutoScalingSettingsProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param write_capacity_auto_scaling_settings: ``CfnGlobalTable.WriteProvisionedThroughputSettingsProperty.WriteCapacityAutoScalingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                write_provisioned_throughput_settings_property = dynamodb.CfnGlobalTable.WriteProvisionedThroughputSettingsProperty(
                    write_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                        max_capacity=123,
                        min_capacity=123,
                        target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                            target_value=123,
                
                            # the properties below are optional
                            disable_scale_in=False,
                            scale_in_cooldown=123,
                            scale_out_cooldown=123
                        ),
                
                        # the properties below are optional
                        seed_capacity=123
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if write_capacity_auto_scaling_settings is not None:
                self._values["write_capacity_auto_scaling_settings"] = write_capacity_auto_scaling_settings

        @builtins.property
        def write_capacity_auto_scaling_settings(
            self,
        ) -> typing.Optional[typing.Union["CfnGlobalTable.CapacityAutoScalingSettingsProperty", _IResolvable_a771d0ef]]:
            '''``CfnGlobalTable.WriteProvisionedThroughputSettingsProperty.WriteCapacityAutoScalingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings-writecapacityautoscalingsettings
            '''
            result = self._values.get("write_capacity_auto_scaling_settings")
            return typing.cast(typing.Optional[typing.Union["CfnGlobalTable.CapacityAutoScalingSettingsProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WriteProvisionedThroughputSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.CfnGlobalTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_definitions": "attributeDefinitions",
        "billing_mode": "billingMode",
        "global_secondary_indexes": "globalSecondaryIndexes",
        "key_schema": "keySchema",
        "local_secondary_indexes": "localSecondaryIndexes",
        "replicas": "replicas",
        "sse_specification": "sseSpecification",
        "stream_specification": "streamSpecification",
        "table_name": "tableName",
        "time_to_live_specification": "timeToLiveSpecification",
        "write_provisioned_throughput_settings": "writeProvisionedThroughputSettings",
    },
)
class CfnGlobalTableProps:
    def __init__(
        self,
        *,
        attribute_definitions: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnGlobalTable.AttributeDefinitionProperty, _IResolvable_a771d0ef]]],
        billing_mode: typing.Optional[builtins.str] = None,
        global_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnGlobalTable.GlobalSecondaryIndexProperty, _IResolvable_a771d0ef]]]] = None,
        key_schema: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnGlobalTable.KeySchemaProperty, _IResolvable_a771d0ef]]],
        local_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnGlobalTable.LocalSecondaryIndexProperty, _IResolvable_a771d0ef]]]] = None,
        replicas: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnGlobalTable.ReplicaSpecificationProperty, _IResolvable_a771d0ef]]],
        sse_specification: typing.Optional[typing.Union[CfnGlobalTable.SSESpecificationProperty, _IResolvable_a771d0ef]] = None,
        stream_specification: typing.Optional[typing.Union[CfnGlobalTable.StreamSpecificationProperty, _IResolvable_a771d0ef]] = None,
        table_name: typing.Optional[builtins.str] = None,
        time_to_live_specification: typing.Optional[typing.Union[CfnGlobalTable.TimeToLiveSpecificationProperty, _IResolvable_a771d0ef]] = None,
        write_provisioned_throughput_settings: typing.Optional[typing.Union[CfnGlobalTable.WriteProvisionedThroughputSettingsProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DynamoDB::GlobalTable``.

        :param attribute_definitions: ``AWS::DynamoDB::GlobalTable.AttributeDefinitions``.
        :param billing_mode: ``AWS::DynamoDB::GlobalTable.BillingMode``.
        :param global_secondary_indexes: ``AWS::DynamoDB::GlobalTable.GlobalSecondaryIndexes``.
        :param key_schema: ``AWS::DynamoDB::GlobalTable.KeySchema``.
        :param local_secondary_indexes: ``AWS::DynamoDB::GlobalTable.LocalSecondaryIndexes``.
        :param replicas: ``AWS::DynamoDB::GlobalTable.Replicas``.
        :param sse_specification: ``AWS::DynamoDB::GlobalTable.SSESpecification``.
        :param stream_specification: ``AWS::DynamoDB::GlobalTable.StreamSpecification``.
        :param table_name: ``AWS::DynamoDB::GlobalTable.TableName``.
        :param time_to_live_specification: ``AWS::DynamoDB::GlobalTable.TimeToLiveSpecification``.
        :param write_provisioned_throughput_settings: ``AWS::DynamoDB::GlobalTable.WriteProvisionedThroughputSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dynamodb as dynamodb
            
            cfn_global_table_props = dynamodb.CfnGlobalTableProps(
                attribute_definitions=[dynamodb.CfnGlobalTable.AttributeDefinitionProperty(
                    attribute_name="attributeName",
                    attribute_type="attributeType"
                )],
                key_schema=[dynamodb.CfnGlobalTable.KeySchemaProperty(
                    attribute_name="attributeName",
                    key_type="keyType"
                )],
                replicas=[dynamodb.CfnGlobalTable.ReplicaSpecificationProperty(
                    region="region",
            
                    # the properties below are optional
                    contributor_insights_specification=dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty(
                        enabled=False
                    ),
                    global_secondary_indexes=[dynamodb.CfnGlobalTable.ReplicaGlobalSecondaryIndexSpecificationProperty(
                        index_name="indexName",
            
                        # the properties below are optional
                        contributor_insights_specification=dynamodb.CfnGlobalTable.ContributorInsightsSpecificationProperty(
                            enabled=False
                        ),
                        read_provisioned_throughput_settings=dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty(
                            read_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                                max_capacity=123,
                                min_capacity=123,
                                target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                                    target_value=123,
            
                                    # the properties below are optional
                                    disable_scale_in=False,
                                    scale_in_cooldown=123,
                                    scale_out_cooldown=123
                                ),
            
                                # the properties below are optional
                                seed_capacity=123
                            ),
                            read_capacity_units=123
                        )
                    )],
                    point_in_time_recovery_specification=dynamodb.CfnGlobalTable.PointInTimeRecoverySpecificationProperty(
                        point_in_time_recovery_enabled=False
                    ),
                    read_provisioned_throughput_settings=dynamodb.CfnGlobalTable.ReadProvisionedThroughputSettingsProperty(
                        read_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                            max_capacity=123,
                            min_capacity=123,
                            target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                                target_value=123,
            
                                # the properties below are optional
                                disable_scale_in=False,
                                scale_in_cooldown=123,
                                scale_out_cooldown=123
                            ),
            
                            # the properties below are optional
                            seed_capacity=123
                        ),
                        read_capacity_units=123
                    ),
                    sse_specification=dynamodb.CfnGlobalTable.ReplicaSSESpecificationProperty(
                        kms_master_key_id="kmsMasterKeyId"
                    ),
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
            
                # the properties below are optional
                billing_mode="billingMode",
                global_secondary_indexes=[dynamodb.CfnGlobalTable.GlobalSecondaryIndexProperty(
                    index_name="indexName",
                    key_schema=[dynamodb.CfnGlobalTable.KeySchemaProperty(
                        attribute_name="attributeName",
                        key_type="keyType"
                    )],
                    projection=dynamodb.CfnGlobalTable.ProjectionProperty(
                        non_key_attributes=["nonKeyAttributes"],
                        projection_type="projectionType"
                    ),
            
                    # the properties below are optional
                    write_provisioned_throughput_settings=dynamodb.CfnGlobalTable.WriteProvisionedThroughputSettingsProperty(
                        write_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                            max_capacity=123,
                            min_capacity=123,
                            target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                                target_value=123,
            
                                # the properties below are optional
                                disable_scale_in=False,
                                scale_in_cooldown=123,
                                scale_out_cooldown=123
                            ),
            
                            # the properties below are optional
                            seed_capacity=123
                        )
                    )
                )],
                local_secondary_indexes=[dynamodb.CfnGlobalTable.LocalSecondaryIndexProperty(
                    index_name="indexName",
                    key_schema=[dynamodb.CfnGlobalTable.KeySchemaProperty(
                        attribute_name="attributeName",
                        key_type="keyType"
                    )],
                    projection=dynamodb.CfnGlobalTable.ProjectionProperty(
                        non_key_attributes=["nonKeyAttributes"],
                        projection_type="projectionType"
                    )
                )],
                sse_specification=dynamodb.CfnGlobalTable.SSESpecificationProperty(
                    sse_enabled=False,
            
                    # the properties below are optional
                    sse_type="sseType"
                ),
                stream_specification=dynamodb.CfnGlobalTable.StreamSpecificationProperty(
                    stream_view_type="streamViewType"
                ),
                table_name="tableName",
                time_to_live_specification=dynamodb.CfnGlobalTable.TimeToLiveSpecificationProperty(
                    enabled=False,
            
                    # the properties below are optional
                    attribute_name="attributeName"
                ),
                write_provisioned_throughput_settings=dynamodb.CfnGlobalTable.WriteProvisionedThroughputSettingsProperty(
                    write_capacity_auto_scaling_settings=dynamodb.CfnGlobalTable.CapacityAutoScalingSettingsProperty(
                        max_capacity=123,
                        min_capacity=123,
                        target_tracking_scaling_policy_configuration=dynamodb.CfnGlobalTable.TargetTrackingScalingPolicyConfigurationProperty(
                            target_value=123,
            
                            # the properties below are optional
                            disable_scale_in=False,
                            scale_in_cooldown=123,
                            scale_out_cooldown=123
                        ),
            
                        # the properties below are optional
                        seed_capacity=123
                    )
                )
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "attribute_definitions": attribute_definitions,
            "key_schema": key_schema,
            "replicas": replicas,
        }
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if global_secondary_indexes is not None:
            self._values["global_secondary_indexes"] = global_secondary_indexes
        if local_secondary_indexes is not None:
            self._values["local_secondary_indexes"] = local_secondary_indexes
        if sse_specification is not None:
            self._values["sse_specification"] = sse_specification
        if stream_specification is not None:
            self._values["stream_specification"] = stream_specification
        if table_name is not None:
            self._values["table_name"] = table_name
        if time_to_live_specification is not None:
            self._values["time_to_live_specification"] = time_to_live_specification
        if write_provisioned_throughput_settings is not None:
            self._values["write_provisioned_throughput_settings"] = write_provisioned_throughput_settings

    @builtins.property
    def attribute_definitions(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.AttributeDefinitionProperty, _IResolvable_a771d0ef]]]:
        '''``AWS::DynamoDB::GlobalTable.AttributeDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-attributedefinitions
        '''
        result = self._values.get("attribute_definitions")
        assert result is not None, "Required property 'attribute_definitions' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.AttributeDefinitionProperty, _IResolvable_a771d0ef]]], result)

    @builtins.property
    def billing_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::GlobalTable.BillingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-billingmode
        '''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_secondary_indexes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.GlobalSecondaryIndexProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::GlobalTable.GlobalSecondaryIndexes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-globalsecondaryindexes
        '''
        result = self._values.get("global_secondary_indexes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.GlobalSecondaryIndexProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def key_schema(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.KeySchemaProperty, _IResolvable_a771d0ef]]]:
        '''``AWS::DynamoDB::GlobalTable.KeySchema``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-keyschema
        '''
        result = self._values.get("key_schema")
        assert result is not None, "Required property 'key_schema' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.KeySchemaProperty, _IResolvable_a771d0ef]]], result)

    @builtins.property
    def local_secondary_indexes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.LocalSecondaryIndexProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::GlobalTable.LocalSecondaryIndexes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-localsecondaryindexes
        '''
        result = self._values.get("local_secondary_indexes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.LocalSecondaryIndexProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def replicas(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.ReplicaSpecificationProperty, _IResolvable_a771d0ef]]]:
        '''``AWS::DynamoDB::GlobalTable.Replicas``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-replicas
        '''
        result = self._values.get("replicas")
        assert result is not None, "Required property 'replicas' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGlobalTable.ReplicaSpecificationProperty, _IResolvable_a771d0ef]]], result)

    @builtins.property
    def sse_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnGlobalTable.SSESpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::GlobalTable.SSESpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-ssespecification
        '''
        result = self._values.get("sse_specification")
        return typing.cast(typing.Optional[typing.Union[CfnGlobalTable.SSESpecificationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def stream_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnGlobalTable.StreamSpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::GlobalTable.StreamSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-streamspecification
        '''
        result = self._values.get("stream_specification")
        return typing.cast(typing.Optional[typing.Union[CfnGlobalTable.StreamSpecificationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::GlobalTable.TableName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-tablename
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_to_live_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnGlobalTable.TimeToLiveSpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::GlobalTable.TimeToLiveSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-timetolivespecification
        '''
        result = self._values.get("time_to_live_specification")
        return typing.cast(typing.Optional[typing.Union[CfnGlobalTable.TimeToLiveSpecificationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def write_provisioned_throughput_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnGlobalTable.WriteProvisionedThroughputSettingsProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::GlobalTable.WriteProvisionedThroughputSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings
        '''
        result = self._values.get("write_provisioned_throughput_settings")
        return typing.cast(typing.Optional[typing.Union[CfnGlobalTable.WriteProvisionedThroughputSettingsProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGlobalTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnTable(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dynamodb.CfnTable",
):
    '''A CloudFormation ``AWS::DynamoDB::Table``.

    :cloudformationResource: AWS::DynamoDB::Table
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_dynamodb as dynamodb
        
        cfn_table = dynamodb.CfnTable(self, "MyCfnTable",
            key_schema=[dynamodb.CfnTable.KeySchemaProperty(
                attribute_name="attributeName",
                key_type="keyType"
            )],
        
            # the properties below are optional
            attribute_definitions=[dynamodb.CfnTable.AttributeDefinitionProperty(
                attribute_name="attributeName",
                attribute_type="attributeType"
            )],
            billing_mode="billingMode",
            contributor_insights_specification=dynamodb.CfnTable.ContributorInsightsSpecificationProperty(
                enabled=False
            ),
            global_secondary_indexes=[dynamodb.CfnTable.GlobalSecondaryIndexProperty(
                index_name="indexName",
                key_schema=[dynamodb.CfnTable.KeySchemaProperty(
                    attribute_name="attributeName",
                    key_type="keyType"
                )],
                projection=dynamodb.CfnTable.ProjectionProperty(
                    non_key_attributes=["nonKeyAttributes"],
                    projection_type="projectionType"
                ),
        
                # the properties below are optional
                contributor_insights_specification=dynamodb.CfnTable.ContributorInsightsSpecificationProperty(
                    enabled=False
                ),
                provisioned_throughput=dynamodb.CfnTable.ProvisionedThroughputProperty(
                    read_capacity_units=123,
                    write_capacity_units=123
                )
            )],
            kinesis_stream_specification=dynamodb.CfnTable.KinesisStreamSpecificationProperty(
                stream_arn="streamArn"
            ),
            local_secondary_indexes=[dynamodb.CfnTable.LocalSecondaryIndexProperty(
                index_name="indexName",
                key_schema=[dynamodb.CfnTable.KeySchemaProperty(
                    attribute_name="attributeName",
                    key_type="keyType"
                )],
                projection=dynamodb.CfnTable.ProjectionProperty(
                    non_key_attributes=["nonKeyAttributes"],
                    projection_type="projectionType"
                )
            )],
            point_in_time_recovery_specification=dynamodb.CfnTable.PointInTimeRecoverySpecificationProperty(
                point_in_time_recovery_enabled=False
            ),
            provisioned_throughput=dynamodb.CfnTable.ProvisionedThroughputProperty(
                read_capacity_units=123,
                write_capacity_units=123
            ),
            sse_specification=dynamodb.CfnTable.SSESpecificationProperty(
                sse_enabled=False,
        
                # the properties below are optional
                kms_master_key_id="kmsMasterKeyId",
                sse_type="sseType"
            ),
            stream_specification=dynamodb.CfnTable.StreamSpecificationProperty(
                stream_view_type="streamViewType"
            ),
            table_class="tableClass",
            table_name="tableName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            time_to_live_specification=dynamodb.CfnTable.TimeToLiveSpecificationProperty(
                attribute_name="attributeName",
                enabled=False
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        attribute_definitions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnTable.AttributeDefinitionProperty", _IResolvable_a771d0ef]]]] = None,
        billing_mode: typing.Optional[builtins.str] = None,
        contributor_insights_specification: typing.Optional[typing.Union["CfnTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]] = None,
        global_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnTable.GlobalSecondaryIndexProperty", _IResolvable_a771d0ef]]]] = None,
        key_schema: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]],
        kinesis_stream_specification: typing.Optional[typing.Union["CfnTable.KinesisStreamSpecificationProperty", _IResolvable_a771d0ef]] = None,
        local_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnTable.LocalSecondaryIndexProperty", _IResolvable_a771d0ef]]]] = None,
        point_in_time_recovery_specification: typing.Optional[typing.Union["CfnTable.PointInTimeRecoverySpecificationProperty", _IResolvable_a771d0ef]] = None,
        provisioned_throughput: typing.Optional[typing.Union["CfnTable.ProvisionedThroughputProperty", _IResolvable_a771d0ef]] = None,
        sse_specification: typing.Optional[typing.Union["CfnTable.SSESpecificationProperty", _IResolvable_a771d0ef]] = None,
        stream_specification: typing.Optional[typing.Union["CfnTable.StreamSpecificationProperty", _IResolvable_a771d0ef]] = None,
        table_class: typing.Optional[builtins.str] = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        time_to_live_specification: typing.Optional[typing.Union["CfnTable.TimeToLiveSpecificationProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::DynamoDB::Table``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param attribute_definitions: ``AWS::DynamoDB::Table.AttributeDefinitions``.
        :param billing_mode: ``AWS::DynamoDB::Table.BillingMode``.
        :param contributor_insights_specification: ``AWS::DynamoDB::Table.ContributorInsightsSpecification``.
        :param global_secondary_indexes: ``AWS::DynamoDB::Table.GlobalSecondaryIndexes``.
        :param key_schema: ``AWS::DynamoDB::Table.KeySchema``.
        :param kinesis_stream_specification: ``AWS::DynamoDB::Table.KinesisStreamSpecification``.
        :param local_secondary_indexes: ``AWS::DynamoDB::Table.LocalSecondaryIndexes``.
        :param point_in_time_recovery_specification: ``AWS::DynamoDB::Table.PointInTimeRecoverySpecification``.
        :param provisioned_throughput: ``AWS::DynamoDB::Table.ProvisionedThroughput``.
        :param sse_specification: ``AWS::DynamoDB::Table.SSESpecification``.
        :param stream_specification: ``AWS::DynamoDB::Table.StreamSpecification``.
        :param table_class: ``AWS::DynamoDB::Table.TableClass``.
        :param table_name: ``AWS::DynamoDB::Table.TableName``.
        :param tags: ``AWS::DynamoDB::Table.Tags``.
        :param time_to_live_specification: ``AWS::DynamoDB::Table.TimeToLiveSpecification``.
        '''
        props = CfnTableProps(
            attribute_definitions=attribute_definitions,
            billing_mode=billing_mode,
            contributor_insights_specification=contributor_insights_specification,
            global_secondary_indexes=global_secondary_indexes,
            key_schema=key_schema,
            kinesis_stream_specification=kinesis_stream_specification,
            local_secondary_indexes=local_secondary_indexes,
            point_in_time_recovery_specification=point_in_time_recovery_specification,
            provisioned_throughput=provisioned_throughput,
            sse_specification=sse_specification,
            stream_specification=stream_specification,
            table_class=table_class,
            table_name=table_name,
            tags=tags,
            time_to_live_specification=time_to_live_specification,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
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
    @jsii.member(jsii_name="attributeDefinitions")
    def attribute_definitions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.AttributeDefinitionProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::Table.AttributeDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedef
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.AttributeDefinitionProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "attributeDefinitions"))

    @attribute_definitions.setter
    def attribute_definitions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.AttributeDefinitionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "attributeDefinitions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStreamArn")
    def attr_stream_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: StreamArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStreamArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="billingMode")
    def billing_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::Table.BillingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-billingmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingMode"))

    @billing_mode.setter
    def billing_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "billingMode", value)

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
    @jsii.member(jsii_name="contributorInsightsSpecification")
    def contributor_insights_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.ContributorInsightsSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-contributorinsightsspecification-enabled
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "contributorInsightsSpecification"))

    @contributor_insights_specification.setter
    def contributor_insights_specification(
        self,
        value: typing.Optional[typing.Union["CfnTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "contributorInsightsSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalSecondaryIndexes")
    def global_secondary_indexes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.GlobalSecondaryIndexProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::Table.GlobalSecondaryIndexes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-gsi
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.GlobalSecondaryIndexProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "globalSecondaryIndexes"))

    @global_secondary_indexes.setter
    def global_secondary_indexes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.GlobalSecondaryIndexProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "globalSecondaryIndexes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keySchema")
    def key_schema(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]]:
        '''``AWS::DynamoDB::Table.KeySchema``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]], jsii.get(self, "keySchema"))

    @key_schema.setter
    def key_schema(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        jsii.set(self, "keySchema", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kinesisStreamSpecification")
    def kinesis_stream_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnTable.KinesisStreamSpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.KinesisStreamSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-kinesisstreamspecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTable.KinesisStreamSpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "kinesisStreamSpecification"))

    @kinesis_stream_specification.setter
    def kinesis_stream_specification(
        self,
        value: typing.Optional[typing.Union["CfnTable.KinesisStreamSpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "kinesisStreamSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="localSecondaryIndexes")
    def local_secondary_indexes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.LocalSecondaryIndexProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::Table.LocalSecondaryIndexes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-lsi
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.LocalSecondaryIndexProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "localSecondaryIndexes"))

    @local_secondary_indexes.setter
    def local_secondary_indexes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.LocalSecondaryIndexProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "localSecondaryIndexes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pointInTimeRecoverySpecification")
    def point_in_time_recovery_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnTable.PointInTimeRecoverySpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.PointInTimeRecoverySpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-pointintimerecoveryspecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTable.PointInTimeRecoverySpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "pointInTimeRecoverySpecification"))

    @point_in_time_recovery_specification.setter
    def point_in_time_recovery_specification(
        self,
        value: typing.Optional[typing.Union["CfnTable.PointInTimeRecoverySpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "pointInTimeRecoverySpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="provisionedThroughput")
    def provisioned_throughput(
        self,
    ) -> typing.Optional[typing.Union["CfnTable.ProvisionedThroughputProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.ProvisionedThroughput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTable.ProvisionedThroughputProperty", _IResolvable_a771d0ef]], jsii.get(self, "provisionedThroughput"))

    @provisioned_throughput.setter
    def provisioned_throughput(
        self,
        value: typing.Optional[typing.Union["CfnTable.ProvisionedThroughputProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "provisionedThroughput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sseSpecification")
    def sse_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnTable.SSESpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.SSESpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-ssespecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTable.SSESpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "sseSpecification"))

    @sse_specification.setter
    def sse_specification(
        self,
        value: typing.Optional[typing.Union["CfnTable.SSESpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "sseSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="streamSpecification")
    def stream_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnTable.StreamSpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.StreamSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTable.StreamSpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "streamSpecification"))

    @stream_specification.setter
    def stream_specification(
        self,
        value: typing.Optional[typing.Union["CfnTable.StreamSpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "streamSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableClass")
    def table_class(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::Table.TableClass``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tableclass
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableClass"))

    @table_class.setter
    def table_class(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tableClass", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::Table.TableName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tableName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::DynamoDB::Table.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeToLiveSpecification")
    def time_to_live_specification(
        self,
    ) -> typing.Optional[typing.Union["CfnTable.TimeToLiveSpecificationProperty", _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.TimeToLiveSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-timetolivespecification
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTable.TimeToLiveSpecificationProperty", _IResolvable_a771d0ef]], jsii.get(self, "timeToLiveSpecification"))

    @time_to_live_specification.setter
    def time_to_live_specification(
        self,
        value: typing.Optional[typing.Union["CfnTable.TimeToLiveSpecificationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "timeToLiveSpecification", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.AttributeDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_name": "attributeName",
            "attribute_type": "attributeType",
        },
    )
    class AttributeDefinitionProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            attribute_type: builtins.str,
        ) -> None:
            '''
            :param attribute_name: ``CfnTable.AttributeDefinitionProperty.AttributeName``.
            :param attribute_type: ``CfnTable.AttributeDefinitionProperty.AttributeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                attribute_definition_property = dynamodb.CfnTable.AttributeDefinitionProperty(
                    attribute_name="attributeName",
                    attribute_type="attributeType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attribute_name": attribute_name,
                "attribute_type": attribute_type,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''``CfnTable.AttributeDefinitionProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute_type(self) -> builtins.str:
            '''``CfnTable.AttributeDefinitionProperty.AttributeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename-attributetype
            '''
            result = self._values.get("attribute_type")
            assert result is not None, "Required property 'attribute_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.ContributorInsightsSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class ContributorInsightsSpecificationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param enabled: ``CfnTable.ContributorInsightsSpecificationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-contributorinsightsspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                contributor_insights_specification_property = dynamodb.CfnTable.ContributorInsightsSpecificationProperty(
                    enabled=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
            '''``CfnTable.ContributorInsightsSpecificationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-contributorinsightsspecification.html#cfn-dynamodb-contributorinsightsspecification-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContributorInsightsSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.GlobalSecondaryIndexProperty",
        jsii_struct_bases=[],
        name_mapping={
            "contributor_insights_specification": "contributorInsightsSpecification",
            "index_name": "indexName",
            "key_schema": "keySchema",
            "projection": "projection",
            "provisioned_throughput": "provisionedThroughput",
        },
    )
    class GlobalSecondaryIndexProperty:
        def __init__(
            self,
            *,
            contributor_insights_specification: typing.Optional[typing.Union["CfnTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]] = None,
            index_name: builtins.str,
            key_schema: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]],
            projection: typing.Union["CfnTable.ProjectionProperty", _IResolvable_a771d0ef],
            provisioned_throughput: typing.Optional[typing.Union["CfnTable.ProvisionedThroughputProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param contributor_insights_specification: ``CfnTable.GlobalSecondaryIndexProperty.ContributorInsightsSpecification``.
            :param index_name: ``CfnTable.GlobalSecondaryIndexProperty.IndexName``.
            :param key_schema: ``CfnTable.GlobalSecondaryIndexProperty.KeySchema``.
            :param projection: ``CfnTable.GlobalSecondaryIndexProperty.Projection``.
            :param provisioned_throughput: ``CfnTable.GlobalSecondaryIndexProperty.ProvisionedThroughput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                global_secondary_index_property = dynamodb.CfnTable.GlobalSecondaryIndexProperty(
                    index_name="indexName",
                    key_schema=[dynamodb.CfnTable.KeySchemaProperty(
                        attribute_name="attributeName",
                        key_type="keyType"
                    )],
                    projection=dynamodb.CfnTable.ProjectionProperty(
                        non_key_attributes=["nonKeyAttributes"],
                        projection_type="projectionType"
                    ),
                
                    # the properties below are optional
                    contributor_insights_specification=dynamodb.CfnTable.ContributorInsightsSpecificationProperty(
                        enabled=False
                    ),
                    provisioned_throughput=dynamodb.CfnTable.ProvisionedThroughputProperty(
                        read_capacity_units=123,
                        write_capacity_units=123
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "index_name": index_name,
                "key_schema": key_schema,
                "projection": projection,
            }
            if contributor_insights_specification is not None:
                self._values["contributor_insights_specification"] = contributor_insights_specification
            if provisioned_throughput is not None:
                self._values["provisioned_throughput"] = provisioned_throughput

        @builtins.property
        def contributor_insights_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]]:
            '''``CfnTable.GlobalSecondaryIndexProperty.ContributorInsightsSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-contributorinsightsspecification-enabled
            '''
            result = self._values.get("contributor_insights_specification")
            return typing.cast(typing.Optional[typing.Union["CfnTable.ContributorInsightsSpecificationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def index_name(self) -> builtins.str:
            '''``CfnTable.GlobalSecondaryIndexProperty.IndexName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_schema(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]]:
            '''``CfnTable.GlobalSecondaryIndexProperty.KeySchema``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-keyschema
            '''
            result = self._values.get("key_schema")
            assert result is not None, "Required property 'key_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def projection(
            self,
        ) -> typing.Union["CfnTable.ProjectionProperty", _IResolvable_a771d0ef]:
            '''``CfnTable.GlobalSecondaryIndexProperty.Projection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-projection
            '''
            result = self._values.get("projection")
            assert result is not None, "Required property 'projection' is missing"
            return typing.cast(typing.Union["CfnTable.ProjectionProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def provisioned_throughput(
            self,
        ) -> typing.Optional[typing.Union["CfnTable.ProvisionedThroughputProperty", _IResolvable_a771d0ef]]:
            '''``CfnTable.GlobalSecondaryIndexProperty.ProvisionedThroughput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-provisionedthroughput
            '''
            result = self._values.get("provisioned_throughput")
            return typing.cast(typing.Optional[typing.Union["CfnTable.ProvisionedThroughputProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlobalSecondaryIndexProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.KeySchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_name": "attributeName", "key_type": "keyType"},
    )
    class KeySchemaProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            key_type: builtins.str,
        ) -> None:
            '''
            :param attribute_name: ``CfnTable.KeySchemaProperty.AttributeName``.
            :param key_type: ``CfnTable.KeySchemaProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                key_schema_property = dynamodb.CfnTable.KeySchemaProperty(
                    attribute_name="attributeName",
                    key_type="keyType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attribute_name": attribute_name,
                "key_type": key_type,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''``CfnTable.KeySchemaProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_type(self) -> builtins.str:
            '''``CfnTable.KeySchemaProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-keytype
            '''
            result = self._values.get("key_type")
            assert result is not None, "Required property 'key_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeySchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.KinesisStreamSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"stream_arn": "streamArn"},
    )
    class KinesisStreamSpecificationProperty:
        def __init__(self, *, stream_arn: builtins.str) -> None:
            '''
            :param stream_arn: ``CfnTable.KinesisStreamSpecificationProperty.StreamArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-kinesisstreamspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                kinesis_stream_specification_property = dynamodb.CfnTable.KinesisStreamSpecificationProperty(
                    stream_arn="streamArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "stream_arn": stream_arn,
            }

        @builtins.property
        def stream_arn(self) -> builtins.str:
            '''``CfnTable.KinesisStreamSpecificationProperty.StreamArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-kinesisstreamspecification.html#cfn-dynamodb-kinesisstreamspecification-streamarn
            '''
            result = self._values.get("stream_arn")
            assert result is not None, "Required property 'stream_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.LocalSecondaryIndexProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "key_schema": "keySchema",
            "projection": "projection",
        },
    )
    class LocalSecondaryIndexProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            key_schema: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]],
            projection: typing.Union["CfnTable.ProjectionProperty", _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param index_name: ``CfnTable.LocalSecondaryIndexProperty.IndexName``.
            :param key_schema: ``CfnTable.LocalSecondaryIndexProperty.KeySchema``.
            :param projection: ``CfnTable.LocalSecondaryIndexProperty.Projection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                local_secondary_index_property = dynamodb.CfnTable.LocalSecondaryIndexProperty(
                    index_name="indexName",
                    key_schema=[dynamodb.CfnTable.KeySchemaProperty(
                        attribute_name="attributeName",
                        key_type="keyType"
                    )],
                    projection=dynamodb.CfnTable.ProjectionProperty(
                        non_key_attributes=["nonKeyAttributes"],
                        projection_type="projectionType"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "index_name": index_name,
                "key_schema": key_schema,
                "projection": projection,
            }

        @builtins.property
        def index_name(self) -> builtins.str:
            '''``CfnTable.LocalSecondaryIndexProperty.IndexName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_schema(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]]:
            '''``CfnTable.LocalSecondaryIndexProperty.KeySchema``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-keyschema
            '''
            result = self._values.get("key_schema")
            assert result is not None, "Required property 'key_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTable.KeySchemaProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def projection(
            self,
        ) -> typing.Union["CfnTable.ProjectionProperty", _IResolvable_a771d0ef]:
            '''``CfnTable.LocalSecondaryIndexProperty.Projection``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-projection
            '''
            result = self._values.get("projection")
            assert result is not None, "Required property 'projection' is missing"
            return typing.cast(typing.Union["CfnTable.ProjectionProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalSecondaryIndexProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.PointInTimeRecoverySpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"point_in_time_recovery_enabled": "pointInTimeRecoveryEnabled"},
    )
    class PointInTimeRecoverySpecificationProperty:
        def __init__(
            self,
            *,
            point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param point_in_time_recovery_enabled: ``CfnTable.PointInTimeRecoverySpecificationProperty.PointInTimeRecoveryEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                point_in_time_recovery_specification_property = dynamodb.CfnTable.PointInTimeRecoverySpecificationProperty(
                    point_in_time_recovery_enabled=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if point_in_time_recovery_enabled is not None:
                self._values["point_in_time_recovery_enabled"] = point_in_time_recovery_enabled

        @builtins.property
        def point_in_time_recovery_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''``CfnTable.PointInTimeRecoverySpecificationProperty.PointInTimeRecoveryEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html#cfn-dynamodb-table-pointintimerecoveryspecification-pointintimerecoveryenabled
            '''
            result = self._values.get("point_in_time_recovery_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PointInTimeRecoverySpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.ProjectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "non_key_attributes": "nonKeyAttributes",
            "projection_type": "projectionType",
        },
    )
    class ProjectionProperty:
        def __init__(
            self,
            *,
            non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
            projection_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param non_key_attributes: ``CfnTable.ProjectionProperty.NonKeyAttributes``.
            :param projection_type: ``CfnTable.ProjectionProperty.ProjectionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                projection_property = dynamodb.CfnTable.ProjectionProperty(
                    non_key_attributes=["nonKeyAttributes"],
                    projection_type="projectionType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if non_key_attributes is not None:
                self._values["non_key_attributes"] = non_key_attributes
            if projection_type is not None:
                self._values["projection_type"] = projection_type

        @builtins.property
        def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnTable.ProjectionProperty.NonKeyAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-nonkeyatt
            '''
            result = self._values.get("non_key_attributes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def projection_type(self) -> typing.Optional[builtins.str]:
            '''``CfnTable.ProjectionProperty.ProjectionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-projtype
            '''
            result = self._values.get("projection_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProjectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.ProvisionedThroughputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "read_capacity_units": "readCapacityUnits",
            "write_capacity_units": "writeCapacityUnits",
        },
    )
    class ProvisionedThroughputProperty:
        def __init__(
            self,
            *,
            read_capacity_units: jsii.Number,
            write_capacity_units: jsii.Number,
        ) -> None:
            '''
            :param read_capacity_units: ``CfnTable.ProvisionedThroughputProperty.ReadCapacityUnits``.
            :param write_capacity_units: ``CfnTable.ProvisionedThroughputProperty.WriteCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                provisioned_throughput_property = dynamodb.CfnTable.ProvisionedThroughputProperty(
                    read_capacity_units=123,
                    write_capacity_units=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "read_capacity_units": read_capacity_units,
                "write_capacity_units": write_capacity_units,
            }

        @builtins.property
        def read_capacity_units(self) -> jsii.Number:
            '''``CfnTable.ProvisionedThroughputProperty.ReadCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-readcapacityunits
            '''
            result = self._values.get("read_capacity_units")
            assert result is not None, "Required property 'read_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def write_capacity_units(self) -> jsii.Number:
            '''``CfnTable.ProvisionedThroughputProperty.WriteCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-writecapacityunits
            '''
            result = self._values.get("write_capacity_units")
            assert result is not None, "Required property 'write_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedThroughputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.SSESpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_master_key_id": "kmsMasterKeyId",
            "sse_enabled": "sseEnabled",
            "sse_type": "sseType",
        },
    )
    class SSESpecificationProperty:
        def __init__(
            self,
            *,
            kms_master_key_id: typing.Optional[builtins.str] = None,
            sse_enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
            sse_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param kms_master_key_id: ``CfnTable.SSESpecificationProperty.KMSMasterKeyId``.
            :param sse_enabled: ``CfnTable.SSESpecificationProperty.SSEEnabled``.
            :param sse_type: ``CfnTable.SSESpecificationProperty.SSEType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                s_sESpecification_property = dynamodb.CfnTable.SSESpecificationProperty(
                    sse_enabled=False,
                
                    # the properties below are optional
                    kms_master_key_id="kmsMasterKeyId",
                    sse_type="sseType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "sse_enabled": sse_enabled,
            }
            if kms_master_key_id is not None:
                self._values["kms_master_key_id"] = kms_master_key_id
            if sse_type is not None:
                self._values["sse_type"] = sse_type

        @builtins.property
        def kms_master_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnTable.SSESpecificationProperty.KMSMasterKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-kmsmasterkeyid
            '''
            result = self._values.get("kms_master_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sse_enabled(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
            '''``CfnTable.SSESpecificationProperty.SSEEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-sseenabled
            '''
            result = self._values.get("sse_enabled")
            assert result is not None, "Required property 'sse_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], result)

        @builtins.property
        def sse_type(self) -> typing.Optional[builtins.str]:
            '''``CfnTable.SSESpecificationProperty.SSEType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-ssetype
            '''
            result = self._values.get("sse_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SSESpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.StreamSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"stream_view_type": "streamViewType"},
    )
    class StreamSpecificationProperty:
        def __init__(self, *, stream_view_type: builtins.str) -> None:
            '''
            :param stream_view_type: ``CfnTable.StreamSpecificationProperty.StreamViewType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                stream_specification_property = dynamodb.CfnTable.StreamSpecificationProperty(
                    stream_view_type="streamViewType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "stream_view_type": stream_view_type,
            }

        @builtins.property
        def stream_view_type(self) -> builtins.str:
            '''``CfnTable.StreamSpecificationProperty.StreamViewType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html#cfn-dynamodb-streamspecification-streamviewtype
            '''
            result = self._values.get("stream_view_type")
            assert result is not None, "Required property 'stream_view_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dynamodb.CfnTable.TimeToLiveSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_name": "attributeName", "enabled": "enabled"},
    )
    class TimeToLiveSpecificationProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param attribute_name: ``CfnTable.TimeToLiveSpecificationProperty.AttributeName``.
            :param enabled: ``CfnTable.TimeToLiveSpecificationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dynamodb as dynamodb
                
                time_to_live_specification_property = dynamodb.CfnTable.TimeToLiveSpecificationProperty(
                    attribute_name="attributeName",
                    enabled=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attribute_name": attribute_name,
                "enabled": enabled,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''``CfnTable.TimeToLiveSpecificationProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html#cfn-dynamodb-timetolivespecification-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
            '''``CfnTable.TimeToLiveSpecificationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html#cfn-dynamodb-timetolivespecification-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeToLiveSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.CfnTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_definitions": "attributeDefinitions",
        "billing_mode": "billingMode",
        "contributor_insights_specification": "contributorInsightsSpecification",
        "global_secondary_indexes": "globalSecondaryIndexes",
        "key_schema": "keySchema",
        "kinesis_stream_specification": "kinesisStreamSpecification",
        "local_secondary_indexes": "localSecondaryIndexes",
        "point_in_time_recovery_specification": "pointInTimeRecoverySpecification",
        "provisioned_throughput": "provisionedThroughput",
        "sse_specification": "sseSpecification",
        "stream_specification": "streamSpecification",
        "table_class": "tableClass",
        "table_name": "tableName",
        "tags": "tags",
        "time_to_live_specification": "timeToLiveSpecification",
    },
)
class CfnTableProps:
    def __init__(
        self,
        *,
        attribute_definitions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnTable.AttributeDefinitionProperty, _IResolvable_a771d0ef]]]] = None,
        billing_mode: typing.Optional[builtins.str] = None,
        contributor_insights_specification: typing.Optional[typing.Union[CfnTable.ContributorInsightsSpecificationProperty, _IResolvable_a771d0ef]] = None,
        global_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnTable.GlobalSecondaryIndexProperty, _IResolvable_a771d0ef]]]] = None,
        key_schema: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnTable.KeySchemaProperty, _IResolvable_a771d0ef]]],
        kinesis_stream_specification: typing.Optional[typing.Union[CfnTable.KinesisStreamSpecificationProperty, _IResolvable_a771d0ef]] = None,
        local_secondary_indexes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnTable.LocalSecondaryIndexProperty, _IResolvable_a771d0ef]]]] = None,
        point_in_time_recovery_specification: typing.Optional[typing.Union[CfnTable.PointInTimeRecoverySpecificationProperty, _IResolvable_a771d0ef]] = None,
        provisioned_throughput: typing.Optional[typing.Union[CfnTable.ProvisionedThroughputProperty, _IResolvable_a771d0ef]] = None,
        sse_specification: typing.Optional[typing.Union[CfnTable.SSESpecificationProperty, _IResolvable_a771d0ef]] = None,
        stream_specification: typing.Optional[typing.Union[CfnTable.StreamSpecificationProperty, _IResolvable_a771d0ef]] = None,
        table_class: typing.Optional[builtins.str] = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        time_to_live_specification: typing.Optional[typing.Union[CfnTable.TimeToLiveSpecificationProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DynamoDB::Table``.

        :param attribute_definitions: ``AWS::DynamoDB::Table.AttributeDefinitions``.
        :param billing_mode: ``AWS::DynamoDB::Table.BillingMode``.
        :param contributor_insights_specification: ``AWS::DynamoDB::Table.ContributorInsightsSpecification``.
        :param global_secondary_indexes: ``AWS::DynamoDB::Table.GlobalSecondaryIndexes``.
        :param key_schema: ``AWS::DynamoDB::Table.KeySchema``.
        :param kinesis_stream_specification: ``AWS::DynamoDB::Table.KinesisStreamSpecification``.
        :param local_secondary_indexes: ``AWS::DynamoDB::Table.LocalSecondaryIndexes``.
        :param point_in_time_recovery_specification: ``AWS::DynamoDB::Table.PointInTimeRecoverySpecification``.
        :param provisioned_throughput: ``AWS::DynamoDB::Table.ProvisionedThroughput``.
        :param sse_specification: ``AWS::DynamoDB::Table.SSESpecification``.
        :param stream_specification: ``AWS::DynamoDB::Table.StreamSpecification``.
        :param table_class: ``AWS::DynamoDB::Table.TableClass``.
        :param table_name: ``AWS::DynamoDB::Table.TableName``.
        :param tags: ``AWS::DynamoDB::Table.Tags``.
        :param time_to_live_specification: ``AWS::DynamoDB::Table.TimeToLiveSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dynamodb as dynamodb
            
            cfn_table_props = dynamodb.CfnTableProps(
                key_schema=[dynamodb.CfnTable.KeySchemaProperty(
                    attribute_name="attributeName",
                    key_type="keyType"
                )],
            
                # the properties below are optional
                attribute_definitions=[dynamodb.CfnTable.AttributeDefinitionProperty(
                    attribute_name="attributeName",
                    attribute_type="attributeType"
                )],
                billing_mode="billingMode",
                contributor_insights_specification=dynamodb.CfnTable.ContributorInsightsSpecificationProperty(
                    enabled=False
                ),
                global_secondary_indexes=[dynamodb.CfnTable.GlobalSecondaryIndexProperty(
                    index_name="indexName",
                    key_schema=[dynamodb.CfnTable.KeySchemaProperty(
                        attribute_name="attributeName",
                        key_type="keyType"
                    )],
                    projection=dynamodb.CfnTable.ProjectionProperty(
                        non_key_attributes=["nonKeyAttributes"],
                        projection_type="projectionType"
                    ),
            
                    # the properties below are optional
                    contributor_insights_specification=dynamodb.CfnTable.ContributorInsightsSpecificationProperty(
                        enabled=False
                    ),
                    provisioned_throughput=dynamodb.CfnTable.ProvisionedThroughputProperty(
                        read_capacity_units=123,
                        write_capacity_units=123
                    )
                )],
                kinesis_stream_specification=dynamodb.CfnTable.KinesisStreamSpecificationProperty(
                    stream_arn="streamArn"
                ),
                local_secondary_indexes=[dynamodb.CfnTable.LocalSecondaryIndexProperty(
                    index_name="indexName",
                    key_schema=[dynamodb.CfnTable.KeySchemaProperty(
                        attribute_name="attributeName",
                        key_type="keyType"
                    )],
                    projection=dynamodb.CfnTable.ProjectionProperty(
                        non_key_attributes=["nonKeyAttributes"],
                        projection_type="projectionType"
                    )
                )],
                point_in_time_recovery_specification=dynamodb.CfnTable.PointInTimeRecoverySpecificationProperty(
                    point_in_time_recovery_enabled=False
                ),
                provisioned_throughput=dynamodb.CfnTable.ProvisionedThroughputProperty(
                    read_capacity_units=123,
                    write_capacity_units=123
                ),
                sse_specification=dynamodb.CfnTable.SSESpecificationProperty(
                    sse_enabled=False,
            
                    # the properties below are optional
                    kms_master_key_id="kmsMasterKeyId",
                    sse_type="sseType"
                ),
                stream_specification=dynamodb.CfnTable.StreamSpecificationProperty(
                    stream_view_type="streamViewType"
                ),
                table_class="tableClass",
                table_name="tableName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                time_to_live_specification=dynamodb.CfnTable.TimeToLiveSpecificationProperty(
                    attribute_name="attributeName",
                    enabled=False
                )
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "key_schema": key_schema,
        }
        if attribute_definitions is not None:
            self._values["attribute_definitions"] = attribute_definitions
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if contributor_insights_specification is not None:
            self._values["contributor_insights_specification"] = contributor_insights_specification
        if global_secondary_indexes is not None:
            self._values["global_secondary_indexes"] = global_secondary_indexes
        if kinesis_stream_specification is not None:
            self._values["kinesis_stream_specification"] = kinesis_stream_specification
        if local_secondary_indexes is not None:
            self._values["local_secondary_indexes"] = local_secondary_indexes
        if point_in_time_recovery_specification is not None:
            self._values["point_in_time_recovery_specification"] = point_in_time_recovery_specification
        if provisioned_throughput is not None:
            self._values["provisioned_throughput"] = provisioned_throughput
        if sse_specification is not None:
            self._values["sse_specification"] = sse_specification
        if stream_specification is not None:
            self._values["stream_specification"] = stream_specification
        if table_class is not None:
            self._values["table_class"] = table_class
        if table_name is not None:
            self._values["table_name"] = table_name
        if tags is not None:
            self._values["tags"] = tags
        if time_to_live_specification is not None:
            self._values["time_to_live_specification"] = time_to_live_specification

    @builtins.property
    def attribute_definitions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTable.AttributeDefinitionProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::Table.AttributeDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedef
        '''
        result = self._values.get("attribute_definitions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTable.AttributeDefinitionProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def billing_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::Table.BillingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-billingmode
        '''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contributor_insights_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnTable.ContributorInsightsSpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.ContributorInsightsSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-contributorinsightsspecification-enabled
        '''
        result = self._values.get("contributor_insights_specification")
        return typing.cast(typing.Optional[typing.Union[CfnTable.ContributorInsightsSpecificationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def global_secondary_indexes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTable.GlobalSecondaryIndexProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::Table.GlobalSecondaryIndexes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-gsi
        '''
        result = self._values.get("global_secondary_indexes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTable.GlobalSecondaryIndexProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def key_schema(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTable.KeySchemaProperty, _IResolvable_a771d0ef]]]:
        '''``AWS::DynamoDB::Table.KeySchema``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema
        '''
        result = self._values.get("key_schema")
        assert result is not None, "Required property 'key_schema' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTable.KeySchemaProperty, _IResolvable_a771d0ef]]], result)

    @builtins.property
    def kinesis_stream_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnTable.KinesisStreamSpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.KinesisStreamSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-kinesisstreamspecification
        '''
        result = self._values.get("kinesis_stream_specification")
        return typing.cast(typing.Optional[typing.Union[CfnTable.KinesisStreamSpecificationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def local_secondary_indexes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTable.LocalSecondaryIndexProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::DynamoDB::Table.LocalSecondaryIndexes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-lsi
        '''
        result = self._values.get("local_secondary_indexes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnTable.LocalSecondaryIndexProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def point_in_time_recovery_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnTable.PointInTimeRecoverySpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.PointInTimeRecoverySpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-pointintimerecoveryspecification
        '''
        result = self._values.get("point_in_time_recovery_specification")
        return typing.cast(typing.Optional[typing.Union[CfnTable.PointInTimeRecoverySpecificationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def provisioned_throughput(
        self,
    ) -> typing.Optional[typing.Union[CfnTable.ProvisionedThroughputProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.ProvisionedThroughput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput
        '''
        result = self._values.get("provisioned_throughput")
        return typing.cast(typing.Optional[typing.Union[CfnTable.ProvisionedThroughputProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def sse_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnTable.SSESpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.SSESpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-ssespecification
        '''
        result = self._values.get("sse_specification")
        return typing.cast(typing.Optional[typing.Union[CfnTable.SSESpecificationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def stream_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnTable.StreamSpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.StreamSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification
        '''
        result = self._values.get("stream_specification")
        return typing.cast(typing.Optional[typing.Union[CfnTable.StreamSpecificationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def table_class(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::Table.TableClass``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tableclass
        '''
        result = self._values.get("table_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::DynamoDB::Table.TableName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::DynamoDB::Table.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def time_to_live_specification(
        self,
    ) -> typing.Optional[typing.Union[CfnTable.TimeToLiveSpecificationProperty, _IResolvable_a771d0ef]]:
        '''``AWS::DynamoDB::Table.TimeToLiveSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-timetolivespecification
        '''
        result = self._values.get("time_to_live_specification")
        return typing.cast(typing.Optional[typing.Union[CfnTable.TimeToLiveSpecificationProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.EnableScalingProps",
    jsii_struct_bases=[],
    name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
)
class EnableScalingProps:
    def __init__(self, *, max_capacity: jsii.Number, min_capacity: jsii.Number) -> None:
        '''(experimental) Properties for enabling DynamoDB capacity scaling.

        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to.

        :stability: experimental

        Example::

            import monocdk as dynamodb
            
            # table is of type Table
            
            
            read_capacity = table.auto_scale_read_capacity(
                min_capacity=10,
                max_capacity=1000
            )
            read_capacity.scale_on_utilization(
                target_utilization_percent=60
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
        }

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''(experimental) Maximum capacity to scale to.

        :stability: experimental
        '''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''(experimental) Minimum capacity to scale to.

        :stability: experimental
        '''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnableScalingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_dynamodb.IScalableTableAttribute")
class IScalableTableAttribute(typing_extensions.Protocol):
    '''(experimental) Interface for scalable attributes.

    :stability: experimental
    '''

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(
        self,
        id: builtins.str,
        *,
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        schedule: _Schedule_c2a5a45d,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''(experimental) Add scheduled scaling for this scaling attribute.

        :param id: -
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param schedule: (experimental) When to perform this action.
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="scaleOnUtilization")
    def scale_on_utilization(
        self,
        *,
        target_utilization_percent: jsii.Number,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        '''(experimental) Scale out or in to keep utilization at a given level.

        :param target_utilization_percent: (experimental) Target utilization percentage for the attribute.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        '''
        ...


class _IScalableTableAttributeProxy:
    '''(experimental) Interface for scalable attributes.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_dynamodb.IScalableTableAttribute"

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(
        self,
        id: builtins.str,
        *,
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        schedule: _Schedule_c2a5a45d,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''(experimental) Add scheduled scaling for this scaling attribute.

        :param id: -
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param schedule: (experimental) When to perform this action.
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        '''
        actions = _ScalingSchedule_6c3fc38f(
            end_time=end_time,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            schedule=schedule,
            start_time=start_time,
        )

        return typing.cast(None, jsii.invoke(self, "scaleOnSchedule", [id, actions]))

    @jsii.member(jsii_name="scaleOnUtilization")
    def scale_on_utilization(
        self,
        *,
        target_utilization_percent: jsii.Number,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        '''(experimental) Scale out or in to keep utilization at a given level.

        :param target_utilization_percent: (experimental) Target utilization percentage for the attribute.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        '''
        props = UtilizationScalingProps(
            target_utilization_percent=target_utilization_percent,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return typing.cast(None, jsii.invoke(self, "scaleOnUtilization", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScalableTableAttribute).__jsii_proxy_class__ = lambda : _IScalableTableAttributeProxy


@jsii.interface(jsii_type="monocdk.aws_dynamodb.ITable")
class ITable(_IResource_8c1dbbbd, typing_extensions.Protocol):
    '''(experimental) An interface that represents a DynamoDB Table - either created with the CDK, or an existing one.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_36930160]:
        '''(experimental) Optional KMS encryption key associated with this table.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableArn")
    def table_arn(self) -> builtins.str:
        '''(experimental) Arn of the dynamodb table.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        '''(experimental) Table name of the dynamodb table.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableStreamArn")
    def table_stream_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) ARN of the table's stream, if there is one.

        :stability: experimental
        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_4c5a91d1,
        *actions: builtins.str,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Adds an IAM policy statement associated with this table to an IAM principal's policy.

        If ``encryptionKey`` is present, appropriate grants to the key needs to be added
        separately using the ``table.encryptionKey.grant*`` methods.

        :param grantee: The principal (no-op if undefined).
        :param actions: The set of actions to allow (i.e. "dynamodb:PutItem", "dynamodb:GetItem", ...).

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantFullAccess")
    def grant_full_access(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits all DynamoDB operations ("dynamodb:*") to an IAM principal.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantReadData")
    def grant_read_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all data read operations from this table: BatchGetItem, GetRecords, GetShardIterator, Query, GetItem, Scan.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantReadWriteData")
    def grant_read_write_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal to all data read/write operations to this table.

        BatchGetItem, GetRecords, GetShardIterator, Query, GetItem, Scan,
        BatchWriteItem, PutItem, UpdateItem, DeleteItem

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantStream")
    def grant_stream(
        self,
        grantee: _IGrantable_4c5a91d1,
        *actions: builtins.str,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Adds an IAM policy statement associated with this table's stream to an IAM principal's policy.

        If ``encryptionKey`` is present, appropriate grants to the key needs to be added
        separately using the ``table.encryptionKey.grant*`` methods.

        :param grantee: The principal (no-op if undefined).
        :param actions: The set of actions to allow (i.e. "dynamodb:DescribeStream", "dynamodb:GetRecords", ...).

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantStreamRead")
    def grant_stream_read(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all stream data read operations for this table's stream: DescribeStream, GetRecords, GetShardIterator, ListStreams.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantTableListStreams")
    def grant_table_list_streams(
        self,
        grantee: _IGrantable_4c5a91d1,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM Principal to list streams attached to current dynamodb table.

        :param grantee: The principal (no-op if undefined).

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantWriteData")
    def grant_write_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all data write operations to this table: BatchWriteItem, PutItem, UpdateItem, DeleteItem.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the number of Errors executing all Lambdas.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricConditionalCheckFailedRequests")
    def metric_conditional_check_failed_requests(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the conditional check failed requests.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricConsumedReadCapacityUnits")
    def metric_consumed_read_capacity_units(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the consumed read capacity units.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricConsumedWriteCapacityUnits")
    def metric_consumed_write_capacity_units(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the consumed write capacity units.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricSuccessfulRequestLatency")
    def metric_successful_request_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the successful request latency.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricSystemErrors")
    def metric_system_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(deprecated) Metric for the system errors.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :deprecated: use ``metricSystemErrorsForOperations``

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="metricSystemErrorsForOperations")
    def metric_system_errors_for_operations(
        self,
        *,
        operations: typing.Optional[typing.Sequence["Operation"]] = None,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _IMetric_5db43d61:
        '''(experimental) Metric for the system errors this table.

        :param operations: (experimental) The operations to apply the metric to. Default: - All operations available by DynamoDB tables will be considered.
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricThrottledRequests")
    def metric_throttled_requests(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for throttled requests.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricUserErrors")
    def metric_user_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the user errors.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...


class _ITableProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore[misc]
):
    '''(experimental) An interface that represents a DynamoDB Table - either created with the CDK, or an existing one.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_dynamodb.ITable"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_36930160]:
        '''(experimental) Optional KMS encryption key associated with this table.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_IKey_36930160], jsii.get(self, "encryptionKey"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableArn")
    def table_arn(self) -> builtins.str:
        '''(experimental) Arn of the dynamodb table.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "tableArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        '''(experimental) Table name of the dynamodb table.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableStreamArn")
    def table_stream_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) ARN of the table's stream, if there is one.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableStreamArn"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_4c5a91d1,
        *actions: builtins.str,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Adds an IAM policy statement associated with this table to an IAM principal's policy.

        If ``encryptionKey`` is present, appropriate grants to the key needs to be added
        separately using the ``table.encryptionKey.grant*`` methods.

        :param grantee: The principal (no-op if undefined).
        :param actions: The set of actions to allow (i.e. "dynamodb:PutItem", "dynamodb:GetItem", ...).

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantFullAccess")
    def grant_full_access(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits all DynamoDB operations ("dynamodb:*") to an IAM principal.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantFullAccess", [grantee]))

    @jsii.member(jsii_name="grantReadData")
    def grant_read_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all data read operations from this table: BatchGetItem, GetRecords, GetShardIterator, Query, GetItem, Scan.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantReadData", [grantee]))

    @jsii.member(jsii_name="grantReadWriteData")
    def grant_read_write_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal to all data read/write operations to this table.

        BatchGetItem, GetRecords, GetShardIterator, Query, GetItem, Scan,
        BatchWriteItem, PutItem, UpdateItem, DeleteItem

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantReadWriteData", [grantee]))

    @jsii.member(jsii_name="grantStream")
    def grant_stream(
        self,
        grantee: _IGrantable_4c5a91d1,
        *actions: builtins.str,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Adds an IAM policy statement associated with this table's stream to an IAM principal's policy.

        If ``encryptionKey`` is present, appropriate grants to the key needs to be added
        separately using the ``table.encryptionKey.grant*`` methods.

        :param grantee: The principal (no-op if undefined).
        :param actions: The set of actions to allow (i.e. "dynamodb:DescribeStream", "dynamodb:GetRecords", ...).

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantStream", [grantee, *actions]))

    @jsii.member(jsii_name="grantStreamRead")
    def grant_stream_read(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all stream data read operations for this table's stream: DescribeStream, GetRecords, GetShardIterator, ListStreams.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantStreamRead", [grantee]))

    @jsii.member(jsii_name="grantTableListStreams")
    def grant_table_list_streams(
        self,
        grantee: _IGrantable_4c5a91d1,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM Principal to list streams attached to current dynamodb table.

        :param grantee: The principal (no-op if undefined).

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantTableListStreams", [grantee]))

    @jsii.member(jsii_name="grantWriteData")
    def grant_write_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all data write operations to this table: BatchWriteItem, PutItem, UpdateItem, DeleteItem.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantWriteData", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the number of Errors executing all Lambdas.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricConditionalCheckFailedRequests")
    def metric_conditional_check_failed_requests(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the conditional check failed requests.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricConditionalCheckFailedRequests", [props]))

    @jsii.member(jsii_name="metricConsumedReadCapacityUnits")
    def metric_consumed_read_capacity_units(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the consumed read capacity units.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricConsumedReadCapacityUnits", [props]))

    @jsii.member(jsii_name="metricConsumedWriteCapacityUnits")
    def metric_consumed_write_capacity_units(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the consumed write capacity units.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricConsumedWriteCapacityUnits", [props]))

    @jsii.member(jsii_name="metricSuccessfulRequestLatency")
    def metric_successful_request_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the successful request latency.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricSuccessfulRequestLatency", [props]))

    @jsii.member(jsii_name="metricSystemErrors")
    def metric_system_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(deprecated) Metric for the system errors.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :deprecated: use ``metricSystemErrorsForOperations``

        :stability: deprecated
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricSystemErrors", [props]))

    @jsii.member(jsii_name="metricSystemErrorsForOperations")
    def metric_system_errors_for_operations(
        self,
        *,
        operations: typing.Optional[typing.Sequence["Operation"]] = None,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _IMetric_5db43d61:
        '''(experimental) Metric for the system errors this table.

        :param operations: (experimental) The operations to apply the metric to. Default: - All operations available by DynamoDB tables will be considered.
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = SystemErrorsForOperationsMetricOptions(
            operations=operations,
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_IMetric_5db43d61, jsii.invoke(self, "metricSystemErrorsForOperations", [props]))

    @jsii.member(jsii_name="metricThrottledRequests")
    def metric_throttled_requests(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for throttled requests.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricThrottledRequests", [props]))

    @jsii.member(jsii_name="metricUserErrors")
    def metric_user_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the user errors.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricUserErrors", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITable).__jsii_proxy_class__ = lambda : _ITableProxy


@jsii.enum(jsii_type="monocdk.aws_dynamodb.Operation")
class Operation(enum.Enum):
    '''(experimental) Supported DynamoDB table operations.

    :stability: experimental
    '''

    BATCH_EXECUTE_STATEMENT = "BATCH_EXECUTE_STATEMENT"
    '''(experimental) BatchExecuteStatement.

    :stability: experimental
    '''
    BATCH_GET_ITEM = "BATCH_GET_ITEM"
    '''(experimental) BatchGetItem.

    :stability: experimental
    '''
    BATCH_WRITE_ITEM = "BATCH_WRITE_ITEM"
    '''(experimental) BatchWriteItem.

    :stability: experimental
    '''
    DELETE_ITEM = "DELETE_ITEM"
    '''(experimental) DeleteItem.

    :stability: experimental
    '''
    EXECUTE_STATEMENT = "EXECUTE_STATEMENT"
    '''(experimental) ExecuteStatement.

    :stability: experimental
    '''
    EXECUTE_TRANSACTION = "EXECUTE_TRANSACTION"
    '''(experimental) ExecuteTransaction.

    :stability: experimental
    '''
    GET_ITEM = "GET_ITEM"
    '''(experimental) GetItem.

    :stability: experimental
    '''
    GET_RECORDS = "GET_RECORDS"
    '''(experimental) GetRecords.

    :stability: experimental
    '''
    PUT_ITEM = "PUT_ITEM"
    '''(experimental) PutItem.

    :stability: experimental
    '''
    QUERY = "QUERY"
    '''(experimental) Query.

    :stability: experimental
    '''
    SCAN = "SCAN"
    '''(experimental) Scan.

    :stability: experimental
    '''
    TRANSACT_GET_ITEMS = "TRANSACT_GET_ITEMS"
    '''(experimental) TransactGetItems.

    :stability: experimental
    '''
    TRANSACT_WRITE_ITEMS = "TRANSACT_WRITE_ITEMS"
    '''(experimental) TransactWriteItems.

    :stability: experimental
    '''
    UPDATE_ITEM = "UPDATE_ITEM"
    '''(experimental) UpdateItem.

    :stability: experimental
    '''


@jsii.enum(jsii_type="monocdk.aws_dynamodb.ProjectionType")
class ProjectionType(enum.Enum):
    '''(experimental) The set of attributes that are projected into the index.

    :see: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Projection.html
    :stability: experimental
    '''

    ALL = "ALL"
    '''(experimental) All of the table attributes are projected into the index.

    :stability: experimental
    '''
    INCLUDE = "INCLUDE"
    '''(experimental) Only the specified table attributes are projected into the index.

    The list of projected attributes is in ``nonKeyAttributes``.

    :stability: experimental
    '''
    KEYS_ONLY = "KEYS_ONLY"
    '''(experimental) Only the index and primary keys are projected into the index.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.SchemaOptions",
    jsii_struct_bases=[],
    name_mapping={"partition_key": "partitionKey", "sort_key": "sortKey"},
)
class SchemaOptions:
    def __init__(
        self,
        *,
        partition_key: Attribute,
        sort_key: typing.Optional[Attribute] = None,
    ) -> None:
        '''(experimental) Represents the table schema attributes.

        :param partition_key: (experimental) Partition key attribute definition.
        :param sort_key: (experimental) Sort key attribute definition. Default: no sort key

        :stability: experimental

        Example::

            # table is of type Table
            
            schema = table.schema()
            partition_key = schema.partition_key
            sort_key = schema.sort_key
        '''
        if isinstance(partition_key, dict):
            partition_key = Attribute(**partition_key)
        if isinstance(sort_key, dict):
            sort_key = Attribute(**sort_key)
        self._values: typing.Dict[str, typing.Any] = {
            "partition_key": partition_key,
        }
        if sort_key is not None:
            self._values["sort_key"] = sort_key

    @builtins.property
    def partition_key(self) -> Attribute:
        '''(experimental) Partition key attribute definition.

        :stability: experimental
        '''
        result = self._values.get("partition_key")
        assert result is not None, "Required property 'partition_key' is missing"
        return typing.cast(Attribute, result)

    @builtins.property
    def sort_key(self) -> typing.Optional[Attribute]:
        '''(experimental) Sort key attribute definition.

        :default: no sort key

        :stability: experimental
        '''
        result = self._values.get("sort_key")
        return typing.cast(typing.Optional[Attribute], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.SecondaryIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "index_name": "indexName",
        "non_key_attributes": "nonKeyAttributes",
        "projection_type": "projectionType",
    },
)
class SecondaryIndexProps:
    def __init__(
        self,
        *,
        index_name: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        projection_type: typing.Optional[ProjectionType] = None,
    ) -> None:
        '''(experimental) Properties for a secondary index.

        :param index_name: (experimental) The name of the secondary index.
        :param non_key_attributes: (experimental) The non-key attributes that are projected into the secondary index. Default: - No additional attributes
        :param projection_type: (experimental) The set of attributes that are projected into the secondary index. Default: ALL

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dynamodb as dynamodb
            
            secondary_index_props = dynamodb.SecondaryIndexProps(
                index_name="indexName",
            
                # the properties below are optional
                non_key_attributes=["nonKeyAttributes"],
                projection_type=dynamodb.ProjectionType.KEYS_ONLY
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "index_name": index_name,
        }
        if non_key_attributes is not None:
            self._values["non_key_attributes"] = non_key_attributes
        if projection_type is not None:
            self._values["projection_type"] = projection_type

    @builtins.property
    def index_name(self) -> builtins.str:
        '''(experimental) The name of the secondary index.

        :stability: experimental
        '''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The non-key attributes that are projected into the secondary index.

        :default: - No additional attributes

        :stability: experimental
        '''
        result = self._values.get("non_key_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def projection_type(self) -> typing.Optional[ProjectionType]:
        '''(experimental) The set of attributes that are projected into the secondary index.

        :default: ALL

        :stability: experimental
        '''
        result = self._values.get("projection_type")
        return typing.cast(typing.Optional[ProjectionType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecondaryIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_dynamodb.StreamViewType")
class StreamViewType(enum.Enum):
    '''(experimental) When an item in the table is modified, StreamViewType determines what information is written to the stream for this table.

    :see: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StreamSpecification.html
    :stability: experimental
    '''

    KEYS_ONLY = "KEYS_ONLY"
    '''(experimental) Only the key attributes of the modified item are written to the stream.

    :stability: experimental
    '''
    NEW_AND_OLD_IMAGES = "NEW_AND_OLD_IMAGES"
    '''(experimental) Both the new and the old item images of the item are written to the stream.

    :stability: experimental
    '''
    NEW_IMAGE = "NEW_IMAGE"
    '''(experimental) The entire item, as it appears after it was modified, is written to the stream.

    :stability: experimental
    '''
    OLD_IMAGE = "OLD_IMAGE"
    '''(experimental) The entire item, as it appeared before it was modified, is written to the stream.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.SystemErrorsForOperationsMetricOptions",
    jsii_struct_bases=[_MetricOptions_1c185ae8],
    name_mapping={
        "account": "account",
        "color": "color",
        "dimensions": "dimensions",
        "dimensions_map": "dimensionsMap",
        "label": "label",
        "period": "period",
        "region": "region",
        "statistic": "statistic",
        "unit": "unit",
        "operations": "operations",
    },
)
class SystemErrorsForOperationsMetricOptions(_MetricOptions_1c185ae8):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
        operations: typing.Optional[typing.Sequence[Operation]] = None,
    ) -> None:
        '''(experimental) Options for configuring a system errors metric that considers multiple operations.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param operations: (experimental) The operations to apply the metric to. Default: - All operations available by DynamoDB tables will be considered.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_cloudwatch as cloudwatch
            from monocdk import aws_dynamodb as dynamodb
            
            # dimensions is of type object
            # duration is of type Duration
            
            system_errors_for_operations_metric_options = dynamodb.SystemErrorsForOperationsMetricOptions(
                account="account",
                color="color",
                dimensions={
                    "dimensions_key": dimensions
                },
                dimensions_map={
                    "dimensions_map_key": "dimensionsMap"
                },
                label="label",
                operations=[dynamodb.Operation.GET_ITEM],
                period=duration,
                region="region",
                statistic="statistic",
                unit=cloudwatch.Unit.SECONDS
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if color is not None:
            self._values["color"] = color
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if dimensions_map is not None:
            self._values["dimensions_map"] = dimensions_map
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if region is not None:
            self._values["region"] = region
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit
        if operations is not None:
            self._values["operations"] = operations

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account which this metric comes from.

        :default: - Deployment account.

        :stability: experimental
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color

        :stability: experimental
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(deprecated) Dimensions of the metric.

        :default: - No dimensions.

        :deprecated: Use 'dimensionsMap' instead.

        :stability: deprecated
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def dimensions_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Dimensions of the metric.

        :default: - No dimensions.

        :stability: experimental
        '''
        result = self._values.get("dimensions_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for this metric when added to a Graph in a Dashboard.

        :default: - No label

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The period over which the specified statistic is applied.

        :default: Duration.minutes(5)

        :stability: experimental
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region which this metric comes from.

        :default: - Deployment region.

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''(experimental) What function to use for aggregating.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"

        :default: Average

        :stability: experimental
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[_Unit_113c79f9]:
        '''(experimental) Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        The default is to use all matric datums in the stream, regardless of unit,
        which is recommended in nearly all cases.

        CloudWatch does not honor this property for graphs.

        :default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[_Unit_113c79f9], result)

    @builtins.property
    def operations(self) -> typing.Optional[typing.List[Operation]]:
        '''(experimental) The operations to apply the metric to.

        :default: - All operations available by DynamoDB tables will be considered.

        :stability: experimental
        '''
        result = self._values.get("operations")
        return typing.cast(typing.Optional[typing.List[Operation]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SystemErrorsForOperationsMetricOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ITable)
class Table(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dynamodb.Table",
):
    '''(experimental) Provides a DynamoDB table.

    :stability: experimental

    Example::

        global_table = dynamodb.Table(self, "Table",
            partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            replication_regions=["us-east-1", "us-east-2", "us-west-2"],
            billing_mode=dynamodb.BillingMode.PROVISIONED
        )
        
        global_table.auto_scale_write_capacity(
            min_capacity=1,
            max_capacity=10
        ).scale_on_utilization(target_utilization_percent=75)
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        kinesis_stream: typing.Optional[_IStream_14c6ec7f] = None,
        table_name: typing.Optional[builtins.str] = None,
        billing_mode: typing.Optional[BillingMode] = None,
        contributor_insights_enabled: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional["TableEncryption"] = None,
        encryption_key: typing.Optional[_IKey_36930160] = None,
        point_in_time_recovery: typing.Optional[builtins.bool] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        replication_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        replication_timeout: typing.Optional[_Duration_070aa057] = None,
        server_side_encryption: typing.Optional[builtins.bool] = None,
        stream: typing.Optional[StreamViewType] = None,
        time_to_live_attribute: typing.Optional[builtins.str] = None,
        wait_for_replication_to_finish: typing.Optional[builtins.bool] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
        partition_key: Attribute,
        sort_key: typing.Optional[Attribute] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param kinesis_stream: (experimental) Kinesis Data Stream to capture item-level changes for the table. Default: - no Kinesis Data Stream
        :param table_name: (experimental) Enforces a particular physical table name. Default: 
        :param billing_mode: (experimental) Specify how you are charged for read and write throughput and how you manage capacity. Default: PROVISIONED if ``replicationRegions`` is not specified, PAY_PER_REQUEST otherwise
        :param contributor_insights_enabled: (experimental) Whether CloudWatch contributor insights is enabled. Default: false
        :param encryption: (experimental) Whether server-side encryption with an AWS managed customer master key is enabled. This property cannot be set if ``serverSideEncryption`` is set. Default: - server-side encryption is enabled with an AWS owned customer master key
        :param encryption_key: (experimental) External KMS key to use for table encryption. This property can only be set if ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED``. Default: - If ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED`` and this property is undefined, a new KMS key will be created and associated with this table.
        :param point_in_time_recovery: (experimental) Whether point-in-time recovery is enabled. Default: - point-in-time recovery is disabled
        :param read_capacity: (experimental) The read capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5
        :param removal_policy: (experimental) The removal policy to apply to the DynamoDB Table. Default: RemovalPolicy.RETAIN
        :param replication_regions: (experimental) Regions where replica tables will be created. Default: - no replica tables are created
        :param replication_timeout: (experimental) The timeout for a table replication operation in a single region. Default: Duration.minutes(30)
        :param server_side_encryption: (deprecated) Whether server-side encryption with an AWS managed customer master key is enabled. This property cannot be set if ``encryption`` and/or ``encryptionKey`` is set. Default: - server-side encryption is enabled with an AWS owned customer master key
        :param stream: (experimental) When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Default: - streams are disabled unless ``replicationRegions`` is specified
        :param time_to_live_attribute: (experimental) The name of TTL attribute. Default: - TTL is disabled
        :param wait_for_replication_to_finish: (experimental) Indicates whether CloudFormation stack waits for replication to finish. If set to false, the CloudFormation resource will mark the resource as created and replication will be completed asynchronously. This property is ignored if replicationRegions property is not set. DO NOT UNSET this property if adding/removing multiple replicationRegions in one deployment, as CloudFormation only supports one region replication at a time. CDK overcomes this limitation by waiting for replication to finish before starting new replicationRegion. Default: true
        :param write_capacity: (experimental) The write capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5
        :param partition_key: (experimental) Partition key attribute definition.
        :param sort_key: (experimental) Sort key attribute definition. Default: no sort key

        :stability: experimental
        '''
        props = TableProps(
            kinesis_stream=kinesis_stream,
            table_name=table_name,
            billing_mode=billing_mode,
            contributor_insights_enabled=contributor_insights_enabled,
            encryption=encryption,
            encryption_key=encryption_key,
            point_in_time_recovery=point_in_time_recovery,
            read_capacity=read_capacity,
            removal_policy=removal_policy,
            replication_regions=replication_regions,
            replication_timeout=replication_timeout,
            server_side_encryption=server_side_encryption,
            stream=stream,
            time_to_live_attribute=time_to_live_attribute,
            wait_for_replication_to_finish=wait_for_replication_to_finish,
            write_capacity=write_capacity,
            partition_key=partition_key,
            sort_key=sort_key,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromTableArn") # type: ignore[misc]
    @builtins.classmethod
    def from_table_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        table_arn: builtins.str,
    ) -> ITable:
        '''(experimental) Creates a Table construct that represents an external table via table arn.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param table_arn: The table's ARN.

        :stability: experimental
        '''
        return typing.cast(ITable, jsii.sinvoke(cls, "fromTableArn", [scope, id, table_arn]))

    @jsii.member(jsii_name="fromTableAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_table_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        encryption_key: typing.Optional[_IKey_36930160] = None,
        global_indexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_indexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        table_arn: typing.Optional[builtins.str] = None,
        table_name: typing.Optional[builtins.str] = None,
        table_stream_arn: typing.Optional[builtins.str] = None,
    ) -> ITable:
        '''(experimental) Creates a Table construct that represents an external table.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param encryption_key: (experimental) KMS encryption key, if this table uses a customer-managed encryption key. Default: - no key
        :param global_indexes: (experimental) The name of the global indexes set for this Table. Note that you need to set either this property, or {@link localIndexes}, if you want methods like grantReadData() to grant permissions for indexes as well as the table itself. Default: - no global indexes
        :param local_indexes: (experimental) The name of the local indexes set for this Table. Note that you need to set either this property, or {@link globalIndexes}, if you want methods like grantReadData() to grant permissions for indexes as well as the table itself. Default: - no local indexes
        :param table_arn: (experimental) The ARN of the dynamodb table. One of this, or {@link tableName}, is required. Default: - no table arn
        :param table_name: (experimental) The table name of the dynamodb table. One of this, or {@link tableArn}, is required. Default: - no table name
        :param table_stream_arn: (experimental) The ARN of the table's stream. Default: - no table stream

        :stability: experimental
        '''
        attrs = TableAttributes(
            encryption_key=encryption_key,
            global_indexes=global_indexes,
            local_indexes=local_indexes,
            table_arn=table_arn,
            table_name=table_name,
            table_stream_arn=table_stream_arn,
        )

        return typing.cast(ITable, jsii.sinvoke(cls, "fromTableAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromTableName") # type: ignore[misc]
    @builtins.classmethod
    def from_table_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        table_name: builtins.str,
    ) -> ITable:
        '''(experimental) Creates a Table construct that represents an external table via table name.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param table_name: The table's name.

        :stability: experimental
        '''
        return typing.cast(ITable, jsii.sinvoke(cls, "fromTableName", [scope, id, table_name]))

    @jsii.member(jsii_name="grantListStreams") # type: ignore[misc]
    @builtins.classmethod
    def grant_list_streams(cls, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(deprecated) Permits an IAM Principal to list all DynamoDB Streams.

        :param grantee: The principal (no-op if undefined).

        :deprecated: Use {@link #grantTableListStreams} for more granular permission

        :stability: deprecated
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.sinvoke(cls, "grantListStreams", [grantee]))

    @jsii.member(jsii_name="addGlobalSecondaryIndex")
    def add_global_secondary_index(
        self,
        *,
        read_capacity: typing.Optional[jsii.Number] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
        index_name: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        projection_type: typing.Optional[ProjectionType] = None,
        partition_key: Attribute,
        sort_key: typing.Optional[Attribute] = None,
    ) -> None:
        '''(experimental) Add a global secondary index of table.

        :param read_capacity: (experimental) The read capacity for the global secondary index. Can only be provided if table billingMode is Provisioned or undefined. Default: 5
        :param write_capacity: (experimental) The write capacity for the global secondary index. Can only be provided if table billingMode is Provisioned or undefined. Default: 5
        :param index_name: (experimental) The name of the secondary index.
        :param non_key_attributes: (experimental) The non-key attributes that are projected into the secondary index. Default: - No additional attributes
        :param projection_type: (experimental) The set of attributes that are projected into the secondary index. Default: ALL
        :param partition_key: (experimental) Partition key attribute definition.
        :param sort_key: (experimental) Sort key attribute definition. Default: no sort key

        :stability: experimental
        '''
        props = GlobalSecondaryIndexProps(
            read_capacity=read_capacity,
            write_capacity=write_capacity,
            index_name=index_name,
            non_key_attributes=non_key_attributes,
            projection_type=projection_type,
            partition_key=partition_key,
            sort_key=sort_key,
        )

        return typing.cast(None, jsii.invoke(self, "addGlobalSecondaryIndex", [props]))

    @jsii.member(jsii_name="addLocalSecondaryIndex")
    def add_local_secondary_index(
        self,
        *,
        sort_key: Attribute,
        index_name: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        projection_type: typing.Optional[ProjectionType] = None,
    ) -> None:
        '''(experimental) Add a local secondary index of table.

        :param sort_key: (experimental) The attribute of a sort key for the local secondary index.
        :param index_name: (experimental) The name of the secondary index.
        :param non_key_attributes: (experimental) The non-key attributes that are projected into the secondary index. Default: - No additional attributes
        :param projection_type: (experimental) The set of attributes that are projected into the secondary index. Default: ALL

        :stability: experimental
        '''
        props = LocalSecondaryIndexProps(
            sort_key=sort_key,
            index_name=index_name,
            non_key_attributes=non_key_attributes,
            projection_type=projection_type,
        )

        return typing.cast(None, jsii.invoke(self, "addLocalSecondaryIndex", [props]))

    @jsii.member(jsii_name="autoScaleGlobalSecondaryIndexReadCapacity")
    def auto_scale_global_secondary_index_read_capacity(
        self,
        index_name: builtins.str,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
    ) -> IScalableTableAttribute:
        '''(experimental) Enable read capacity scaling for the given GSI.

        :param index_name: -
        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to.

        :return: An object to configure additional AutoScaling settings for this attribute

        :stability: experimental
        '''
        props = EnableScalingProps(
            max_capacity=max_capacity, min_capacity=min_capacity
        )

        return typing.cast(IScalableTableAttribute, jsii.invoke(self, "autoScaleGlobalSecondaryIndexReadCapacity", [index_name, props]))

    @jsii.member(jsii_name="autoScaleGlobalSecondaryIndexWriteCapacity")
    def auto_scale_global_secondary_index_write_capacity(
        self,
        index_name: builtins.str,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
    ) -> IScalableTableAttribute:
        '''(experimental) Enable write capacity scaling for the given GSI.

        :param index_name: -
        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to.

        :return: An object to configure additional AutoScaling settings for this attribute

        :stability: experimental
        '''
        props = EnableScalingProps(
            max_capacity=max_capacity, min_capacity=min_capacity
        )

        return typing.cast(IScalableTableAttribute, jsii.invoke(self, "autoScaleGlobalSecondaryIndexWriteCapacity", [index_name, props]))

    @jsii.member(jsii_name="autoScaleReadCapacity")
    def auto_scale_read_capacity(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
    ) -> IScalableTableAttribute:
        '''(experimental) Enable read capacity scaling for this table.

        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to.

        :return: An object to configure additional AutoScaling settings

        :stability: experimental
        '''
        props = EnableScalingProps(
            max_capacity=max_capacity, min_capacity=min_capacity
        )

        return typing.cast(IScalableTableAttribute, jsii.invoke(self, "autoScaleReadCapacity", [props]))

    @jsii.member(jsii_name="autoScaleWriteCapacity")
    def auto_scale_write_capacity(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
    ) -> IScalableTableAttribute:
        '''(experimental) Enable write capacity scaling for this table.

        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to.

        :return: An object to configure additional AutoScaling settings for this attribute

        :stability: experimental
        '''
        props = EnableScalingProps(
            max_capacity=max_capacity, min_capacity=min_capacity
        )

        return typing.cast(IScalableTableAttribute, jsii.invoke(self, "autoScaleWriteCapacity", [props]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_4c5a91d1,
        *actions: builtins.str,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Adds an IAM policy statement associated with this table to an IAM principal's policy.

        If ``encryptionKey`` is present, appropriate grants to the key needs to be added
        separately using the ``table.encryptionKey.grant*`` methods.

        :param grantee: The principal (no-op if undefined).
        :param actions: The set of actions to allow (i.e. "dynamodb:PutItem", "dynamodb:GetItem", ...).

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantFullAccess")
    def grant_full_access(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits all DynamoDB operations ("dynamodb:*") to an IAM principal.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantFullAccess", [grantee]))

    @jsii.member(jsii_name="grantReadData")
    def grant_read_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all data read operations from this table: BatchGetItem, GetRecords, GetShardIterator, Query, GetItem, Scan.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantReadData", [grantee]))

    @jsii.member(jsii_name="grantReadWriteData")
    def grant_read_write_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal to all data read/write operations to this table.

        BatchGetItem, GetRecords, GetShardIterator, Query, GetItem, Scan,
        BatchWriteItem, PutItem, UpdateItem, DeleteItem

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantReadWriteData", [grantee]))

    @jsii.member(jsii_name="grantStream")
    def grant_stream(
        self,
        grantee: _IGrantable_4c5a91d1,
        *actions: builtins.str,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Adds an IAM policy statement associated with this table's stream to an IAM principal's policy.

        If ``encryptionKey`` is present, appropriate grants to the key needs to be added
        separately using the ``table.encryptionKey.grant*`` methods.

        :param grantee: The principal (no-op if undefined).
        :param actions: The set of actions to allow (i.e. "dynamodb:DescribeStream", "dynamodb:GetRecords", ...).

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantStream", [grantee, *actions]))

    @jsii.member(jsii_name="grantStreamRead")
    def grant_stream_read(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all stream data read operations for this table's stream: DescribeStream, GetRecords, GetShardIterator, ListStreams.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantStreamRead", [grantee]))

    @jsii.member(jsii_name="grantTableListStreams")
    def grant_table_list_streams(
        self,
        grantee: _IGrantable_4c5a91d1,
    ) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM Principal to list streams attached to current dynamodb table.

        :param grantee: The principal (no-op if undefined).

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantTableListStreams", [grantee]))

    @jsii.member(jsii_name="grantWriteData")
    def grant_write_data(self, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Permits an IAM principal all data write operations to this table: BatchWriteItem, PutItem, UpdateItem, DeleteItem.

        Appropriate grants will also be added to the customer-managed KMS key
        if one was configured.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.invoke(self, "grantWriteData", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Return the given named metric for this Table.

        By default, the metric will be calculated as a sum over a period of 5 minutes.
        You can customize this by using the ``statistic`` and ``period`` properties.

        :param metric_name: -
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricConditionalCheckFailedRequests")
    def metric_conditional_check_failed_requests(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the conditional check failed requests this table.

        By default, the metric will be calculated as a sum over a period of 5 minutes.
        You can customize this by using the ``statistic`` and ``period`` properties.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricConditionalCheckFailedRequests", [props]))

    @jsii.member(jsii_name="metricConsumedReadCapacityUnits")
    def metric_consumed_read_capacity_units(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the consumed read capacity units this table.

        By default, the metric will be calculated as a sum over a period of 5 minutes.
        You can customize this by using the ``statistic`` and ``period`` properties.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricConsumedReadCapacityUnits", [props]))

    @jsii.member(jsii_name="metricConsumedWriteCapacityUnits")
    def metric_consumed_write_capacity_units(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the consumed write capacity units this table.

        By default, the metric will be calculated as a sum over a period of 5 minutes.
        You can customize this by using the ``statistic`` and ``period`` properties.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricConsumedWriteCapacityUnits", [props]))

    @jsii.member(jsii_name="metricSuccessfulRequestLatency")
    def metric_successful_request_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the successful request latency this table.

        By default, the metric will be calculated as an average over a period of 5 minutes.
        You can customize this by using the ``statistic`` and ``period`` properties.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricSuccessfulRequestLatency", [props]))

    @jsii.member(jsii_name="metricSystemErrors")
    def metric_system_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(deprecated) Metric for the system errors this table.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :deprecated: use ``metricSystemErrorsForOperations``.

        :stability: deprecated
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricSystemErrors", [props]))

    @jsii.member(jsii_name="metricSystemErrorsForOperations")
    def metric_system_errors_for_operations(
        self,
        *,
        operations: typing.Optional[typing.Sequence[Operation]] = None,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _IMetric_5db43d61:
        '''(experimental) Metric for the system errors this table.

        This will sum errors across all possible operations.
        Note that by default, each individual metric will be calculated as a sum over a period of 5 minutes.
        You can customize this by using the ``statistic`` and ``period`` properties.

        :param operations: (experimental) The operations to apply the metric to. Default: - All operations available by DynamoDB tables will be considered.
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = SystemErrorsForOperationsMetricOptions(
            operations=operations,
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_IMetric_5db43d61, jsii.invoke(self, "metricSystemErrorsForOperations", [props]))

    @jsii.member(jsii_name="metricThrottledRequests")
    def metric_throttled_requests(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) How many requests are throttled on this table.

        Default: sum over 5 minutes

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricThrottledRequests", [props]))

    @jsii.member(jsii_name="metricUserErrors")
    def metric_user_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_113c79f9] = None,
    ) -> _Metric_5b2b8e58:
        '''(experimental) Metric for the user errors.

        Note that this metric reports user errors across all
        the tables in the account and region the table resides in.

        By default, the metric will be calculated as a sum over a period of 5 minutes.
        You can customize this by using the ``statistic`` and ``period`` properties.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = _MetricOptions_1c185ae8(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_5b2b8e58, jsii.invoke(self, "metricUserErrors", [props]))

    @jsii.member(jsii_name="schema")
    def schema(self, index_name: typing.Optional[builtins.str] = None) -> SchemaOptions:
        '''(experimental) Get schema attributes of table or index.

        :param index_name: -

        :return: Schema of table or index.

        :stability: experimental
        '''
        return typing.cast(SchemaOptions, jsii.invoke(self, "schema", [index_name]))

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[builtins.str]:
        '''(experimental) Validate the table construct.

        :return: an array of validation error message

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validate", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hasIndex")
    def _has_index(self) -> builtins.bool:
        '''(experimental) Whether this table has indexes.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "hasIndex"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="regionalArns")
    def _regional_arns(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regionalArns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableArn")
    def table_arn(self) -> builtins.str:
        '''(experimental) Arn of the dynamodb table.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "tableArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        '''(experimental) Table name of the dynamodb table.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_36930160]:
        '''(experimental) KMS encryption key, if this table uses a customer-managed encryption key.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_IKey_36930160], jsii.get(self, "encryptionKey"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableStreamArn")
    def table_stream_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) ARN of the table's stream, if there is one.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableStreamArn"))


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.TableAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_key": "encryptionKey",
        "global_indexes": "globalIndexes",
        "local_indexes": "localIndexes",
        "table_arn": "tableArn",
        "table_name": "tableName",
        "table_stream_arn": "tableStreamArn",
    },
)
class TableAttributes:
    def __init__(
        self,
        *,
        encryption_key: typing.Optional[_IKey_36930160] = None,
        global_indexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_indexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        table_arn: typing.Optional[builtins.str] = None,
        table_name: typing.Optional[builtins.str] = None,
        table_stream_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Reference to a dynamodb table.

        :param encryption_key: (experimental) KMS encryption key, if this table uses a customer-managed encryption key. Default: - no key
        :param global_indexes: (experimental) The name of the global indexes set for this Table. Note that you need to set either this property, or {@link localIndexes}, if you want methods like grantReadData() to grant permissions for indexes as well as the table itself. Default: - no global indexes
        :param local_indexes: (experimental) The name of the local indexes set for this Table. Note that you need to set either this property, or {@link globalIndexes}, if you want methods like grantReadData() to grant permissions for indexes as well as the table itself. Default: - no local indexes
        :param table_arn: (experimental) The ARN of the dynamodb table. One of this, or {@link tableName}, is required. Default: - no table arn
        :param table_name: (experimental) The table name of the dynamodb table. One of this, or {@link tableArn}, is required. Default: - no table name
        :param table_stream_arn: (experimental) The ARN of the table's stream. Default: - no table stream

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dynamodb as dynamodb
            from monocdk import aws_kms as kms
            
            # key is of type Key
            
            table_attributes = dynamodb.TableAttributes(
                encryption_key=key,
                global_indexes=["globalIndexes"],
                local_indexes=["localIndexes"],
                table_arn="tableArn",
                table_name="tableName",
                table_stream_arn="tableStreamArn"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if global_indexes is not None:
            self._values["global_indexes"] = global_indexes
        if local_indexes is not None:
            self._values["local_indexes"] = local_indexes
        if table_arn is not None:
            self._values["table_arn"] = table_arn
        if table_name is not None:
            self._values["table_name"] = table_name
        if table_stream_arn is not None:
            self._values["table_stream_arn"] = table_stream_arn

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_36930160]:
        '''(experimental) KMS encryption key, if this table uses a customer-managed encryption key.

        :default: - no key

        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_36930160], result)

    @builtins.property
    def global_indexes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The name of the global indexes set for this Table.

        Note that you need to set either this property,
        or {@link localIndexes},
        if you want methods like grantReadData()
        to grant permissions for indexes as well as the table itself.

        :default: - no global indexes

        :stability: experimental
        '''
        result = self._values.get("global_indexes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def local_indexes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The name of the local indexes set for this Table.

        Note that you need to set either this property,
        or {@link globalIndexes},
        if you want methods like grantReadData()
        to grant permissions for indexes as well as the table itself.

        :default: - no local indexes

        :stability: experimental
        '''
        result = self._values.get("local_indexes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def table_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) The ARN of the dynamodb table.

        One of this, or {@link tableName}, is required.

        :default: - no table arn

        :stability: experimental
        '''
        result = self._values.get("table_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The table name of the dynamodb table.

        One of this, or {@link tableArn}, is required.

        :default: - no table name

        :stability: experimental
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_stream_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) The ARN of the table's stream.

        :default: - no table stream

        :stability: experimental
        '''
        result = self._values.get("table_stream_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_dynamodb.TableEncryption")
class TableEncryption(enum.Enum):
    '''(experimental) What kind of server-side encryption to apply to this table.

    :stability: experimental

    Example::

        table = dynamodb.Table(self, "MyTable",
            partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            encryption=dynamodb.TableEncryption.CUSTOMER_MANAGED
        )
        
        # You can access the CMK that was added to the stack on your behalf by the Table construct via:
        table_encryption_key = table.encryption_key
    '''

    AWS_MANAGED = "AWS_MANAGED"
    '''(experimental) Server-side KMS encryption with a master key managed by AWS.

    :stability: experimental
    '''
    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    '''(experimental) Server-side KMS encryption with a customer master key managed by customer.

    If ``encryptionKey`` is specified, this key will be used, otherwise, one will be defined.

    :stability: experimental
    '''
    DEFAULT = "DEFAULT"
    '''(experimental) Server-side KMS encryption with a master key owned by AWS.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.TableOptions",
    jsii_struct_bases=[SchemaOptions],
    name_mapping={
        "partition_key": "partitionKey",
        "sort_key": "sortKey",
        "billing_mode": "billingMode",
        "contributor_insights_enabled": "contributorInsightsEnabled",
        "encryption": "encryption",
        "encryption_key": "encryptionKey",
        "point_in_time_recovery": "pointInTimeRecovery",
        "read_capacity": "readCapacity",
        "removal_policy": "removalPolicy",
        "replication_regions": "replicationRegions",
        "replication_timeout": "replicationTimeout",
        "server_side_encryption": "serverSideEncryption",
        "stream": "stream",
        "time_to_live_attribute": "timeToLiveAttribute",
        "wait_for_replication_to_finish": "waitForReplicationToFinish",
        "write_capacity": "writeCapacity",
    },
)
class TableOptions(SchemaOptions):
    def __init__(
        self,
        *,
        partition_key: Attribute,
        sort_key: typing.Optional[Attribute] = None,
        billing_mode: typing.Optional[BillingMode] = None,
        contributor_insights_enabled: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[TableEncryption] = None,
        encryption_key: typing.Optional[_IKey_36930160] = None,
        point_in_time_recovery: typing.Optional[builtins.bool] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        replication_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        replication_timeout: typing.Optional[_Duration_070aa057] = None,
        server_side_encryption: typing.Optional[builtins.bool] = None,
        stream: typing.Optional[StreamViewType] = None,
        time_to_live_attribute: typing.Optional[builtins.str] = None,
        wait_for_replication_to_finish: typing.Optional[builtins.bool] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties of a DynamoDB Table.

        Use {@link TableProps} for all table properties

        :param partition_key: (experimental) Partition key attribute definition.
        :param sort_key: (experimental) Sort key attribute definition. Default: no sort key
        :param billing_mode: (experimental) Specify how you are charged for read and write throughput and how you manage capacity. Default: PROVISIONED if ``replicationRegions`` is not specified, PAY_PER_REQUEST otherwise
        :param contributor_insights_enabled: (experimental) Whether CloudWatch contributor insights is enabled. Default: false
        :param encryption: (experimental) Whether server-side encryption with an AWS managed customer master key is enabled. This property cannot be set if ``serverSideEncryption`` is set. Default: - server-side encryption is enabled with an AWS owned customer master key
        :param encryption_key: (experimental) External KMS key to use for table encryption. This property can only be set if ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED``. Default: - If ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED`` and this property is undefined, a new KMS key will be created and associated with this table.
        :param point_in_time_recovery: (experimental) Whether point-in-time recovery is enabled. Default: - point-in-time recovery is disabled
        :param read_capacity: (experimental) The read capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5
        :param removal_policy: (experimental) The removal policy to apply to the DynamoDB Table. Default: RemovalPolicy.RETAIN
        :param replication_regions: (experimental) Regions where replica tables will be created. Default: - no replica tables are created
        :param replication_timeout: (experimental) The timeout for a table replication operation in a single region. Default: Duration.minutes(30)
        :param server_side_encryption: (deprecated) Whether server-side encryption with an AWS managed customer master key is enabled. This property cannot be set if ``encryption`` and/or ``encryptionKey`` is set. Default: - server-side encryption is enabled with an AWS owned customer master key
        :param stream: (experimental) When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Default: - streams are disabled unless ``replicationRegions`` is specified
        :param time_to_live_attribute: (experimental) The name of TTL attribute. Default: - TTL is disabled
        :param wait_for_replication_to_finish: (experimental) Indicates whether CloudFormation stack waits for replication to finish. If set to false, the CloudFormation resource will mark the resource as created and replication will be completed asynchronously. This property is ignored if replicationRegions property is not set. DO NOT UNSET this property if adding/removing multiple replicationRegions in one deployment, as CloudFormation only supports one region replication at a time. CDK overcomes this limitation by waiting for replication to finish before starting new replicationRegion. Default: true
        :param write_capacity: (experimental) The write capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_dynamodb as dynamodb
            from monocdk import aws_kms as kms
            
            # duration is of type Duration
            # key is of type Key
            
            table_options = dynamodb.TableOptions(
                partition_key=dynamodb.Attribute(
                    name="name",
                    type=dynamodb.AttributeType.BINARY
                ),
            
                # the properties below are optional
                billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
                contributor_insights_enabled=False,
                encryption=dynamodb.TableEncryption.DEFAULT,
                encryption_key=key,
                point_in_time_recovery=False,
                read_capacity=123,
                removal_policy=monocdk.RemovalPolicy.DESTROY,
                replication_regions=["replicationRegions"],
                replication_timeout=duration,
                server_side_encryption=False,
                sort_key=dynamodb.Attribute(
                    name="name",
                    type=dynamodb.AttributeType.BINARY
                ),
                stream=dynamodb.StreamViewType.NEW_IMAGE,
                time_to_live_attribute="timeToLiveAttribute",
                wait_for_replication_to_finish=False,
                write_capacity=123
            )
        '''
        if isinstance(partition_key, dict):
            partition_key = Attribute(**partition_key)
        if isinstance(sort_key, dict):
            sort_key = Attribute(**sort_key)
        self._values: typing.Dict[str, typing.Any] = {
            "partition_key": partition_key,
        }
        if sort_key is not None:
            self._values["sort_key"] = sort_key
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if contributor_insights_enabled is not None:
            self._values["contributor_insights_enabled"] = contributor_insights_enabled
        if encryption is not None:
            self._values["encryption"] = encryption
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if read_capacity is not None:
            self._values["read_capacity"] = read_capacity
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if replication_regions is not None:
            self._values["replication_regions"] = replication_regions
        if replication_timeout is not None:
            self._values["replication_timeout"] = replication_timeout
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if stream is not None:
            self._values["stream"] = stream
        if time_to_live_attribute is not None:
            self._values["time_to_live_attribute"] = time_to_live_attribute
        if wait_for_replication_to_finish is not None:
            self._values["wait_for_replication_to_finish"] = wait_for_replication_to_finish
        if write_capacity is not None:
            self._values["write_capacity"] = write_capacity

    @builtins.property
    def partition_key(self) -> Attribute:
        '''(experimental) Partition key attribute definition.

        :stability: experimental
        '''
        result = self._values.get("partition_key")
        assert result is not None, "Required property 'partition_key' is missing"
        return typing.cast(Attribute, result)

    @builtins.property
    def sort_key(self) -> typing.Optional[Attribute]:
        '''(experimental) Sort key attribute definition.

        :default: no sort key

        :stability: experimental
        '''
        result = self._values.get("sort_key")
        return typing.cast(typing.Optional[Attribute], result)

    @builtins.property
    def billing_mode(self) -> typing.Optional[BillingMode]:
        '''(experimental) Specify how you are charged for read and write throughput and how you manage capacity.

        :default: PROVISIONED if ``replicationRegions`` is not specified, PAY_PER_REQUEST otherwise

        :stability: experimental
        '''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[BillingMode], result)

    @builtins.property
    def contributor_insights_enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether CloudWatch contributor insights is enabled.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("contributor_insights_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption(self) -> typing.Optional[TableEncryption]:
        '''(experimental) Whether server-side encryption with an AWS managed customer master key is enabled.

        This property cannot be set if ``serverSideEncryption`` is set.

        :default: - server-side encryption is enabled with an AWS owned customer master key

        :stability: experimental
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[TableEncryption], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_36930160]:
        '''(experimental) External KMS key to use for table encryption.

        This property can only be set if ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED``.

        :default:

        - If ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED`` and this
        property is undefined, a new KMS key will be created and associated with this table.

        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_36930160], result)

    @builtins.property
    def point_in_time_recovery(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether point-in-time recovery is enabled.

        :default: - point-in-time recovery is disabled

        :stability: experimental
        '''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The read capacity for the table.

        Careful if you add Global Secondary Indexes, as
        those will share the table's provisioned throughput.

        Can only be provided if billingMode is Provisioned.

        :default: 5

        :stability: experimental
        '''
        result = self._values.get("read_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_c97e7a20]:
        '''(experimental) The removal policy to apply to the DynamoDB Table.

        :default: RemovalPolicy.RETAIN

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_c97e7a20], result)

    @builtins.property
    def replication_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Regions where replica tables will be created.

        :default: - no replica tables are created

        :stability: experimental
        '''
        result = self._values.get("replication_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def replication_timeout(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The timeout for a table replication operation in a single region.

        :default: Duration.minutes(30)

        :stability: experimental
        '''
        result = self._values.get("replication_timeout")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def server_side_encryption(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether server-side encryption with an AWS managed customer master key is enabled.

        This property cannot be set if ``encryption`` and/or ``encryptionKey`` is set.

        :default: - server-side encryption is enabled with an AWS owned customer master key

        :deprecated:

        This property is deprecated. In order to obtain the same behavior as
        enabling this, set the ``encryption`` property to ``TableEncryption.AWS_MANAGED`` instead.

        :stability: deprecated
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def stream(self) -> typing.Optional[StreamViewType]:
        '''(experimental) When an item in the table is modified, StreamViewType determines what information is written to the stream for this table.

        :default: - streams are disabled unless ``replicationRegions`` is specified

        :stability: experimental
        '''
        result = self._values.get("stream")
        return typing.cast(typing.Optional[StreamViewType], result)

    @builtins.property
    def time_to_live_attribute(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of TTL attribute.

        :default: - TTL is disabled

        :stability: experimental
        '''
        result = self._values.get("time_to_live_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_replication_to_finish(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether CloudFormation stack waits for replication to finish.

        If set to false, the CloudFormation resource will mark the resource as
        created and replication will be completed asynchronously. This property is
        ignored if replicationRegions property is not set.

        DO NOT UNSET this property if adding/removing multiple replicationRegions
        in one deployment, as CloudFormation only supports one region replication
        at a time. CDK overcomes this limitation by waiting for replication to
        finish before starting new replicationRegion.

        :default: true

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-replicas
        :stability: experimental
        '''
        result = self._values.get("wait_for_replication_to_finish")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def write_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The write capacity for the table.

        Careful if you add Global Secondary Indexes, as
        those will share the table's provisioned throughput.

        Can only be provided if billingMode is Provisioned.

        :default: 5

        :stability: experimental
        '''
        result = self._values.get("write_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.TableProps",
    jsii_struct_bases=[TableOptions],
    name_mapping={
        "partition_key": "partitionKey",
        "sort_key": "sortKey",
        "billing_mode": "billingMode",
        "contributor_insights_enabled": "contributorInsightsEnabled",
        "encryption": "encryption",
        "encryption_key": "encryptionKey",
        "point_in_time_recovery": "pointInTimeRecovery",
        "read_capacity": "readCapacity",
        "removal_policy": "removalPolicy",
        "replication_regions": "replicationRegions",
        "replication_timeout": "replicationTimeout",
        "server_side_encryption": "serverSideEncryption",
        "stream": "stream",
        "time_to_live_attribute": "timeToLiveAttribute",
        "wait_for_replication_to_finish": "waitForReplicationToFinish",
        "write_capacity": "writeCapacity",
        "kinesis_stream": "kinesisStream",
        "table_name": "tableName",
    },
)
class TableProps(TableOptions):
    def __init__(
        self,
        *,
        partition_key: Attribute,
        sort_key: typing.Optional[Attribute] = None,
        billing_mode: typing.Optional[BillingMode] = None,
        contributor_insights_enabled: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[TableEncryption] = None,
        encryption_key: typing.Optional[_IKey_36930160] = None,
        point_in_time_recovery: typing.Optional[builtins.bool] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[_RemovalPolicy_c97e7a20] = None,
        replication_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        replication_timeout: typing.Optional[_Duration_070aa057] = None,
        server_side_encryption: typing.Optional[builtins.bool] = None,
        stream: typing.Optional[StreamViewType] = None,
        time_to_live_attribute: typing.Optional[builtins.str] = None,
        wait_for_replication_to_finish: typing.Optional[builtins.bool] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
        kinesis_stream: typing.Optional[_IStream_14c6ec7f] = None,
        table_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for a DynamoDB Table.

        :param partition_key: (experimental) Partition key attribute definition.
        :param sort_key: (experimental) Sort key attribute definition. Default: no sort key
        :param billing_mode: (experimental) Specify how you are charged for read and write throughput and how you manage capacity. Default: PROVISIONED if ``replicationRegions`` is not specified, PAY_PER_REQUEST otherwise
        :param contributor_insights_enabled: (experimental) Whether CloudWatch contributor insights is enabled. Default: false
        :param encryption: (experimental) Whether server-side encryption with an AWS managed customer master key is enabled. This property cannot be set if ``serverSideEncryption`` is set. Default: - server-side encryption is enabled with an AWS owned customer master key
        :param encryption_key: (experimental) External KMS key to use for table encryption. This property can only be set if ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED``. Default: - If ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED`` and this property is undefined, a new KMS key will be created and associated with this table.
        :param point_in_time_recovery: (experimental) Whether point-in-time recovery is enabled. Default: - point-in-time recovery is disabled
        :param read_capacity: (experimental) The read capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5
        :param removal_policy: (experimental) The removal policy to apply to the DynamoDB Table. Default: RemovalPolicy.RETAIN
        :param replication_regions: (experimental) Regions where replica tables will be created. Default: - no replica tables are created
        :param replication_timeout: (experimental) The timeout for a table replication operation in a single region. Default: Duration.minutes(30)
        :param server_side_encryption: (deprecated) Whether server-side encryption with an AWS managed customer master key is enabled. This property cannot be set if ``encryption`` and/or ``encryptionKey`` is set. Default: - server-side encryption is enabled with an AWS owned customer master key
        :param stream: (experimental) When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Default: - streams are disabled unless ``replicationRegions`` is specified
        :param time_to_live_attribute: (experimental) The name of TTL attribute. Default: - TTL is disabled
        :param wait_for_replication_to_finish: (experimental) Indicates whether CloudFormation stack waits for replication to finish. If set to false, the CloudFormation resource will mark the resource as created and replication will be completed asynchronously. This property is ignored if replicationRegions property is not set. DO NOT UNSET this property if adding/removing multiple replicationRegions in one deployment, as CloudFormation only supports one region replication at a time. CDK overcomes this limitation by waiting for replication to finish before starting new replicationRegion. Default: true
        :param write_capacity: (experimental) The write capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5
        :param kinesis_stream: (experimental) Kinesis Data Stream to capture item-level changes for the table. Default: - no Kinesis Data Stream
        :param table_name: (experimental) Enforces a particular physical table name. Default: 

        :stability: experimental

        Example::

            global_table = dynamodb.Table(self, "Table",
                partition_key=dynamodb.aws_dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
                replication_regions=["us-east-1", "us-east-2", "us-west-2"],
                billing_mode=dynamodb.BillingMode.PROVISIONED
            )
            
            global_table.auto_scale_write_capacity(
                min_capacity=1,
                max_capacity=10
            ).scale_on_utilization(target_utilization_percent=75)
        '''
        if isinstance(partition_key, dict):
            partition_key = Attribute(**partition_key)
        if isinstance(sort_key, dict):
            sort_key = Attribute(**sort_key)
        self._values: typing.Dict[str, typing.Any] = {
            "partition_key": partition_key,
        }
        if sort_key is not None:
            self._values["sort_key"] = sort_key
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if contributor_insights_enabled is not None:
            self._values["contributor_insights_enabled"] = contributor_insights_enabled
        if encryption is not None:
            self._values["encryption"] = encryption
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if read_capacity is not None:
            self._values["read_capacity"] = read_capacity
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if replication_regions is not None:
            self._values["replication_regions"] = replication_regions
        if replication_timeout is not None:
            self._values["replication_timeout"] = replication_timeout
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if stream is not None:
            self._values["stream"] = stream
        if time_to_live_attribute is not None:
            self._values["time_to_live_attribute"] = time_to_live_attribute
        if wait_for_replication_to_finish is not None:
            self._values["wait_for_replication_to_finish"] = wait_for_replication_to_finish
        if write_capacity is not None:
            self._values["write_capacity"] = write_capacity
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if table_name is not None:
            self._values["table_name"] = table_name

    @builtins.property
    def partition_key(self) -> Attribute:
        '''(experimental) Partition key attribute definition.

        :stability: experimental
        '''
        result = self._values.get("partition_key")
        assert result is not None, "Required property 'partition_key' is missing"
        return typing.cast(Attribute, result)

    @builtins.property
    def sort_key(self) -> typing.Optional[Attribute]:
        '''(experimental) Sort key attribute definition.

        :default: no sort key

        :stability: experimental
        '''
        result = self._values.get("sort_key")
        return typing.cast(typing.Optional[Attribute], result)

    @builtins.property
    def billing_mode(self) -> typing.Optional[BillingMode]:
        '''(experimental) Specify how you are charged for read and write throughput and how you manage capacity.

        :default: PROVISIONED if ``replicationRegions`` is not specified, PAY_PER_REQUEST otherwise

        :stability: experimental
        '''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[BillingMode], result)

    @builtins.property
    def contributor_insights_enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether CloudWatch contributor insights is enabled.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("contributor_insights_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption(self) -> typing.Optional[TableEncryption]:
        '''(experimental) Whether server-side encryption with an AWS managed customer master key is enabled.

        This property cannot be set if ``serverSideEncryption`` is set.

        :default: - server-side encryption is enabled with an AWS owned customer master key

        :stability: experimental
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[TableEncryption], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_36930160]:
        '''(experimental) External KMS key to use for table encryption.

        This property can only be set if ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED``.

        :default:

        - If ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED`` and this
        property is undefined, a new KMS key will be created and associated with this table.

        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_36930160], result)

    @builtins.property
    def point_in_time_recovery(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether point-in-time recovery is enabled.

        :default: - point-in-time recovery is disabled

        :stability: experimental
        '''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The read capacity for the table.

        Careful if you add Global Secondary Indexes, as
        those will share the table's provisioned throughput.

        Can only be provided if billingMode is Provisioned.

        :default: 5

        :stability: experimental
        '''
        result = self._values.get("read_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_c97e7a20]:
        '''(experimental) The removal policy to apply to the DynamoDB Table.

        :default: RemovalPolicy.RETAIN

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_c97e7a20], result)

    @builtins.property
    def replication_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Regions where replica tables will be created.

        :default: - no replica tables are created

        :stability: experimental
        '''
        result = self._values.get("replication_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def replication_timeout(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The timeout for a table replication operation in a single region.

        :default: Duration.minutes(30)

        :stability: experimental
        '''
        result = self._values.get("replication_timeout")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def server_side_encryption(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether server-side encryption with an AWS managed customer master key is enabled.

        This property cannot be set if ``encryption`` and/or ``encryptionKey`` is set.

        :default: - server-side encryption is enabled with an AWS owned customer master key

        :deprecated:

        This property is deprecated. In order to obtain the same behavior as
        enabling this, set the ``encryption`` property to ``TableEncryption.AWS_MANAGED`` instead.

        :stability: deprecated
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def stream(self) -> typing.Optional[StreamViewType]:
        '''(experimental) When an item in the table is modified, StreamViewType determines what information is written to the stream for this table.

        :default: - streams are disabled unless ``replicationRegions`` is specified

        :stability: experimental
        '''
        result = self._values.get("stream")
        return typing.cast(typing.Optional[StreamViewType], result)

    @builtins.property
    def time_to_live_attribute(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of TTL attribute.

        :default: - TTL is disabled

        :stability: experimental
        '''
        result = self._values.get("time_to_live_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_replication_to_finish(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether CloudFormation stack waits for replication to finish.

        If set to false, the CloudFormation resource will mark the resource as
        created and replication will be completed asynchronously. This property is
        ignored if replicationRegions property is not set.

        DO NOT UNSET this property if adding/removing multiple replicationRegions
        in one deployment, as CloudFormation only supports one region replication
        at a time. CDK overcomes this limitation by waiting for replication to
        finish before starting new replicationRegion.

        :default: true

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-replicas
        :stability: experimental
        '''
        result = self._values.get("wait_for_replication_to_finish")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def write_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The write capacity for the table.

        Careful if you add Global Secondary Indexes, as
        those will share the table's provisioned throughput.

        Can only be provided if billingMode is Provisioned.

        :default: 5

        :stability: experimental
        '''
        result = self._values.get("write_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kinesis_stream(self) -> typing.Optional[_IStream_14c6ec7f]:
        '''(experimental) Kinesis Data Stream to capture item-level changes for the table.

        :default: - no Kinesis Data Stream

        :stability: experimental
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional[_IStream_14c6ec7f], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Enforces a particular physical table name.

        :default:

        :stability: experimental
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.UtilizationScalingProps",
    jsii_struct_bases=[_BaseTargetTrackingProps_e4402570],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "target_utilization_percent": "targetUtilizationPercent",
    },
)
class UtilizationScalingProps(_BaseTargetTrackingProps_e4402570):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
        target_utilization_percent: jsii.Number,
    ) -> None:
        '''(experimental) Properties for enabling DynamoDB utilization tracking.

        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param target_utilization_percent: (experimental) Target utilization percentage for the attribute.

        :stability: experimental

        Example::

            import monocdk as dynamodb
            
            # table is of type Table
            
            
            read_capacity = table.auto_scale_read_capacity(
                min_capacity=10,
                max_capacity=1000
            )
            read_capacity.scale_on_utilization(
                target_utilization_percent=60
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "target_utilization_percent": target_utilization_percent,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the scaling policy.

        :default: - Automatically generated name.

        :stability: experimental
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def target_utilization_percent(self) -> jsii.Number:
        '''(experimental) Target utilization percentage for the attribute.

        :stability: experimental
        '''
        result = self._values.get("target_utilization_percent")
        assert result is not None, "Required property 'target_utilization_percent' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UtilizationScalingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.GlobalSecondaryIndexProps",
    jsii_struct_bases=[SecondaryIndexProps, SchemaOptions],
    name_mapping={
        "index_name": "indexName",
        "non_key_attributes": "nonKeyAttributes",
        "projection_type": "projectionType",
        "partition_key": "partitionKey",
        "sort_key": "sortKey",
        "read_capacity": "readCapacity",
        "write_capacity": "writeCapacity",
    },
)
class GlobalSecondaryIndexProps(SecondaryIndexProps, SchemaOptions):
    def __init__(
        self,
        *,
        index_name: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        projection_type: typing.Optional[ProjectionType] = None,
        partition_key: Attribute,
        sort_key: typing.Optional[Attribute] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties for a global secondary index.

        :param index_name: (experimental) The name of the secondary index.
        :param non_key_attributes: (experimental) The non-key attributes that are projected into the secondary index. Default: - No additional attributes
        :param projection_type: (experimental) The set of attributes that are projected into the secondary index. Default: ALL
        :param partition_key: (experimental) Partition key attribute definition.
        :param sort_key: (experimental) Sort key attribute definition. Default: no sort key
        :param read_capacity: (experimental) The read capacity for the global secondary index. Can only be provided if table billingMode is Provisioned or undefined. Default: 5
        :param write_capacity: (experimental) The write capacity for the global secondary index. Can only be provided if table billingMode is Provisioned or undefined. Default: 5

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dynamodb as dynamodb
            
            global_secondary_index_props = dynamodb.GlobalSecondaryIndexProps(
                index_name="indexName",
                partition_key=dynamodb.Attribute(
                    name="name",
                    type=dynamodb.AttributeType.BINARY
                ),
            
                # the properties below are optional
                non_key_attributes=["nonKeyAttributes"],
                projection_type=dynamodb.ProjectionType.KEYS_ONLY,
                read_capacity=123,
                sort_key=dynamodb.Attribute(
                    name="name",
                    type=dynamodb.AttributeType.BINARY
                ),
                write_capacity=123
            )
        '''
        if isinstance(partition_key, dict):
            partition_key = Attribute(**partition_key)
        if isinstance(sort_key, dict):
            sort_key = Attribute(**sort_key)
        self._values: typing.Dict[str, typing.Any] = {
            "index_name": index_name,
            "partition_key": partition_key,
        }
        if non_key_attributes is not None:
            self._values["non_key_attributes"] = non_key_attributes
        if projection_type is not None:
            self._values["projection_type"] = projection_type
        if sort_key is not None:
            self._values["sort_key"] = sort_key
        if read_capacity is not None:
            self._values["read_capacity"] = read_capacity
        if write_capacity is not None:
            self._values["write_capacity"] = write_capacity

    @builtins.property
    def index_name(self) -> builtins.str:
        '''(experimental) The name of the secondary index.

        :stability: experimental
        '''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The non-key attributes that are projected into the secondary index.

        :default: - No additional attributes

        :stability: experimental
        '''
        result = self._values.get("non_key_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def projection_type(self) -> typing.Optional[ProjectionType]:
        '''(experimental) The set of attributes that are projected into the secondary index.

        :default: ALL

        :stability: experimental
        '''
        result = self._values.get("projection_type")
        return typing.cast(typing.Optional[ProjectionType], result)

    @builtins.property
    def partition_key(self) -> Attribute:
        '''(experimental) Partition key attribute definition.

        :stability: experimental
        '''
        result = self._values.get("partition_key")
        assert result is not None, "Required property 'partition_key' is missing"
        return typing.cast(Attribute, result)

    @builtins.property
    def sort_key(self) -> typing.Optional[Attribute]:
        '''(experimental) Sort key attribute definition.

        :default: no sort key

        :stability: experimental
        '''
        result = self._values.get("sort_key")
        return typing.cast(typing.Optional[Attribute], result)

    @builtins.property
    def read_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The read capacity for the global secondary index.

        Can only be provided if table billingMode is Provisioned or undefined.

        :default: 5

        :stability: experimental
        '''
        result = self._values.get("read_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def write_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The write capacity for the global secondary index.

        Can only be provided if table billingMode is Provisioned or undefined.

        :default: 5

        :stability: experimental
        '''
        result = self._values.get("write_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlobalSecondaryIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_dynamodb.LocalSecondaryIndexProps",
    jsii_struct_bases=[SecondaryIndexProps],
    name_mapping={
        "index_name": "indexName",
        "non_key_attributes": "nonKeyAttributes",
        "projection_type": "projectionType",
        "sort_key": "sortKey",
    },
)
class LocalSecondaryIndexProps(SecondaryIndexProps):
    def __init__(
        self,
        *,
        index_name: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        projection_type: typing.Optional[ProjectionType] = None,
        sort_key: Attribute,
    ) -> None:
        '''(experimental) Properties for a local secondary index.

        :param index_name: (experimental) The name of the secondary index.
        :param non_key_attributes: (experimental) The non-key attributes that are projected into the secondary index. Default: - No additional attributes
        :param projection_type: (experimental) The set of attributes that are projected into the secondary index. Default: ALL
        :param sort_key: (experimental) The attribute of a sort key for the local secondary index.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dynamodb as dynamodb
            
            local_secondary_index_props = dynamodb.LocalSecondaryIndexProps(
                index_name="indexName",
                sort_key=dynamodb.Attribute(
                    name="name",
                    type=dynamodb.AttributeType.BINARY
                ),
            
                # the properties below are optional
                non_key_attributes=["nonKeyAttributes"],
                projection_type=dynamodb.ProjectionType.KEYS_ONLY
            )
        '''
        if isinstance(sort_key, dict):
            sort_key = Attribute(**sort_key)
        self._values: typing.Dict[str, typing.Any] = {
            "index_name": index_name,
            "sort_key": sort_key,
        }
        if non_key_attributes is not None:
            self._values["non_key_attributes"] = non_key_attributes
        if projection_type is not None:
            self._values["projection_type"] = projection_type

    @builtins.property
    def index_name(self) -> builtins.str:
        '''(experimental) The name of the secondary index.

        :stability: experimental
        '''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The non-key attributes that are projected into the secondary index.

        :default: - No additional attributes

        :stability: experimental
        '''
        result = self._values.get("non_key_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def projection_type(self) -> typing.Optional[ProjectionType]:
        '''(experimental) The set of attributes that are projected into the secondary index.

        :default: ALL

        :stability: experimental
        '''
        result = self._values.get("projection_type")
        return typing.cast(typing.Optional[ProjectionType], result)

    @builtins.property
    def sort_key(self) -> Attribute:
        '''(experimental) The attribute of a sort key for the local secondary index.

        :stability: experimental
        '''
        result = self._values.get("sort_key")
        assert result is not None, "Required property 'sort_key' is missing"
        return typing.cast(Attribute, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalSecondaryIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Attribute",
    "AttributeType",
    "BillingMode",
    "CfnGlobalTable",
    "CfnGlobalTableProps",
    "CfnTable",
    "CfnTableProps",
    "EnableScalingProps",
    "GlobalSecondaryIndexProps",
    "IScalableTableAttribute",
    "ITable",
    "LocalSecondaryIndexProps",
    "Operation",
    "ProjectionType",
    "SchemaOptions",
    "SecondaryIndexProps",
    "StreamViewType",
    "SystemErrorsForOperationsMetricOptions",
    "Table",
    "TableAttributes",
    "TableEncryption",
    "TableOptions",
    "TableProps",
    "UtilizationScalingProps",
]

publication.publish()
