'''
# AWS::Connect Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as connect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Connect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Connect.html).

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
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnContactFlow(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_connect.CfnContactFlow",
):
    '''A CloudFormation ``AWS::Connect::ContactFlow``.

    :cloudformationResource: AWS::Connect::ContactFlow
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_connect as connect
        
        cfn_contact_flow = connect.CfnContactFlow(self, "MyCfnContactFlow",
            content="content",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            description="description",
            state="state",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        content: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_arn: builtins.str,
        name: builtins.str,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::ContactFlow``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: ``AWS::Connect::ContactFlow.Content``.
        :param description: ``AWS::Connect::ContactFlow.Description``.
        :param instance_arn: ``AWS::Connect::ContactFlow.InstanceArn``.
        :param name: ``AWS::Connect::ContactFlow.Name``.
        :param state: ``AWS::Connect::ContactFlow.State``.
        :param tags: ``AWS::Connect::ContactFlow.Tags``.
        :param type: ``AWS::Connect::ContactFlow.Type``.
        '''
        props = CfnContactFlowProps(
            content=content,
            description=description,
            instance_arn=instance_arn,
            name=name,
            state=state,
            tags=tags,
            type=type,
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
    @jsii.member(jsii_name="attrContactFlowArn")
    def attr_contact_flow_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ContactFlowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContactFlowArn"))

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
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''``AWS::Connect::ContactFlow.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-content
        '''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlow.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::ContactFlow.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Connect::ContactFlow.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlow.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "state", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::Connect::ContactFlow.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlow.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)


@jsii.implements(_IInspectable_82c04a63)
class CfnContactFlowModule(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_connect.CfnContactFlowModule",
):
    '''A CloudFormation ``AWS::Connect::ContactFlowModule``.

    :cloudformationResource: AWS::Connect::ContactFlowModule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_connect as connect
        
        cfn_contact_flow_module = connect.CfnContactFlowModule(self, "MyCfnContactFlowModule",
            content="content",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            description="description",
            state="state",
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
        content: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_arn: builtins.str,
        name: builtins.str,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::ContactFlowModule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: ``AWS::Connect::ContactFlowModule.Content``.
        :param description: ``AWS::Connect::ContactFlowModule.Description``.
        :param instance_arn: ``AWS::Connect::ContactFlowModule.InstanceArn``.
        :param name: ``AWS::Connect::ContactFlowModule.Name``.
        :param state: ``AWS::Connect::ContactFlowModule.State``.
        :param tags: ``AWS::Connect::ContactFlowModule.Tags``.
        '''
        props = CfnContactFlowModuleProps(
            content=content,
            description=description,
            instance_arn=instance_arn,
            name=name,
            state=state,
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
    @jsii.member(jsii_name="attrContactFlowModuleArn")
    def attr_contact_flow_module_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ContactFlowModuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContactFlowModuleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''``AWS::Connect::ContactFlowModule.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-content
        '''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlowModule.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::ContactFlowModule.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Connect::ContactFlowModule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlowModule.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "state", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::Connect::ContactFlowModule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="monocdk.aws_connect.CfnContactFlowModuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "description": "description",
        "instance_arn": "instanceArn",
        "name": "name",
        "state": "state",
        "tags": "tags",
    },
)
class CfnContactFlowModuleProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_arn: builtins.str,
        name: builtins.str,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Connect::ContactFlowModule``.

        :param content: ``AWS::Connect::ContactFlowModule.Content``.
        :param description: ``AWS::Connect::ContactFlowModule.Description``.
        :param instance_arn: ``AWS::Connect::ContactFlowModule.InstanceArn``.
        :param name: ``AWS::Connect::ContactFlowModule.Name``.
        :param state: ``AWS::Connect::ContactFlowModule.State``.
        :param tags: ``AWS::Connect::ContactFlowModule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_connect as connect
            
            cfn_contact_flow_module_props = connect.CfnContactFlowModuleProps(
                content="content",
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                description="description",
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(self) -> builtins.str:
        '''``AWS::Connect::ContactFlowModule.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlowModule.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::ContactFlowModule.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Connect::ContactFlowModule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlowModule.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::Connect::ContactFlowModule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactFlowModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_connect.CfnContactFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "description": "description",
        "instance_arn": "instanceArn",
        "name": "name",
        "state": "state",
        "tags": "tags",
        "type": "type",
    },
)
class CfnContactFlowProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_arn: builtins.str,
        name: builtins.str,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Connect::ContactFlow``.

        :param content: ``AWS::Connect::ContactFlow.Content``.
        :param description: ``AWS::Connect::ContactFlow.Description``.
        :param instance_arn: ``AWS::Connect::ContactFlow.InstanceArn``.
        :param name: ``AWS::Connect::ContactFlow.Name``.
        :param state: ``AWS::Connect::ContactFlow.State``.
        :param tags: ``AWS::Connect::ContactFlow.Tags``.
        :param type: ``AWS::Connect::ContactFlow.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_connect as connect
            
            cfn_contact_flow_props = connect.CfnContactFlowProps(
                content="content",
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                description="description",
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def content(self) -> builtins.str:
        '''``AWS::Connect::ContactFlow.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlow.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::ContactFlow.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Connect::ContactFlow.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlow.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::Connect::ContactFlow.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::ContactFlow.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnHoursOfOperation(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_connect.CfnHoursOfOperation",
):
    '''A CloudFormation ``AWS::Connect::HoursOfOperation``.

    :cloudformationResource: AWS::Connect::HoursOfOperation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_connect as connect
        
        cfn_hours_of_operation = connect.CfnHoursOfOperation(self, "MyCfnHoursOfOperation",
            config=[connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                day="day",
                end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                ),
                start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                )
            )],
            instance_arn="instanceArn",
            name="name",
            time_zone="timeZone",
        
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
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        config: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", _IResolvable_a771d0ef]]],
        description: typing.Optional[builtins.str] = None,
        instance_arn: builtins.str,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        time_zone: builtins.str,
    ) -> None:
        '''Create a new ``AWS::Connect::HoursOfOperation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param config: ``AWS::Connect::HoursOfOperation.Config``.
        :param description: ``AWS::Connect::HoursOfOperation.Description``.
        :param instance_arn: ``AWS::Connect::HoursOfOperation.InstanceArn``.
        :param name: ``AWS::Connect::HoursOfOperation.Name``.
        :param tags: ``AWS::Connect::HoursOfOperation.Tags``.
        :param time_zone: ``AWS::Connect::HoursOfOperation.TimeZone``.
        '''
        props = CfnHoursOfOperationProps(
            config=config,
            description=description,
            instance_arn=instance_arn,
            name=name,
            tags=tags,
            time_zone=time_zone,
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
    @jsii.member(jsii_name="attrHoursOfOperationArn")
    def attr_hours_of_operation_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: HoursOfOperationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHoursOfOperationArn"))

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
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", _IResolvable_a771d0ef]]]:
        '''``AWS::Connect::HoursOfOperation.Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-config
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", _IResolvable_a771d0ef]]], jsii.get(self, "config"))

    @config.setter
    def config(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        jsii.set(self, "config", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::HoursOfOperation.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::HoursOfOperation.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Connect::HoursOfOperation.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::Connect::HoursOfOperation.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        '''``AWS::Connect::HoursOfOperation.TimeZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-timezone
        '''
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        jsii.set(self, "timeZone", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_connect.CfnHoursOfOperation.HoursOfOperationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"day": "day", "end_time": "endTime", "start_time": "startTime"},
    )
    class HoursOfOperationConfigProperty:
        def __init__(
            self,
            *,
            day: builtins.str,
            end_time: typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_a771d0ef],
            start_time: typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param day: ``CfnHoursOfOperation.HoursOfOperationConfigProperty.Day``.
            :param end_time: ``CfnHoursOfOperation.HoursOfOperationConfigProperty.EndTime``.
            :param start_time: ``CfnHoursOfOperation.HoursOfOperationConfigProperty.StartTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_connect as connect
                
                hours_of_operation_config_property = connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                    day="day",
                    end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    ),
                    start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "day": day,
                "end_time": end_time,
                "start_time": start_time,
            }

        @builtins.property
        def day(self) -> builtins.str:
            '''``CfnHoursOfOperation.HoursOfOperationConfigProperty.Day``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-day
            '''
            result = self._values.get("day")
            assert result is not None, "Required property 'day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time(
            self,
        ) -> typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_a771d0ef]:
            '''``CfnHoursOfOperation.HoursOfOperationConfigProperty.EndTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_a771d0ef]:
            '''``CfnHoursOfOperation.HoursOfOperationConfigProperty.StartTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HoursOfOperationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty",
        jsii_struct_bases=[],
        name_mapping={"hours": "hours", "minutes": "minutes"},
    )
    class HoursOfOperationTimeSliceProperty:
        def __init__(self, *, hours: jsii.Number, minutes: jsii.Number) -> None:
            '''
            :param hours: ``CfnHoursOfOperation.HoursOfOperationTimeSliceProperty.Hours``.
            :param minutes: ``CfnHoursOfOperation.HoursOfOperationTimeSliceProperty.Minutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_connect as connect
                
                hours_of_operation_time_slice_property = connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "hours": hours,
                "minutes": minutes,
            }

        @builtins.property
        def hours(self) -> jsii.Number:
            '''``CfnHoursOfOperation.HoursOfOperationTimeSliceProperty.Hours``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html#cfn-connect-hoursofoperation-hoursofoperationtimeslice-hours
            '''
            result = self._values.get("hours")
            assert result is not None, "Required property 'hours' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def minutes(self) -> jsii.Number:
            '''``CfnHoursOfOperation.HoursOfOperationTimeSliceProperty.Minutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html#cfn-connect-hoursofoperation-hoursofoperationtimeslice-minutes
            '''
            result = self._values.get("minutes")
            assert result is not None, "Required property 'minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HoursOfOperationTimeSliceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_connect.CfnHoursOfOperationProps",
    jsii_struct_bases=[],
    name_mapping={
        "config": "config",
        "description": "description",
        "instance_arn": "instanceArn",
        "name": "name",
        "tags": "tags",
        "time_zone": "timeZone",
    },
)
class CfnHoursOfOperationProps:
    def __init__(
        self,
        *,
        config: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, _IResolvable_a771d0ef]]],
        description: typing.Optional[builtins.str] = None,
        instance_arn: builtins.str,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        time_zone: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::Connect::HoursOfOperation``.

        :param config: ``AWS::Connect::HoursOfOperation.Config``.
        :param description: ``AWS::Connect::HoursOfOperation.Description``.
        :param instance_arn: ``AWS::Connect::HoursOfOperation.InstanceArn``.
        :param name: ``AWS::Connect::HoursOfOperation.Name``.
        :param tags: ``AWS::Connect::HoursOfOperation.Tags``.
        :param time_zone: ``AWS::Connect::HoursOfOperation.TimeZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_connect as connect
            
            cfn_hours_of_operation_props = connect.CfnHoursOfOperationProps(
                config=[connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                    day="day",
                    end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    ),
                    start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    )
                )],
                instance_arn="instanceArn",
                name="name",
                time_zone="timeZone",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "config": config,
            "instance_arn": instance_arn,
            "name": name,
            "time_zone": time_zone,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def config(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, _IResolvable_a771d0ef]]]:
        '''``AWS::Connect::HoursOfOperation.Config``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-config
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, _IResolvable_a771d0ef]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::HoursOfOperation.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::HoursOfOperation.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Connect::HoursOfOperation.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::Connect::HoursOfOperation.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def time_zone(self) -> builtins.str:
        '''``AWS::Connect::HoursOfOperation.TimeZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-timezone
        '''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHoursOfOperationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnQuickConnect(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_connect.CfnQuickConnect",
):
    '''A CloudFormation ``AWS::Connect::QuickConnect``.

    :cloudformationResource: AWS::Connect::QuickConnect
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_connect as connect
        
        cfn_quick_connect = connect.CfnQuickConnect(self, "MyCfnQuickConnect",
            instance_arn="instanceArn",
            name="name",
            quick_connect_config=connect.CfnQuickConnect.QuickConnectConfigProperty(
                quick_connect_type="quickConnectType",
        
                # the properties below are optional
                phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                    phone_number="phoneNumber"
                ),
                queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    queue_arn="queueArn"
                ),
                user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    user_arn="userArn"
                )
            ),
        
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
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        instance_arn: builtins.str,
        name: builtins.str,
        quick_connect_config: typing.Union["CfnQuickConnect.QuickConnectConfigProperty", _IResolvable_a771d0ef],
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::QuickConnect``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::Connect::QuickConnect.Description``.
        :param instance_arn: ``AWS::Connect::QuickConnect.InstanceArn``.
        :param name: ``AWS::Connect::QuickConnect.Name``.
        :param quick_connect_config: ``AWS::Connect::QuickConnect.QuickConnectConfig``.
        :param tags: ``AWS::Connect::QuickConnect.Tags``.
        '''
        props = CfnQuickConnectProps(
            description=description,
            instance_arn=instance_arn,
            name=name,
            quick_connect_config=quick_connect_config,
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
    @jsii.member(jsii_name="attrQuickConnectArn")
    def attr_quick_connect_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: QuickConnectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQuickConnectArn"))

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
        '''``AWS::Connect::QuickConnect.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::QuickConnect.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Connect::QuickConnect.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quickConnectConfig")
    def quick_connect_config(
        self,
    ) -> typing.Union["CfnQuickConnect.QuickConnectConfigProperty", _IResolvable_a771d0ef]:
        '''``AWS::Connect::QuickConnect.QuickConnectConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-quickconnectconfig
        '''
        return typing.cast(typing.Union["CfnQuickConnect.QuickConnectConfigProperty", _IResolvable_a771d0ef], jsii.get(self, "quickConnectConfig"))

    @quick_connect_config.setter
    def quick_connect_config(
        self,
        value: typing.Union["CfnQuickConnect.QuickConnectConfigProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "quickConnectConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::Connect::QuickConnect.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="monocdk.aws_connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"phone_number": "phoneNumber"},
    )
    class PhoneNumberQuickConnectConfigProperty:
        def __init__(self, *, phone_number: builtins.str) -> None:
            '''
            :param phone_number: ``CfnQuickConnect.PhoneNumberQuickConnectConfigProperty.PhoneNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_connect as connect
                
                phone_number_quick_connect_config_property = connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                    phone_number="phoneNumber"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "phone_number": phone_number,
            }

        @builtins.property
        def phone_number(self) -> builtins.str:
            '''``CfnQuickConnect.PhoneNumberQuickConnectConfigProperty.PhoneNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html#cfn-connect-quickconnect-phonenumberquickconnectconfig-phonenumber
            '''
            result = self._values.get("phone_number")
            assert result is not None, "Required property 'phone_number' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhoneNumberQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_connect.CfnQuickConnect.QueueQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_flow_arn": "contactFlowArn", "queue_arn": "queueArn"},
    )
    class QueueQuickConnectConfigProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            queue_arn: builtins.str,
        ) -> None:
            '''
            :param contact_flow_arn: ``CfnQuickConnect.QueueQuickConnectConfigProperty.ContactFlowArn``.
            :param queue_arn: ``CfnQuickConnect.QueueQuickConnectConfigProperty.QueueArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_connect as connect
                
                queue_quick_connect_config_property = connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    queue_arn="queueArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "queue_arn": queue_arn,
            }

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''``CfnQuickConnect.QueueQuickConnectConfigProperty.ContactFlowArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def queue_arn(self) -> builtins.str:
            '''``CfnQuickConnect.QueueQuickConnectConfigProperty.QueueArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-queuearn
            '''
            result = self._values.get("queue_arn")
            assert result is not None, "Required property 'queue_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueueQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_connect.CfnQuickConnect.QuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "phone_config": "phoneConfig",
            "queue_config": "queueConfig",
            "quick_connect_type": "quickConnectType",
            "user_config": "userConfig",
        },
    )
    class QuickConnectConfigProperty:
        def __init__(
            self,
            *,
            phone_config: typing.Optional[typing.Union["CfnQuickConnect.PhoneNumberQuickConnectConfigProperty", _IResolvable_a771d0ef]] = None,
            queue_config: typing.Optional[typing.Union["CfnQuickConnect.QueueQuickConnectConfigProperty", _IResolvable_a771d0ef]] = None,
            quick_connect_type: builtins.str,
            user_config: typing.Optional[typing.Union["CfnQuickConnect.UserQuickConnectConfigProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param phone_config: ``CfnQuickConnect.QuickConnectConfigProperty.PhoneConfig``.
            :param queue_config: ``CfnQuickConnect.QuickConnectConfigProperty.QueueConfig``.
            :param quick_connect_type: ``CfnQuickConnect.QuickConnectConfigProperty.QuickConnectType``.
            :param user_config: ``CfnQuickConnect.QuickConnectConfigProperty.UserConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_connect as connect
                
                quick_connect_config_property = connect.CfnQuickConnect.QuickConnectConfigProperty(
                    quick_connect_type="quickConnectType",
                
                    # the properties below are optional
                    phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                        phone_number="phoneNumber"
                    ),
                    queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        queue_arn="queueArn"
                    ),
                    user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        user_arn="userArn"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "quick_connect_type": quick_connect_type,
            }
            if phone_config is not None:
                self._values["phone_config"] = phone_config
            if queue_config is not None:
                self._values["queue_config"] = queue_config
            if user_config is not None:
                self._values["user_config"] = user_config

        @builtins.property
        def phone_config(
            self,
        ) -> typing.Optional[typing.Union["CfnQuickConnect.PhoneNumberQuickConnectConfigProperty", _IResolvable_a771d0ef]]:
            '''``CfnQuickConnect.QuickConnectConfigProperty.PhoneConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-phoneconfig
            '''
            result = self._values.get("phone_config")
            return typing.cast(typing.Optional[typing.Union["CfnQuickConnect.PhoneNumberQuickConnectConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def queue_config(
            self,
        ) -> typing.Optional[typing.Union["CfnQuickConnect.QueueQuickConnectConfigProperty", _IResolvable_a771d0ef]]:
            '''``CfnQuickConnect.QuickConnectConfigProperty.QueueConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-queueconfig
            '''
            result = self._values.get("queue_config")
            return typing.cast(typing.Optional[typing.Union["CfnQuickConnect.QueueQuickConnectConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def quick_connect_type(self) -> builtins.str:
            '''``CfnQuickConnect.QuickConnectConfigProperty.QuickConnectType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-quickconnecttype
            '''
            result = self._values.get("quick_connect_type")
            assert result is not None, "Required property 'quick_connect_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_config(
            self,
        ) -> typing.Optional[typing.Union["CfnQuickConnect.UserQuickConnectConfigProperty", _IResolvable_a771d0ef]]:
            '''``CfnQuickConnect.QuickConnectConfigProperty.UserConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-userconfig
            '''
            result = self._values.get("user_config")
            return typing.cast(typing.Optional[typing.Union["CfnQuickConnect.UserQuickConnectConfigProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_connect.CfnQuickConnect.UserQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_flow_arn": "contactFlowArn", "user_arn": "userArn"},
    )
    class UserQuickConnectConfigProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            user_arn: builtins.str,
        ) -> None:
            '''
            :param contact_flow_arn: ``CfnQuickConnect.UserQuickConnectConfigProperty.ContactFlowArn``.
            :param user_arn: ``CfnQuickConnect.UserQuickConnectConfigProperty.UserArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_connect as connect
                
                user_quick_connect_config_property = connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    user_arn="userArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "user_arn": user_arn,
            }

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''``CfnQuickConnect.UserQuickConnectConfigProperty.ContactFlowArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_arn(self) -> builtins.str:
            '''``CfnQuickConnect.UserQuickConnectConfigProperty.UserArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-userarn
            '''
            result = self._values.get("user_arn")
            assert result is not None, "Required property 'user_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_connect.CfnQuickConnectProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "instance_arn": "instanceArn",
        "name": "name",
        "quick_connect_config": "quickConnectConfig",
        "tags": "tags",
    },
)
class CfnQuickConnectProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        instance_arn: builtins.str,
        name: builtins.str,
        quick_connect_config: typing.Union[CfnQuickConnect.QuickConnectConfigProperty, _IResolvable_a771d0ef],
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Connect::QuickConnect``.

        :param description: ``AWS::Connect::QuickConnect.Description``.
        :param instance_arn: ``AWS::Connect::QuickConnect.InstanceArn``.
        :param name: ``AWS::Connect::QuickConnect.Name``.
        :param quick_connect_config: ``AWS::Connect::QuickConnect.QuickConnectConfig``.
        :param tags: ``AWS::Connect::QuickConnect.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_connect as connect
            
            cfn_quick_connect_props = connect.CfnQuickConnectProps(
                instance_arn="instanceArn",
                name="name",
                quick_connect_config=connect.CfnQuickConnect.QuickConnectConfigProperty(
                    quick_connect_type="quickConnectType",
            
                    # the properties below are optional
                    phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                        phone_number="phoneNumber"
                    ),
                    queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        queue_arn="queueArn"
                    ),
                    user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        user_arn="userArn"
                    )
                ),
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
            "quick_connect_config": quick_connect_config,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::QuickConnect.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::QuickConnect.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Connect::QuickConnect.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def quick_connect_config(
        self,
    ) -> typing.Union[CfnQuickConnect.QuickConnectConfigProperty, _IResolvable_a771d0ef]:
        '''``AWS::Connect::QuickConnect.QuickConnectConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-quickconnectconfig
        '''
        result = self._values.get("quick_connect_config")
        assert result is not None, "Required property 'quick_connect_config' is missing"
        return typing.cast(typing.Union[CfnQuickConnect.QuickConnectConfigProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::Connect::QuickConnect.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickConnectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnUser(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_connect.CfnUser",
):
    '''A CloudFormation ``AWS::Connect::User``.

    :cloudformationResource: AWS::Connect::User
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_connect as connect
        
        cfn_user = connect.CfnUser(self, "MyCfnUser",
            instance_arn="instanceArn",
            phone_config=connect.CfnUser.UserPhoneConfigProperty(
                phone_type="phoneType",
        
                # the properties below are optional
                after_contact_work_time_limit=123,
                auto_accept=False,
                desk_phone_number="deskPhoneNumber"
            ),
            routing_profile_arn="routingProfileArn",
            security_profile_arns=["securityProfileArns"],
            username="username",
        
            # the properties below are optional
            directory_user_id="directoryUserId",
            hierarchy_group_arn="hierarchyGroupArn",
            identity_info=connect.CfnUser.UserIdentityInfoProperty(
                email="email",
                first_name="firstName",
                last_name="lastName"
            ),
            password="password",
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
        directory_user_id: typing.Optional[builtins.str] = None,
        hierarchy_group_arn: typing.Optional[builtins.str] = None,
        identity_info: typing.Optional[typing.Union["CfnUser.UserIdentityInfoProperty", _IResolvable_a771d0ef]] = None,
        instance_arn: builtins.str,
        password: typing.Optional[builtins.str] = None,
        phone_config: typing.Union["CfnUser.UserPhoneConfigProperty", _IResolvable_a771d0ef],
        routing_profile_arn: builtins.str,
        security_profile_arns: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        username: builtins.str,
    ) -> None:
        '''Create a new ``AWS::Connect::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param directory_user_id: ``AWS::Connect::User.DirectoryUserId``.
        :param hierarchy_group_arn: ``AWS::Connect::User.HierarchyGroupArn``.
        :param identity_info: ``AWS::Connect::User.IdentityInfo``.
        :param instance_arn: ``AWS::Connect::User.InstanceArn``.
        :param password: ``AWS::Connect::User.Password``.
        :param phone_config: ``AWS::Connect::User.PhoneConfig``.
        :param routing_profile_arn: ``AWS::Connect::User.RoutingProfileArn``.
        :param security_profile_arns: ``AWS::Connect::User.SecurityProfileArns``.
        :param tags: ``AWS::Connect::User.Tags``.
        :param username: ``AWS::Connect::User.Username``.
        '''
        props = CfnUserProps(
            directory_user_id=directory_user_id,
            hierarchy_group_arn=hierarchy_group_arn,
            identity_info=identity_info,
            instance_arn=instance_arn,
            password=password,
            phone_config=phone_config,
            routing_profile_arn=routing_profile_arn,
            security_profile_arns=security_profile_arns,
            tags=tags,
            username=username,
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
    @jsii.member(jsii_name="attrUserArn")
    def attr_user_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: UserArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserArn"))

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
    @jsii.member(jsii_name="directoryUserId")
    def directory_user_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::User.DirectoryUserId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-directoryuserid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryUserId"))

    @directory_user_id.setter
    def directory_user_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "directoryUserId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hierarchyGroupArn")
    def hierarchy_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::User.HierarchyGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-hierarchygrouparn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hierarchyGroupArn"))

    @hierarchy_group_arn.setter
    def hierarchy_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "hierarchyGroupArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityInfo")
    def identity_info(
        self,
    ) -> typing.Optional[typing.Union["CfnUser.UserIdentityInfoProperty", _IResolvable_a771d0ef]]:
        '''``AWS::Connect::User.IdentityInfo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-identityinfo
        '''
        return typing.cast(typing.Optional[typing.Union["CfnUser.UserIdentityInfoProperty", _IResolvable_a771d0ef]], jsii.get(self, "identityInfo"))

    @identity_info.setter
    def identity_info(
        self,
        value: typing.Optional[typing.Union["CfnUser.UserIdentityInfoProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "identityInfo", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::User.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::User.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-password
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "password", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="phoneConfig")
    def phone_config(
        self,
    ) -> typing.Union["CfnUser.UserPhoneConfigProperty", _IResolvable_a771d0ef]:
        '''``AWS::Connect::User.PhoneConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-phoneconfig
        '''
        return typing.cast(typing.Union["CfnUser.UserPhoneConfigProperty", _IResolvable_a771d0ef], jsii.get(self, "phoneConfig"))

    @phone_config.setter
    def phone_config(
        self,
        value: typing.Union["CfnUser.UserPhoneConfigProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "phoneConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routingProfileArn")
    def routing_profile_arn(self) -> builtins.str:
        '''``AWS::Connect::User.RoutingProfileArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-routingprofilearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "routingProfileArn"))

    @routing_profile_arn.setter
    def routing_profile_arn(self, value: builtins.str) -> None:
        jsii.set(self, "routingProfileArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityProfileArns")
    def security_profile_arns(self) -> typing.List[builtins.str]:
        '''``AWS::Connect::User.SecurityProfileArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-securityprofilearns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityProfileArns"))

    @security_profile_arns.setter
    def security_profile_arns(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "securityProfileArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::Connect::User.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        '''``AWS::Connect::User.Username``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-username
        '''
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        jsii.set(self, "username", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_connect.CfnUser.UserIdentityInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "email": "email",
            "first_name": "firstName",
            "last_name": "lastName",
        },
    )
    class UserIdentityInfoProperty:
        def __init__(
            self,
            *,
            email: typing.Optional[builtins.str] = None,
            first_name: typing.Optional[builtins.str] = None,
            last_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param email: ``CfnUser.UserIdentityInfoProperty.Email``.
            :param first_name: ``CfnUser.UserIdentityInfoProperty.FirstName``.
            :param last_name: ``CfnUser.UserIdentityInfoProperty.LastName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_connect as connect
                
                user_identity_info_property = connect.CfnUser.UserIdentityInfoProperty(
                    email="email",
                    first_name="firstName",
                    last_name="lastName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if email is not None:
                self._values["email"] = email
            if first_name is not None:
                self._values["first_name"] = first_name
            if last_name is not None:
                self._values["last_name"] = last_name

        @builtins.property
        def email(self) -> typing.Optional[builtins.str]:
            '''``CfnUser.UserIdentityInfoProperty.Email``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-email
            '''
            result = self._values.get("email")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_name(self) -> typing.Optional[builtins.str]:
            '''``CfnUser.UserIdentityInfoProperty.FirstName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_name(self) -> typing.Optional[builtins.str]:
            '''``CfnUser.UserIdentityInfoProperty.LastName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserIdentityInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_connect.CfnUser.UserPhoneConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "after_contact_work_time_limit": "afterContactWorkTimeLimit",
            "auto_accept": "autoAccept",
            "desk_phone_number": "deskPhoneNumber",
            "phone_type": "phoneType",
        },
    )
    class UserPhoneConfigProperty:
        def __init__(
            self,
            *,
            after_contact_work_time_limit: typing.Optional[jsii.Number] = None,
            auto_accept: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            desk_phone_number: typing.Optional[builtins.str] = None,
            phone_type: builtins.str,
        ) -> None:
            '''
            :param after_contact_work_time_limit: ``CfnUser.UserPhoneConfigProperty.AfterContactWorkTimeLimit``.
            :param auto_accept: ``CfnUser.UserPhoneConfigProperty.AutoAccept``.
            :param desk_phone_number: ``CfnUser.UserPhoneConfigProperty.DeskPhoneNumber``.
            :param phone_type: ``CfnUser.UserPhoneConfigProperty.PhoneType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_connect as connect
                
                user_phone_config_property = connect.CfnUser.UserPhoneConfigProperty(
                    phone_type="phoneType",
                
                    # the properties below are optional
                    after_contact_work_time_limit=123,
                    auto_accept=False,
                    desk_phone_number="deskPhoneNumber"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "phone_type": phone_type,
            }
            if after_contact_work_time_limit is not None:
                self._values["after_contact_work_time_limit"] = after_contact_work_time_limit
            if auto_accept is not None:
                self._values["auto_accept"] = auto_accept
            if desk_phone_number is not None:
                self._values["desk_phone_number"] = desk_phone_number

        @builtins.property
        def after_contact_work_time_limit(self) -> typing.Optional[jsii.Number]:
            '''``CfnUser.UserPhoneConfigProperty.AfterContactWorkTimeLimit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-aftercontactworktimelimit
            '''
            result = self._values.get("after_contact_work_time_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def auto_accept(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''``CfnUser.UserPhoneConfigProperty.AutoAccept``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-autoaccept
            '''
            result = self._values.get("auto_accept")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def desk_phone_number(self) -> typing.Optional[builtins.str]:
            '''``CfnUser.UserPhoneConfigProperty.DeskPhoneNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-deskphonenumber
            '''
            result = self._values.get("desk_phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def phone_type(self) -> builtins.str:
            '''``CfnUser.UserPhoneConfigProperty.PhoneType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-phonetype
            '''
            result = self._values.get("phone_type")
            assert result is not None, "Required property 'phone_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPhoneConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_82c04a63)
class CfnUserHierarchyGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_connect.CfnUserHierarchyGroup",
):
    '''A CloudFormation ``AWS::Connect::UserHierarchyGroup``.

    :cloudformationResource: AWS::Connect::UserHierarchyGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_connect as connect
        
        cfn_user_hierarchy_group = connect.CfnUserHierarchyGroup(self, "MyCfnUserHierarchyGroup",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            parent_group_arn="parentGroupArn"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        parent_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Connect::UserHierarchyGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: ``AWS::Connect::UserHierarchyGroup.InstanceArn``.
        :param name: ``AWS::Connect::UserHierarchyGroup.Name``.
        :param parent_group_arn: ``AWS::Connect::UserHierarchyGroup.ParentGroupArn``.
        '''
        props = CfnUserHierarchyGroupProps(
            instance_arn=instance_arn, name=name, parent_group_arn=parent_group_arn
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
    @jsii.member(jsii_name="attrUserHierarchyGroupArn")
    def attr_user_hierarchy_group_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: UserHierarchyGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserHierarchyGroupArn"))

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::UserHierarchyGroup.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Connect::UserHierarchyGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parentGroupArn")
    def parent_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::UserHierarchyGroup.ParentGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-parentgrouparn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentGroupArn"))

    @parent_group_arn.setter
    def parent_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "parentGroupArn", value)


@jsii.data_type(
    jsii_type="monocdk.aws_connect.CfnUserHierarchyGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "parent_group_arn": "parentGroupArn",
    },
)
class CfnUserHierarchyGroupProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        parent_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Connect::UserHierarchyGroup``.

        :param instance_arn: ``AWS::Connect::UserHierarchyGroup.InstanceArn``.
        :param name: ``AWS::Connect::UserHierarchyGroup.Name``.
        :param parent_group_arn: ``AWS::Connect::UserHierarchyGroup.ParentGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_connect as connect
            
            cfn_user_hierarchy_group_props = connect.CfnUserHierarchyGroupProps(
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                parent_group_arn="parentGroupArn"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if parent_group_arn is not None:
            self._values["parent_group_arn"] = parent_group_arn

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::UserHierarchyGroup.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Connect::UserHierarchyGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::UserHierarchyGroup.ParentGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-parentgrouparn
        '''
        result = self._values.get("parent_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserHierarchyGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_connect.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "directory_user_id": "directoryUserId",
        "hierarchy_group_arn": "hierarchyGroupArn",
        "identity_info": "identityInfo",
        "instance_arn": "instanceArn",
        "password": "password",
        "phone_config": "phoneConfig",
        "routing_profile_arn": "routingProfileArn",
        "security_profile_arns": "securityProfileArns",
        "tags": "tags",
        "username": "username",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        directory_user_id: typing.Optional[builtins.str] = None,
        hierarchy_group_arn: typing.Optional[builtins.str] = None,
        identity_info: typing.Optional[typing.Union[CfnUser.UserIdentityInfoProperty, _IResolvable_a771d0ef]] = None,
        instance_arn: builtins.str,
        password: typing.Optional[builtins.str] = None,
        phone_config: typing.Union[CfnUser.UserPhoneConfigProperty, _IResolvable_a771d0ef],
        routing_profile_arn: builtins.str,
        security_profile_arns: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        username: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::Connect::User``.

        :param directory_user_id: ``AWS::Connect::User.DirectoryUserId``.
        :param hierarchy_group_arn: ``AWS::Connect::User.HierarchyGroupArn``.
        :param identity_info: ``AWS::Connect::User.IdentityInfo``.
        :param instance_arn: ``AWS::Connect::User.InstanceArn``.
        :param password: ``AWS::Connect::User.Password``.
        :param phone_config: ``AWS::Connect::User.PhoneConfig``.
        :param routing_profile_arn: ``AWS::Connect::User.RoutingProfileArn``.
        :param security_profile_arns: ``AWS::Connect::User.SecurityProfileArns``.
        :param tags: ``AWS::Connect::User.Tags``.
        :param username: ``AWS::Connect::User.Username``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_connect as connect
            
            cfn_user_props = connect.CfnUserProps(
                instance_arn="instanceArn",
                phone_config=connect.CfnUser.UserPhoneConfigProperty(
                    phone_type="phoneType",
            
                    # the properties below are optional
                    after_contact_work_time_limit=123,
                    auto_accept=False,
                    desk_phone_number="deskPhoneNumber"
                ),
                routing_profile_arn="routingProfileArn",
                security_profile_arns=["securityProfileArns"],
                username="username",
            
                # the properties below are optional
                directory_user_id="directoryUserId",
                hierarchy_group_arn="hierarchyGroupArn",
                identity_info=connect.CfnUser.UserIdentityInfoProperty(
                    email="email",
                    first_name="firstName",
                    last_name="lastName"
                ),
                password="password",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "phone_config": phone_config,
            "routing_profile_arn": routing_profile_arn,
            "security_profile_arns": security_profile_arns,
            "username": username,
        }
        if directory_user_id is not None:
            self._values["directory_user_id"] = directory_user_id
        if hierarchy_group_arn is not None:
            self._values["hierarchy_group_arn"] = hierarchy_group_arn
        if identity_info is not None:
            self._values["identity_info"] = identity_info
        if password is not None:
            self._values["password"] = password
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def directory_user_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::User.DirectoryUserId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-directoryuserid
        '''
        result = self._values.get("directory_user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hierarchy_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::User.HierarchyGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-hierarchygrouparn
        '''
        result = self._values.get("hierarchy_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_info(
        self,
    ) -> typing.Optional[typing.Union[CfnUser.UserIdentityInfoProperty, _IResolvable_a771d0ef]]:
        '''``AWS::Connect::User.IdentityInfo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-identityinfo
        '''
        result = self._values.get("identity_info")
        return typing.cast(typing.Optional[typing.Union[CfnUser.UserIdentityInfoProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::Connect::User.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''``AWS::Connect::User.Password``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phone_config(
        self,
    ) -> typing.Union[CfnUser.UserPhoneConfigProperty, _IResolvable_a771d0ef]:
        '''``AWS::Connect::User.PhoneConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-phoneconfig
        '''
        result = self._values.get("phone_config")
        assert result is not None, "Required property 'phone_config' is missing"
        return typing.cast(typing.Union[CfnUser.UserPhoneConfigProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def routing_profile_arn(self) -> builtins.str:
        '''``AWS::Connect::User.RoutingProfileArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-routingprofilearn
        '''
        result = self._values.get("routing_profile_arn")
        assert result is not None, "Required property 'routing_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_profile_arns(self) -> typing.List[builtins.str]:
        '''``AWS::Connect::User.SecurityProfileArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-securityprofilearns
        '''
        result = self._values.get("security_profile_arns")
        assert result is not None, "Required property 'security_profile_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::Connect::User.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def username(self) -> builtins.str:
        '''``AWS::Connect::User.Username``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-username
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnContactFlow",
    "CfnContactFlowModule",
    "CfnContactFlowModuleProps",
    "CfnContactFlowProps",
    "CfnHoursOfOperation",
    "CfnHoursOfOperationProps",
    "CfnQuickConnect",
    "CfnQuickConnectProps",
    "CfnUser",
    "CfnUserHierarchyGroup",
    "CfnUserHierarchyGroupProps",
    "CfnUserProps",
]

publication.publish()
