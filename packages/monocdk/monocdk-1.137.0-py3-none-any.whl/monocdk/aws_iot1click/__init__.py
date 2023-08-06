'''
# AWS IoT 1-Click Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as iot1click
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoT1Click](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoT1Click.html).

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
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnDevice(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot1click.CfnDevice",
):
    '''A CloudFormation ``AWS::IoT1Click::Device``.

    :cloudformationResource: AWS::IoT1Click::Device
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot1click as iot1click
        
        cfn_device = iot1click.CfnDevice(self, "MyCfnDevice",
            device_id="deviceId",
            enabled=False
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        device_id: builtins.str,
        enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
    ) -> None:
        '''Create a new ``AWS::IoT1Click::Device``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param device_id: ``AWS::IoT1Click::Device.DeviceId``.
        :param enabled: ``AWS::IoT1Click::Device.Enabled``.
        '''
        props = CfnDeviceProps(device_id=device_id, enabled=enabled)

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
    @jsii.member(jsii_name="attrDeviceId")
    def attr_device_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DeviceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeviceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEnabled")
    def attr_enabled(self) -> _IResolvable_a771d0ef:
        '''
        :cloudformationAttribute: Enabled
        '''
        return typing.cast(_IResolvable_a771d0ef, jsii.get(self, "attrEnabled"))

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
    @jsii.member(jsii_name="deviceId")
    def device_id(self) -> builtins.str:
        '''``AWS::IoT1Click::Device.DeviceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html#cfn-iot1click-device-deviceid
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceId"))

    @device_id.setter
    def device_id(self, value: builtins.str) -> None:
        jsii.set(self, "deviceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
        '''``AWS::IoT1Click::Device.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html#cfn-iot1click-device-enabled
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot1click.CfnDeviceProps",
    jsii_struct_bases=[],
    name_mapping={"device_id": "deviceId", "enabled": "enabled"},
)
class CfnDeviceProps:
    def __init__(
        self,
        *,
        device_id: builtins.str,
        enabled: typing.Union[builtins.bool, _IResolvable_a771d0ef],
    ) -> None:
        '''Properties for defining a ``AWS::IoT1Click::Device``.

        :param device_id: ``AWS::IoT1Click::Device.DeviceId``.
        :param enabled: ``AWS::IoT1Click::Device.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot1click as iot1click
            
            cfn_device_props = iot1click.CfnDeviceProps(
                device_id="deviceId",
                enabled=False
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "device_id": device_id,
            "enabled": enabled,
        }

    @builtins.property
    def device_id(self) -> builtins.str:
        '''``AWS::IoT1Click::Device.DeviceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html#cfn-iot1click-device-deviceid
        '''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _IResolvable_a771d0ef]:
        '''``AWS::IoT1Click::Device.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html#cfn-iot1click-device-enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_a771d0ef], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnPlacement(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot1click.CfnPlacement",
):
    '''A CloudFormation ``AWS::IoT1Click::Placement``.

    :cloudformationResource: AWS::IoT1Click::Placement
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot1click as iot1click
        
        # associated_devices is of type object
        # attributes is of type object
        
        cfn_placement = iot1click.CfnPlacement(self, "MyCfnPlacement",
            project_name="projectName",
        
            # the properties below are optional
            associated_devices=associated_devices,
            attributes=attributes,
            placement_name="placementName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        associated_devices: typing.Any = None,
        attributes: typing.Any = None,
        placement_name: typing.Optional[builtins.str] = None,
        project_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT1Click::Placement``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param associated_devices: ``AWS::IoT1Click::Placement.AssociatedDevices``.
        :param attributes: ``AWS::IoT1Click::Placement.Attributes``.
        :param placement_name: ``AWS::IoT1Click::Placement.PlacementName``.
        :param project_name: ``AWS::IoT1Click::Placement.ProjectName``.
        '''
        props = CfnPlacementProps(
            associated_devices=associated_devices,
            attributes=attributes,
            placement_name=placement_name,
            project_name=project_name,
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
    @jsii.member(jsii_name="associatedDevices")
    def associated_devices(self) -> typing.Any:
        '''``AWS::IoT1Click::Placement.AssociatedDevices``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-associateddevices
        '''
        return typing.cast(typing.Any, jsii.get(self, "associatedDevices"))

    @associated_devices.setter
    def associated_devices(self, value: typing.Any) -> None:
        jsii.set(self, "associatedDevices", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Any:
        '''``AWS::IoT1Click::Placement.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-attributes
        '''
        return typing.cast(typing.Any, jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(self, value: typing.Any) -> None:
        jsii.set(self, "attributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPlacementName")
    def attr_placement_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: PlacementName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlacementName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProjectName")
    def attr_project_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectName"))

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
    @jsii.member(jsii_name="placementName")
    def placement_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT1Click::Placement.PlacementName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-placementname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementName"))

    @placement_name.setter
    def placement_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "placementName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        '''``AWS::IoT1Click::Placement.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-projectname
        '''
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        jsii.set(self, "projectName", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot1click.CfnPlacementProps",
    jsii_struct_bases=[],
    name_mapping={
        "associated_devices": "associatedDevices",
        "attributes": "attributes",
        "placement_name": "placementName",
        "project_name": "projectName",
    },
)
class CfnPlacementProps:
    def __init__(
        self,
        *,
        associated_devices: typing.Any = None,
        attributes: typing.Any = None,
        placement_name: typing.Optional[builtins.str] = None,
        project_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::IoT1Click::Placement``.

        :param associated_devices: ``AWS::IoT1Click::Placement.AssociatedDevices``.
        :param attributes: ``AWS::IoT1Click::Placement.Attributes``.
        :param placement_name: ``AWS::IoT1Click::Placement.PlacementName``.
        :param project_name: ``AWS::IoT1Click::Placement.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot1click as iot1click
            
            # associated_devices is of type object
            # attributes is of type object
            
            cfn_placement_props = iot1click.CfnPlacementProps(
                project_name="projectName",
            
                # the properties below are optional
                associated_devices=associated_devices,
                attributes=attributes,
                placement_name="placementName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "project_name": project_name,
        }
        if associated_devices is not None:
            self._values["associated_devices"] = associated_devices
        if attributes is not None:
            self._values["attributes"] = attributes
        if placement_name is not None:
            self._values["placement_name"] = placement_name

    @builtins.property
    def associated_devices(self) -> typing.Any:
        '''``AWS::IoT1Click::Placement.AssociatedDevices``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-associateddevices
        '''
        result = self._values.get("associated_devices")
        return typing.cast(typing.Any, result)

    @builtins.property
    def attributes(self) -> typing.Any:
        '''``AWS::IoT1Click::Placement.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Any, result)

    @builtins.property
    def placement_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT1Click::Placement.PlacementName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-placementname
        '''
        result = self._values.get("placement_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_name(self) -> builtins.str:
        '''``AWS::IoT1Click::Placement.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-projectname
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlacementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnProject(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot1click.CfnProject",
):
    '''A CloudFormation ``AWS::IoT1Click::Project``.

    :cloudformationResource: AWS::IoT1Click::Project
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot1click as iot1click
        
        # callback_overrides is of type object
        # default_attributes is of type object
        
        cfn_project = iot1click.CfnProject(self, "MyCfnProject",
            placement_template=iot1click.CfnProject.PlacementTemplateProperty(
                default_attributes=default_attributes,
                device_templates={
                    "device_templates_key": iot1click.CfnProject.DeviceTemplateProperty(
                        callback_overrides=callback_overrides,
                        device_type="deviceType"
                    )
                }
            ),
        
            # the properties below are optional
            description="description",
            project_name="projectName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        placement_template: typing.Union["CfnProject.PlacementTemplateProperty", _IResolvable_a771d0ef],
        project_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT1Click::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::IoT1Click::Project.Description``.
        :param placement_template: ``AWS::IoT1Click::Project.PlacementTemplate``.
        :param project_name: ``AWS::IoT1Click::Project.ProjectName``.
        '''
        props = CfnProjectProps(
            description=description,
            placement_template=placement_template,
            project_name=project_name,
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
    @jsii.member(jsii_name="attrProjectName")
    def attr_project_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectName"))

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
        '''``AWS::IoT1Click::Project.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="placementTemplate")
    def placement_template(
        self,
    ) -> typing.Union["CfnProject.PlacementTemplateProperty", _IResolvable_a771d0ef]:
        '''``AWS::IoT1Click::Project.PlacementTemplate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-placementtemplate
        '''
        return typing.cast(typing.Union["CfnProject.PlacementTemplateProperty", _IResolvable_a771d0ef], jsii.get(self, "placementTemplate"))

    @placement_template.setter
    def placement_template(
        self,
        value: typing.Union["CfnProject.PlacementTemplateProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "placementTemplate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT1Click::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-projectname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "projectName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot1click.CfnProject.DeviceTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "callback_overrides": "callbackOverrides",
            "device_type": "deviceType",
        },
    )
    class DeviceTemplateProperty:
        def __init__(
            self,
            *,
            callback_overrides: typing.Any = None,
            device_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param callback_overrides: ``CfnProject.DeviceTemplateProperty.CallbackOverrides``.
            :param device_type: ``CfnProject.DeviceTemplateProperty.DeviceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot1click as iot1click
                
                # callback_overrides is of type object
                
                device_template_property = iot1click.CfnProject.DeviceTemplateProperty(
                    callback_overrides=callback_overrides,
                    device_type="deviceType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if callback_overrides is not None:
                self._values["callback_overrides"] = callback_overrides
            if device_type is not None:
                self._values["device_type"] = device_type

        @builtins.property
        def callback_overrides(self) -> typing.Any:
            '''``CfnProject.DeviceTemplateProperty.CallbackOverrides``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html#cfn-iot1click-project-devicetemplate-callbackoverrides
            '''
            result = self._values.get("callback_overrides")
            return typing.cast(typing.Any, result)

        @builtins.property
        def device_type(self) -> typing.Optional[builtins.str]:
            '''``CfnProject.DeviceTemplateProperty.DeviceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html#cfn-iot1click-project-devicetemplate-devicetype
            '''
            result = self._values.get("device_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot1click.CfnProject.PlacementTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_attributes": "defaultAttributes",
            "device_templates": "deviceTemplates",
        },
    )
    class PlacementTemplateProperty:
        def __init__(
            self,
            *,
            default_attributes: typing.Any = None,
            device_templates: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnProject.DeviceTemplateProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''
            :param default_attributes: ``CfnProject.PlacementTemplateProperty.DefaultAttributes``.
            :param device_templates: ``CfnProject.PlacementTemplateProperty.DeviceTemplates``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot1click as iot1click
                
                # callback_overrides is of type object
                # default_attributes is of type object
                
                placement_template_property = iot1click.CfnProject.PlacementTemplateProperty(
                    default_attributes=default_attributes,
                    device_templates={
                        "device_templates_key": iot1click.CfnProject.DeviceTemplateProperty(
                            callback_overrides=callback_overrides,
                            device_type="deviceType"
                        )
                    }
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_attributes is not None:
                self._values["default_attributes"] = default_attributes
            if device_templates is not None:
                self._values["device_templates"] = device_templates

        @builtins.property
        def default_attributes(self) -> typing.Any:
            '''``CfnProject.PlacementTemplateProperty.DefaultAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html#cfn-iot1click-project-placementtemplate-defaultattributes
            '''
            result = self._values.get("default_attributes")
            return typing.cast(typing.Any, result)

        @builtins.property
        def device_templates(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnProject.DeviceTemplateProperty", _IResolvable_a771d0ef]]]]:
            '''``CfnProject.PlacementTemplateProperty.DeviceTemplates``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html#cfn-iot1click-project-placementtemplate-devicetemplates
            '''
            result = self._values.get("device_templates")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnProject.DeviceTemplateProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot1click.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "placement_template": "placementTemplate",
        "project_name": "projectName",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        placement_template: typing.Union[CfnProject.PlacementTemplateProperty, _IResolvable_a771d0ef],
        project_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoT1Click::Project``.

        :param description: ``AWS::IoT1Click::Project.Description``.
        :param placement_template: ``AWS::IoT1Click::Project.PlacementTemplate``.
        :param project_name: ``AWS::IoT1Click::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot1click as iot1click
            
            # callback_overrides is of type object
            # default_attributes is of type object
            
            cfn_project_props = iot1click.CfnProjectProps(
                placement_template=iot1click.CfnProject.PlacementTemplateProperty(
                    default_attributes=default_attributes,
                    device_templates={
                        "device_templates_key": iot1click.CfnProject.DeviceTemplateProperty(
                            callback_overrides=callback_overrides,
                            device_type="deviceType"
                        )
                    }
                ),
            
                # the properties below are optional
                description="description",
                project_name="projectName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "placement_template": placement_template,
        }
        if description is not None:
            self._values["description"] = description
        if project_name is not None:
            self._values["project_name"] = project_name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT1Click::Project.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_template(
        self,
    ) -> typing.Union[CfnProject.PlacementTemplateProperty, _IResolvable_a771d0ef]:
        '''``AWS::IoT1Click::Project.PlacementTemplate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-placementtemplate
        '''
        result = self._values.get("placement_template")
        assert result is not None, "Required property 'placement_template' is missing"
        return typing.cast(typing.Union[CfnProject.PlacementTemplateProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def project_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT1Click::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-projectname
        '''
        result = self._values.get("project_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDevice",
    "CfnDeviceProps",
    "CfnPlacement",
    "CfnPlacementProps",
    "CfnProject",
    "CfnProjectProps",
]

publication.publish()
