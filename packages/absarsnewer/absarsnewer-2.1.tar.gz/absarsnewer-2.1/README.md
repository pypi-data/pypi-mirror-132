
# Getting Started with Zype-V1

## Introduction

TODO: Add a description

## Install the Package

The package is compatible with Python versions `2 >=2.7.9` and `3 >=3.4`.
Install the package from PyPi using the following pip command:

```python
pip install absarsnewer==2.1
```

You can also view the package at:
https://pypi.python.org/pypi/absarsnewer

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `nose` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
nosetests
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from zypev1.zypev_1_client import Zypev1Client
from zypev1.configuration import Environment

client = Zypev1Client(
    environment=Environment.PRODUCTION,)
```

## List of APIs

* [Videos](/doc/controllers/videos.md)
* [Playlists](/doc/controllers/playlists.md)
* [Managing Playlist Relationships](/doc/controllers/managing-playlist-relationships.md)
* [Categories](/doc/controllers/categories.md)
* [Apps](/doc/controllers/apps.md)
* [Devices](/doc/controllers/devices.md)
* [Device Categories](/doc/controllers/device-categories.md)
* [Players](/doc/controllers/players.md)
* [Master Manifests](/doc/controllers/master-manifests.md)
* [Segments](/doc/controllers/segments.md)
* [Video Imports](/doc/controllers/video-imports.md)
* [Video Sources](/doc/controllers/video-sources.md)
* [Category Content Rules](/doc/controllers/category-content-rules.md)
* [Playlist Content Rules](/doc/controllers/playlist-content-rules.md)
* [Video Content Rules](/doc/controllers/video-content-rules.md)
* [Consumers](/doc/controllers/consumers.md)
* [Device Linking](/doc/controllers/device-linking.md)
* [O Auth](/doc/controllers/o-auth.md)
* [Video Entitlements](/doc/controllers/video-entitlements.md)
* [Playlist Entitlements](/doc/controllers/playlist-entitlements.md)
* [Subscription Entitlements](/doc/controllers/subscription-entitlements.md)
* [Subscriptions](/doc/controllers/subscriptions.md)
* [Plans](/doc/controllers/plans.md)
* [Transactions](/doc/controllers/transactions.md)
* [Redemption Codes](/doc/controllers/redemption-codes.md)
* [Ad Tags](/doc/controllers/ad-tags.md)
* [Revenue Models](/doc/controllers/revenue-models.md)
* [Video Favorites](/doc/controllers/video-favorites.md)
* [Zobject Types](/doc/controllers/zobject-types.md)
* [Zobject](/doc/controllers/zobject.md)

## Classes Documentation

* [Utility Classes](/doc/utility-classes.md)
* [HttpResponse](/doc/http-response.md)
* [HttpRequest](/doc/http-request.md)

