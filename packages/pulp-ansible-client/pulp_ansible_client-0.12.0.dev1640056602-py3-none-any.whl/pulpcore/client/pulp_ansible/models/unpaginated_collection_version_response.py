# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_ansible.configuration import Configuration


class UnpaginatedCollectionVersionResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'version': 'str',
        'href': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'requires_ansible': 'str',
        'artifact': 'ArtifactRefResponse',
        'collection': 'CollectionRefResponse',
        'download_url': 'str',
        'name': 'str',
        'namespace': 'CollectionNamespaceResponse',
        'metadata': 'CollectionMetadataResponse',
        'git_url': 'str',
        'git_commit_sha': 'str'
    }

    attribute_map = {
        'version': 'version',
        'href': 'href',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'requires_ansible': 'requires_ansible',
        'artifact': 'artifact',
        'collection': 'collection',
        'download_url': 'download_url',
        'name': 'name',
        'namespace': 'namespace',
        'metadata': 'metadata',
        'git_url': 'git_url',
        'git_commit_sha': 'git_commit_sha'
    }

    def __init__(self, version=None, href=None, created_at=None, updated_at=None, requires_ansible=None, artifact=None, collection=None, download_url=None, name=None, namespace=None, metadata=None, git_url=None, git_commit_sha=None, local_vars_configuration=None):  # noqa: E501
        """UnpaginatedCollectionVersionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._href = None
        self._created_at = None
        self._updated_at = None
        self._requires_ansible = None
        self._artifact = None
        self._collection = None
        self._download_url = None
        self._name = None
        self._namespace = None
        self._metadata = None
        self._git_url = None
        self._git_commit_sha = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if href is not None:
            self.href = href
        self.created_at = created_at
        self.updated_at = updated_at
        self.requires_ansible = requires_ansible
        if artifact is not None:
            self.artifact = artifact
        if collection is not None:
            self.collection = collection
        if download_url is not None:
            self.download_url = download_url
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if metadata is not None:
            self.metadata = metadata
        if git_url is not None:
            self.git_url = git_url
        if git_commit_sha is not None:
            self.git_commit_sha = git_commit_sha

    @property
    def version(self):
        """Gets the version of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The version of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UnpaginatedCollectionVersionResponse.


        :param version: The version of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def href(self):
        """Gets the href of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The href of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this UnpaginatedCollectionVersionResponse.


        :param href: The href of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def created_at(self):
        """Gets the created_at of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The created_at of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UnpaginatedCollectionVersionResponse.


        :param created_at: The created_at of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The updated_at of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UnpaginatedCollectionVersionResponse.


        :param updated_at: The updated_at of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def requires_ansible(self):
        """Gets the requires_ansible of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The requires_ansible of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._requires_ansible

    @requires_ansible.setter
    def requires_ansible(self, requires_ansible):
        """Sets the requires_ansible of this UnpaginatedCollectionVersionResponse.


        :param requires_ansible: The requires_ansible of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                requires_ansible is not None and len(requires_ansible) > 255):
            raise ValueError("Invalid value for `requires_ansible`, length must be less than or equal to `255`")  # noqa: E501

        self._requires_ansible = requires_ansible

    @property
    def artifact(self):
        """Gets the artifact of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The artifact of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: ArtifactRefResponse
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this UnpaginatedCollectionVersionResponse.


        :param artifact: The artifact of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: ArtifactRefResponse
        """

        self._artifact = artifact

    @property
    def collection(self):
        """Gets the collection of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The collection of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: CollectionRefResponse
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this UnpaginatedCollectionVersionResponse.


        :param collection: The collection of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: CollectionRefResponse
        """

        self._collection = collection

    @property
    def download_url(self):
        """Gets the download_url of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The download_url of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this UnpaginatedCollectionVersionResponse.


        :param download_url: The download_url of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def name(self):
        """Gets the name of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The name of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnpaginatedCollectionVersionResponse.


        :param name: The name of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The namespace of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: CollectionNamespaceResponse
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this UnpaginatedCollectionVersionResponse.


        :param namespace: The namespace of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: CollectionNamespaceResponse
        """

        self._namespace = namespace

    @property
    def metadata(self):
        """Gets the metadata of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The metadata of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: CollectionMetadataResponse
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UnpaginatedCollectionVersionResponse.


        :param metadata: The metadata of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: CollectionMetadataResponse
        """

        self._metadata = metadata

    @property
    def git_url(self):
        """Gets the git_url of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The git_url of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this UnpaginatedCollectionVersionResponse.


        :param git_url: The git_url of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._git_url = git_url

    @property
    def git_commit_sha(self):
        """Gets the git_commit_sha of this UnpaginatedCollectionVersionResponse.  # noqa: E501


        :return: The git_commit_sha of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._git_commit_sha

    @git_commit_sha.setter
    def git_commit_sha(self, git_commit_sha):
        """Sets the git_commit_sha of this UnpaginatedCollectionVersionResponse.


        :param git_commit_sha: The git_commit_sha of this UnpaginatedCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._git_commit_sha = git_commit_sha

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UnpaginatedCollectionVersionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnpaginatedCollectionVersionResponse):
            return True

        return self.to_dict() != other.to_dict()
