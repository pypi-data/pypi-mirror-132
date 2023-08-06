'''
# AWS::LookoutEquipment Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as lookoutequipment
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LookoutEquipment](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LookoutEquipment.html).

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

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnInferenceScheduler(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lookoutequipment.CfnInferenceScheduler",
):
    '''A CloudFormation ``AWS::LookoutEquipment::InferenceScheduler``.

    :cloudformationResource: AWS::LookoutEquipment::InferenceScheduler
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_lookoutequipment as lookoutequipment
        
        # data_input_configuration is of type object
        # data_output_configuration is of type object
        
        cfn_inference_scheduler = lookoutequipment.CfnInferenceScheduler(self, "MyCfnInferenceScheduler",
            data_input_configuration=data_input_configuration,
            data_output_configuration=data_output_configuration,
            data_upload_frequency="dataUploadFrequency",
            model_name="modelName",
            role_arn="roleArn",
        
            # the properties below are optional
            data_delay_offset_in_minutes=123,
            inference_scheduler_name="inferenceSchedulerName",
            server_side_kms_key_id="serverSideKmsKeyId",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        data_delay_offset_in_minutes: typing.Optional[jsii.Number] = None,
        data_input_configuration: typing.Any,
        data_output_configuration: typing.Any,
        data_upload_frequency: builtins.str,
        inference_scheduler_name: typing.Optional[builtins.str] = None,
        model_name: builtins.str,
        role_arn: builtins.str,
        server_side_kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Create a new ``AWS::LookoutEquipment::InferenceScheduler``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_delay_offset_in_minutes: ``AWS::LookoutEquipment::InferenceScheduler.DataDelayOffsetInMinutes``.
        :param data_input_configuration: ``AWS::LookoutEquipment::InferenceScheduler.DataInputConfiguration``.
        :param data_output_configuration: ``AWS::LookoutEquipment::InferenceScheduler.DataOutputConfiguration``.
        :param data_upload_frequency: ``AWS::LookoutEquipment::InferenceScheduler.DataUploadFrequency``.
        :param inference_scheduler_name: ``AWS::LookoutEquipment::InferenceScheduler.InferenceSchedulerName``.
        :param model_name: ``AWS::LookoutEquipment::InferenceScheduler.ModelName``.
        :param role_arn: ``AWS::LookoutEquipment::InferenceScheduler.RoleArn``.
        :param server_side_kms_key_id: ``AWS::LookoutEquipment::InferenceScheduler.ServerSideKmsKeyId``.
        :param tags: ``AWS::LookoutEquipment::InferenceScheduler.Tags``.
        '''
        props = CfnInferenceSchedulerProps(
            data_delay_offset_in_minutes=data_delay_offset_in_minutes,
            data_input_configuration=data_input_configuration,
            data_output_configuration=data_output_configuration,
            data_upload_frequency=data_upload_frequency,
            inference_scheduler_name=inference_scheduler_name,
            model_name=model_name,
            role_arn=role_arn,
            server_side_kms_key_id=server_side_kms_key_id,
            tags=tags,
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
    @jsii.member(jsii_name="attrInferenceSchedulerArn")
    def attr_inference_scheduler_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: InferenceSchedulerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInferenceSchedulerArn"))

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
    @jsii.member(jsii_name="dataDelayOffsetInMinutes")
    def data_delay_offset_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataDelayOffsetInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataDelayOffsetInMinutes"))

    @data_delay_offset_in_minutes.setter
    def data_delay_offset_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "dataDelayOffsetInMinutes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataInputConfiguration")
    def data_input_configuration(self) -> typing.Any:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataInputConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration
        '''
        return typing.cast(typing.Any, jsii.get(self, "dataInputConfiguration"))

    @data_input_configuration.setter
    def data_input_configuration(self, value: typing.Any) -> None:
        jsii.set(self, "dataInputConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataOutputConfiguration")
    def data_output_configuration(self) -> typing.Any:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataOutputConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration
        '''
        return typing.cast(typing.Any, jsii.get(self, "dataOutputConfiguration"))

    @data_output_configuration.setter
    def data_output_configuration(self, value: typing.Any) -> None:
        jsii.set(self, "dataOutputConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataUploadFrequency")
    def data_upload_frequency(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataUploadFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datauploadfrequency
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataUploadFrequency"))

    @data_upload_frequency.setter
    def data_upload_frequency(self, value: builtins.str) -> None:
        jsii.set(self, "dataUploadFrequency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inferenceSchedulerName")
    def inference_scheduler_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutEquipment::InferenceScheduler.InferenceSchedulerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-inferenceschedulername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inferenceSchedulerName"))

    @inference_scheduler_name.setter
    def inference_scheduler_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "inferenceSchedulerName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.ModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-modelname
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: builtins.str) -> None:
        jsii.set(self, "modelName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverSideKmsKeyId")
    def server_side_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutEquipment::InferenceScheduler.ServerSideKmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSideKmsKeyId"))

    @server_side_kms_key_id.setter
    def server_side_kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serverSideKmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::LookoutEquipment::InferenceScheduler.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="monocdk.aws_lookoutequipment.CfnInferenceSchedulerProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_delay_offset_in_minutes": "dataDelayOffsetInMinutes",
        "data_input_configuration": "dataInputConfiguration",
        "data_output_configuration": "dataOutputConfiguration",
        "data_upload_frequency": "dataUploadFrequency",
        "inference_scheduler_name": "inferenceSchedulerName",
        "model_name": "modelName",
        "role_arn": "roleArn",
        "server_side_kms_key_id": "serverSideKmsKeyId",
        "tags": "tags",
    },
)
class CfnInferenceSchedulerProps:
    def __init__(
        self,
        *,
        data_delay_offset_in_minutes: typing.Optional[jsii.Number] = None,
        data_input_configuration: typing.Any,
        data_output_configuration: typing.Any,
        data_upload_frequency: builtins.str,
        inference_scheduler_name: typing.Optional[builtins.str] = None,
        model_name: builtins.str,
        role_arn: builtins.str,
        server_side_kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::LookoutEquipment::InferenceScheduler``.

        :param data_delay_offset_in_minutes: ``AWS::LookoutEquipment::InferenceScheduler.DataDelayOffsetInMinutes``.
        :param data_input_configuration: ``AWS::LookoutEquipment::InferenceScheduler.DataInputConfiguration``.
        :param data_output_configuration: ``AWS::LookoutEquipment::InferenceScheduler.DataOutputConfiguration``.
        :param data_upload_frequency: ``AWS::LookoutEquipment::InferenceScheduler.DataUploadFrequency``.
        :param inference_scheduler_name: ``AWS::LookoutEquipment::InferenceScheduler.InferenceSchedulerName``.
        :param model_name: ``AWS::LookoutEquipment::InferenceScheduler.ModelName``.
        :param role_arn: ``AWS::LookoutEquipment::InferenceScheduler.RoleArn``.
        :param server_side_kms_key_id: ``AWS::LookoutEquipment::InferenceScheduler.ServerSideKmsKeyId``.
        :param tags: ``AWS::LookoutEquipment::InferenceScheduler.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_lookoutequipment as lookoutequipment
            
            # data_input_configuration is of type object
            # data_output_configuration is of type object
            
            cfn_inference_scheduler_props = lookoutequipment.CfnInferenceSchedulerProps(
                data_input_configuration=data_input_configuration,
                data_output_configuration=data_output_configuration,
                data_upload_frequency="dataUploadFrequency",
                model_name="modelName",
                role_arn="roleArn",
            
                # the properties below are optional
                data_delay_offset_in_minutes=123,
                inference_scheduler_name="inferenceSchedulerName",
                server_side_kms_key_id="serverSideKmsKeyId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_input_configuration": data_input_configuration,
            "data_output_configuration": data_output_configuration,
            "data_upload_frequency": data_upload_frequency,
            "model_name": model_name,
            "role_arn": role_arn,
        }
        if data_delay_offset_in_minutes is not None:
            self._values["data_delay_offset_in_minutes"] = data_delay_offset_in_minutes
        if inference_scheduler_name is not None:
            self._values["inference_scheduler_name"] = inference_scheduler_name
        if server_side_kms_key_id is not None:
            self._values["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_delay_offset_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataDelayOffsetInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes
        '''
        result = self._values.get("data_delay_offset_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_input_configuration(self) -> typing.Any:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataInputConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration
        '''
        result = self._values.get("data_input_configuration")
        assert result is not None, "Required property 'data_input_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def data_output_configuration(self) -> typing.Any:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataOutputConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration
        '''
        result = self._values.get("data_output_configuration")
        assert result is not None, "Required property 'data_output_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def data_upload_frequency(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.DataUploadFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datauploadfrequency
        '''
        result = self._values.get("data_upload_frequency")
        assert result is not None, "Required property 'data_upload_frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def inference_scheduler_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutEquipment::InferenceScheduler.InferenceSchedulerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-inferenceschedulername
        '''
        result = self._values.get("inference_scheduler_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_name(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.ModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-modelname
        '''
        result = self._values.get("model_name")
        assert result is not None, "Required property 'model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::LookoutEquipment::InferenceScheduler.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_side_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutEquipment::InferenceScheduler.ServerSideKmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid
        '''
        result = self._values.get("server_side_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::LookoutEquipment::InferenceScheduler.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInferenceSchedulerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnInferenceScheduler",
    "CfnInferenceSchedulerProps",
]

publication.publish()
