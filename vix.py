# -*- coding: utf-8 -*-

import sys
from ctypes import *

_vix = cdll.LoadLibrary('vix.dll' if sys.platform[:3] == 'win' else 'libvixAllProducts.so')

# === Global ===

VIX_INVALID_HANDLE                                 = 0

# types of handles
VIX_HANDLETYPE_NONE                                = 0
VIX_HANDLETYPE_HOST                                = 2
VIX_HANDLETYPE_VM                                  = 3
VIX_HANDLETYPE_NETWORK                             = 5
VIX_HANDLETYPE_JOB                                 = 6
VIX_HANDLETYPE_SNAPSHOT                            = 7
VIX_HANDLETYPE_PROPERTY_LIST                       = 9
VIX_HANDLETYPE_METADATA_CONTAINER                  = 11

VIX_OK                                             = 0

# General errors
VIX_E_FAIL                                         = 1
VIX_E_OUT_OF_MEMORY                                = 2
VIX_E_INVALID_ARG                                  = 3
VIX_E_FILE_NOT_FOUND                               = 4
VIX_E_OBJECT_IS_BUSY                               = 5
VIX_E_NOT_SUPPORTED                                = 6
VIX_E_FILE_ERROR                                   = 7
VIX_E_DISK_FULL                                    = 8
VIX_E_INCORRECT_FILE_TYPE                          = 9
VIX_E_CANCELLED                                    = 10
VIX_E_FILE_READ_ONLY                               = 11
VIX_E_FILE_ALREADY_EXISTS                          = 12
VIX_E_FILE_ACCESS_ERROR                            = 13
VIX_E_REQUIRES_LARGE_FILES                         = 14
VIX_E_FILE_ALREADY_LOCKED                          = 15
VIX_E_VMDB                                         = 16
VIX_E_NOT_SUPPORTED_ON_REMOTE_OBJECT               = 20
VIX_E_FILE_TOO_BIG                                 = 21
VIX_E_FILE_NAME_INVALID                            = 22
VIX_E_ALREADY_EXISTS                               = 23
VIX_E_BUFFER_TOOSMALL                              = 24
VIX_E_OBJECT_NOT_FOUND                             = 25
VIX_E_HOST_NOT_CONNECTED                           = 26
VIX_E_INVALID_UTF8_STRING                          = 27
VIX_E_OPERATION_ALREADY_IN_PROGRESS                = 31
VIX_E_UNFINISHED_JOB                               = 29
VIX_E_NEED_KEY                                     = 30
VIX_E_LICENSE                                      = 32
VIX_E_VM_HOST_DISCONNECTED                         = 34
VIX_E_AUTHENTICATION_FAIL                          = 35
VIX_E_HOST_CONNECTION_LOST                         = 36
VIX_E_DUPLICATE_NAME                               = 41

# Handle errors
VIX_E_INVALID_HANDLE                               = 1000
VIX_E_NOT_SUPPORTED_ON_HANDLE_TYPE                 = 1001
VIX_E_TOO_MANY_HANDLES                             = 1002

# XML errors
VIX_E_NOT_FOUND                                    = 2000
VIX_E_TYPE_MISMATCH                                = 2001
VIX_E_INVALID_XML                                  = 2002

# VM control errors
VIX_E_TIMEOUT_WAITING_FOR_TOOLS                    = 3000
VIX_E_UNRECOGNIZED_COMMAND                         = 3001
VIX_E_OP_NOT_SUPPORTED_ON_GUEST                    = 3003
VIX_E_PROGRAM_NOT_STARTED                          = 3004
VIX_E_CANNOT_START_READ_ONLY_VM                    = 3005
VIX_E_VM_NOT_RUNNING                               = 3006
VIX_E_VM_IS_RUNNING                                = 3007
VIX_E_CANNOT_CONNECT_TO_VM                         = 3008
VIX_E_POWEROP_SCRIPTS_NOT_AVAILABLE                = 3009
VIX_E_NO_GUEST_OS_INSTALLED                        = 3010
VIX_E_VM_INSUFFICIENT_HOST_MEMORY                  = 3011
VIX_E_SUSPEND_ERROR                                = 3012
VIX_E_VM_NOT_ENOUGH_CPUS                           = 3013
VIX_E_HOST_USER_PERMISSIONS                        = 3014
VIX_E_GUEST_USER_PERMISSIONS                       = 3015
VIX_E_TOOLS_NOT_RUNNING                            = 3016
VIX_E_GUEST_OPERATIONS_PROHIBITED                  = 3017
VIX_E_ANON_GUEST_OPERATIONS_PROHIBITED             = 3018
VIX_E_ROOT_GUEST_OPERATIONS_PROHIBITED             = 3019
VIX_E_MISSING_ANON_GUEST_ACCOUNT                   = 3023
VIX_E_CANNOT_AUTHENTICATE_WITH_GUEST               = 3024
VIX_E_UNRECOGNIZED_COMMAND_IN_GUEST                = 3025
VIX_E_CONSOLE_GUEST_OPERATIONS_PROHIBITED          = 3026
VIX_E_MUST_BE_CONSOLE_USER                         = 3027
VIX_E_VMX_MSG_DIALOG_AND_NO_UI                     = 3028
VIX_E_NOT_ALLOWED_DURING_VM_RECORDING              = 3029
VIX_E_NOT_ALLOWED_DURING_VM_REPLAY                 = 3030
VIX_E_OPERATION_NOT_ALLOWED_FOR_LOGIN_TYPE         = 3031
VIX_E_LOGIN_TYPE_NOT_SUPPORTED                     = 3032
VIX_E_EMPTY_PASSWORD_NOT_ALLOWED_IN_GUEST          = 3033
VIX_E_INTERACTIVE_SESSION_NOT_PRESENT              = 3034
VIX_E_INTERACTIVE_SESSION_USER_MISMATCH            = 3035
VIX_E_UNABLE_TO_REPLAY_VM                          = 3039
VIX_E_CANNOT_POWER_ON_VM                           = 3041
VIX_E_NO_DISPLAY_SERVER                            = 3043
VIX_E_VM_NOT_RECORDING                             = 3044
VIX_E_VM_NOT_REPLAYING                             = 3045

# VM errors
VIX_E_VM_NOT_FOUND                                 = 4000
VIX_E_NOT_SUPPORTED_FOR_VM_VERSION                 = 4001
VIX_E_CANNOT_READ_VM_CONFIG                        = 4002
VIX_E_TEMPLATE_VM                                  = 4003
VIX_E_VM_ALREADY_LOADED                            = 4004
VIX_E_VM_ALREADY_UP_TO_DATE                        = 4006
VIX_E_VM_UNSUPPORTED_GUEST                         = 4011

# Property errors
VIX_E_UNRECOGNIZED_PROPERTY                        = 6000
VIX_E_INVALID_PROPERTY_VALUE                       = 6001
VIX_E_READ_ONLY_PROPERTY                           = 6002
VIX_E_MISSING_REQUIRED_PROPERTY                    = 6003
VIX_E_INVALID_SERIALIZED_DATA                      = 6004
VIX_E_PROPERTY_TYPE_MISMATCH                       = 6005

# Completion errors
VIX_E_BAD_VM_INDEX                                 = 8000

# Message errors
VIX_E_INVALID_MESSAGE_HEADER                       = 10000
VIX_E_INVALID_MESSAGE_BODY                         = 10001

# Snapshot errors
VIX_E_SNAPSHOT_INVAL                               = 13000
VIX_E_SNAPSHOT_DUMPER                              = 13001
VIX_E_SNAPSHOT_DISKLIB                             = 13002
VIX_E_SNAPSHOT_NOTFOUND                            = 13003
VIX_E_SNAPSHOT_EXISTS                              = 13004
VIX_E_SNAPSHOT_VERSION                             = 13005
VIX_E_SNAPSHOT_NOPERM                              = 13006
VIX_E_SNAPSHOT_CONFIG                              = 13007
VIX_E_SNAPSHOT_NOCHANGE                            = 13008
VIX_E_SNAPSHOT_CHECKPOINT                          = 13009
VIX_E_SNAPSHOT_LOCKED                              = 13010
VIX_E_SNAPSHOT_INCONSISTENT                        = 13011
VIX_E_SNAPSHOT_NAMETOOLONG                         = 13012
VIX_E_SNAPSHOT_VIXFILE                             = 13013
VIX_E_SNAPSHOT_DISKLOCKED                          = 13014
VIX_E_SNAPSHOT_DUPLICATEDDISK                      = 13015
VIX_E_SNAPSHOT_INDEPENDENTDISK                     = 13016
VIX_E_SNAPSHOT_NONUNIQUE_NAME                      = 13017
VIX_E_SNAPSHOT_MEMORY_ON_INDEPENDENT_DISK          = 13018
VIX_E_SNAPSHOT_MAXSNAPSHOTS                        = 13019
VIX_E_SNAPSHOT_MIN_FREE_SPACE                      = 13020
VIX_E_SNAPSHOT_HIERARCHY_TOODEEP                   = 13021

# Host errors
VIX_E_HOST_DISK_INVALID_VALUE                      = 14003
VIX_E_HOST_DISK_SECTORSIZE                         = 14004
VIX_E_HOST_FILE_ERROR_EOF                          = 14005
VIX_E_HOST_NETBLKDEV_HANDSHAKE                     = 14006
VIX_E_HOST_SOCKET_CREATION_ERROR                   = 14007
VIX_E_HOST_SERVER_NOT_FOUND                        = 14008
VIX_E_HOST_NETWORK_CONN_REFUSED                    = 14009
VIX_E_HOST_TCP_SOCKET_ERROR                        = 14010
VIX_E_HOST_TCP_CONN_LOST                           = 14011
VIX_E_HOST_NBD_HASHFILE_VOLUME                     = 14012
VIX_E_HOST_NBD_HASHFILE_INIT                       = 14013

# Disklib errors
VIX_E_DISK_INVAL                                   = 16000
VIX_E_DISK_NOINIT                                  = 16001
VIX_E_DISK_NOIO                                    = 16002
VIX_E_DISK_PARTIALCHAIN                            = 16003
VIX_E_DISK_NEEDSREPAIR                             = 16006
VIX_E_DISK_OUTOFRANGE                              = 16007
VIX_E_DISK_CID_MISMATCH                            = 16008
VIX_E_DISK_CANTSHRINK                              = 16009
VIX_E_DISK_PARTMISMATCH                            = 16010
VIX_E_DISK_UNSUPPORTEDDISKVERSION                  = 16011
VIX_E_DISK_OPENPARENT                              = 16012
VIX_E_DISK_NOTSUPPORTED                            = 16013
VIX_E_DISK_NEEDKEY                                 = 16014
VIX_E_DISK_NOKEYOVERRIDE                           = 16015
VIX_E_DISK_NOTENCRYPTED                            = 16016
VIX_E_DISK_NOKEY                                   = 16017
VIX_E_DISK_INVALIDPARTITIONTABLE                   = 16018
VIX_E_DISK_NOTNORMAL                               = 16019
VIX_E_DISK_NOTENCDESC                              = 16020
VIX_E_DISK_NEEDVMFS                                = 16022
VIX_E_DISK_RAWTOOBIG                               = 16024
VIX_E_DISK_TOOMANYOPENFILES                        = 16027
VIX_E_DISK_TOOMANYREDO                             = 16028
VIX_E_DISK_RAWTOOSMALL                             = 16029
VIX_E_DISK_INVALIDCHAIN                            = 16030
VIX_E_DISK_KEY_NOTFOUND                            = 16052
VIX_E_DISK_SUBSYSTEM_INIT_FAIL                     = 16053
VIX_E_DISK_INVALID_CONNECTION                      = 16054
VIX_E_DISK_ENCODING                                = 16061
VIX_E_DISK_CANTREPAIR                              = 16062
VIX_E_DISK_INVALIDDISK                             = 16063
VIX_E_DISK_NOLICENSE                               = 16064
VIX_E_DISK_NODEVICE                                = 16065
VIX_E_DISK_UNSUPPORTEDDEVICE                       = 16066

# Crypto library errors
VIX_E_CRYPTO_UNKNOWN_ALGORITHM                     = 17000
VIX_E_CRYPTO_BAD_BUFFER_SIZE                       = 17001
VIX_E_CRYPTO_INVALID_OPERATION                     = 17002
VIX_E_CRYPTO_RANDOM_DEVICE                         = 17003
VIX_E_CRYPTO_NEED_PASSWORD                         = 17004
VIX_E_CRYPTO_BAD_PASSWORD                          = 17005
VIX_E_CRYPTO_NOT_IN_DICTIONARY                     = 17006
VIX_E_CRYPTO_NO_CRYPTO                             = 17007
VIX_E_CRYPTO_ERROR                                 = 17008
VIX_E_CRYPTO_BAD_FORMAT                            = 17009
VIX_E_CRYPTO_LOCKED                                = 17010
VIX_E_CRYPTO_EMPTY                                 = 17011
VIX_E_CRYPTO_KEYSAFE_LOCATOR                       = 17012

# Remoting errors
VIX_E_CANNOT_CONNECT_TO_HOST                       = 18000
VIX_E_NOT_FOR_REMOTE_HOST                          = 18001
VIX_E_INVALID_HOSTNAME_SPECIFICATION               = 18002

# Screen capture errors
VIX_E_SCREEN_CAPTURE_ERROR                         = 19000
VIX_E_SCREEN_CAPTURE_BAD_FORMAT                    = 19001
VIX_E_SCREEN_CAPTURE_COMPRESSION_FAIL              = 19002
VIX_E_SCREEN_CAPTURE_LARGE_DATA                    = 19003

# Guest errors
VIX_E_GUEST_VOLUMES_NOT_FROZEN                     = 20000
VIX_E_NOT_A_FILE                                   = 20001
VIX_E_NOT_A_DIRECTORY                              = 20002
VIX_E_NO_SUCH_PROCESS                              = 20003
VIX_E_FILE_NAME_TOO_LONG                           = 20004

# Tools install errors
VIX_E_TOOLS_INSTALL_NO_IMAGE                       = 21000
VIX_E_TOOLS_INSTALL_IMAGE_INACCESIBLE              = 21001
VIX_E_TOOLS_INSTALL_NO_DEVICE                      = 21002
VIX_E_TOOLS_INSTALL_DEVICE_NOT_CONNECTED           = 21003
VIX_E_TOOLS_INSTALL_CANCELLED                      = 21004
VIX_E_TOOLS_INSTALL_INIT_FAILED                    = 21005
VIX_E_TOOLS_INSTALL_AUTO_NOT_SUPPORTED             = 21006
VIX_E_TOOLS_INSTALL_GUEST_NOT_READY                = 21007
VIX_E_TOOLS_INSTALL_SIG_CHECK_FAILED               = 21008
VIX_E_TOOLS_INSTALL_ERROR                          = 21009
VIX_E_TOOLS_INSTALL_ALREADY_UP_TO_DATE             = 21010
VIX_E_TOOLS_INSTALL_IN_PROGRESS                    = 21011

# Wrapper errors
VIX_E_WRAPPER_WORKSTATION_NOT_INSTALLED            = 22001
VIX_E_WRAPPER_VERSION_NOT_FOUND                    = 22002
VIX_E_WRAPPER_SERVICEPROVIDER_NOT_FOUND            = 22003
VIX_E_WRAPPER_PLAYER_NOT_INSTALLED                 = 22004
VIX_E_WRAPPER_RUNTIME_NOT_INSTALLED                = 22005
VIX_E_WRAPPER_MULTIPLE_SERVICEPROVIDERS            = 22006

# FuseMnt errors
VIX_E_MNTAPI_MOUNTPT_NOT_FOUND                     = 24000
VIX_E_MNTAPI_MOUNTPT_IN_USE                        = 24001
VIX_E_MNTAPI_DISK_NOT_FOUND                        = 24002
VIX_E_MNTAPI_DISK_NOT_MOUNTED                      = 24003
VIX_E_MNTAPI_DISK_IS_MOUNTED                       = 24004
VIX_E_MNTAPI_DISK_NOT_SAFE                         = 24005
VIX_E_MNTAPI_DISK_CANT_OPEN                        = 24006
VIX_E_MNTAPI_CANT_READ_PARTS                       = 24007
VIX_E_MNTAPI_UMOUNT_APP_NOT_FOUND                  = 24008
VIX_E_MNTAPI_UMOUNT                                = 24009
VIX_E_MNTAPI_NO_MOUNTABLE_PARTITONS                = 24010
VIX_E_MNTAPI_PARTITION_RANGE                       = 24011
VIX_E_MNTAPI_PERM                                  = 24012
VIX_E_MNTAPI_DICT                                  = 24013
VIX_E_MNTAPI_DICT_LOCKED                           = 24014
VIX_E_MNTAPI_OPEN_HANDLES                          = 24015
VIX_E_MNTAPI_CANT_MAKE_VAR_DIR                     = 24016
VIX_E_MNTAPI_NO_ROOT                               = 24017
VIX_E_MNTAPI_LOOP_FAILED                           = 24018
VIX_E_MNTAPI_DAEMON                                = 24019
VIX_E_MNTAPI_INTERNAL                              = 24020
VIX_E_MNTAPI_SYSTEM                                = 24021
VIX_E_MNTAPI_NO_CONNECTION_DETAILS                 = 24022

# VixMntapi errors
VIX_E_MNTAPI_INCOMPATIBLE_VERSION                  = 24300
VIX_E_MNTAPI_OS_ERROR                              = 24301
VIX_E_MNTAPI_DRIVE_LETTER_IN_USE                   = 24302
VIX_E_MNTAPI_DRIVE_LETTER_ALREADY_ASSIGNED         = 24303
VIX_E_MNTAPI_VOLUME_NOT_MOUNTED                    = 24304
VIX_E_MNTAPI_VOLUME_ALREADY_MOUNTED                = 24305
VIX_E_MNTAPI_FORMAT_FAILURE                        = 24306
VIX_E_MNTAPI_NO_DRIVER                             = 24307
VIX_E_MNTAPI_ALREADY_OPENED                        = 24308
VIX_E_MNTAPI_ITEM_NOT_FOUND                        = 24309
VIX_E_MNTAPI_UNSUPPROTED_BOOT_LOADER               = 24310
VIX_E_MNTAPI_UNSUPPROTED_OS                        = 24311
VIX_E_MNTAPI_CODECONVERSION                        = 24312
VIX_E_MNTAPI_REGWRITE_ERROR                        = 24313
VIX_E_MNTAPI_UNSUPPORTED_FT_VOLUME                 = 24314
VIX_E_MNTAPI_PARTITION_NOT_FOUND                   = 24315
VIX_E_MNTAPI_PUTFILE_ERROR                         = 24316
VIX_E_MNTAPI_GETFILE_ERROR                         = 24317
VIX_E_MNTAPI_REG_NOT_OPENED                        = 24318
VIX_E_MNTAPI_REGDELKEY_ERROR                       = 24319
VIX_E_MNTAPI_CREATE_PARTITIONTABLE_ERROR           = 24320
VIX_E_MNTAPI_OPEN_FAILURE                          = 24321
VIX_E_MNTAPI_VOLUME_NOT_WRITABLE                   = 24322

# Network errors
VIX_E_NET_HTTP_UNSUPPORTED_PROTOCOL                = 30001
VIX_E_NET_HTTP_URL_MALFORMAT                       = 30003
VIX_E_NET_HTTP_COULDNT_RESOLVE_PROXY               = 30005
VIX_E_NET_HTTP_COULDNT_RESOLVE_HOST                = 30006
VIX_E_NET_HTTP_COULDNT_CONNECT                     = 30007
VIX_E_NET_HTTP_HTTP_RETURNED_ERROR                 = 30022
VIX_E_NET_HTTP_OPERATION_TIMEDOUT                  = 30028
VIX_E_NET_HTTP_SSL_CONNECT_ERROR                   = 30035
VIX_E_NET_HTTP_TOO_MANY_REDIRECTS                  = 30047
VIX_E_NET_HTTP_TRANSFER                            = 30200
VIX_E_NET_HTTP_SSL_SECURITY                        = 30201
VIX_E_NET_HTTP_GENERIC                             = 30202

# VIX Property Type
VIX_PROPERTYTYPE_ANY                               = 0
VIX_PROPERTYTYPE_INTEGER                           = 1
VIX_PROPERTYTYPE_STRING                            = 2
VIX_PROPERTYTYPE_BOOL                              = 3
VIX_PROPERTYTYPE_HANDLE                            = 4
VIX_PROPERTYTYPE_INT64                             = 5
VIX_PROPERTYTYPE_BLOB                              = 6

# VIX Property ID
VIX_PROPERTY_NONE                                  = 0

# VIX Property ID: Properties used by several handle types
VIX_PROPERTY_META_DATA_CONTAINER                   = 2

# VIX Property ID: VIX_HANDLETYPE_HOST properties
VIX_PROPERTY_HOST_HOSTTYPE                         = 50
VIX_PROPERTY_HOST_API_VERSION                      = 51

# VIX Property ID: VIX_HANDLETYPE_VM properties
VIX_PROPERTY_VM_NUM_VCPUS                          = 101
VIX_PROPERTY_VM_VMX_PATHNAME                       = 103
VIX_PROPERTY_VM_VMTEAM_PATHNAME                    = 105
VIX_PROPERTY_VM_MEMORY_SIZE                        = 106
VIX_PROPERTY_VM_READ_ONLY                          = 107
VIX_PROPERTY_VM_NAME                               = 108
VIX_PROPERTY_VM_GUESTOS                            = 109
VIX_PROPERTY_VM_IN_VMTEAM                          = 128
VIX_PROPERTY_VM_POWER_STATE                        = 129
VIX_PROPERTY_VM_TOOLS_STATE                        = 152
VIX_PROPERTY_VM_IS_RUNNING                         = 196
VIX_PROPERTY_VM_SUPPORTED_FEATURES                 = 197
VIX_PROPERTY_VM_IS_RECORDING                       = 236
VIX_PROPERTY_VM_IS_REPLAYING                       = 237

# VIX Property ID: Result properties
# These are returned by various procedures
VIX_PROPERTY_JOB_RESULT_ERROR_CODE                 = 3000
VIX_PROPERTY_JOB_RESULT_VM_IN_GROUP                = 3001
VIX_PROPERTY_JOB_RESULT_USER_MESSAGE               = 3002
VIX_PROPERTY_JOB_RESULT_EXIT_CODE                  = 3004
VIX_PROPERTY_JOB_RESULT_COMMAND_OUTPUT             = 3005
VIX_PROPERTY_JOB_RESULT_HANDLE                     = 3010
VIX_PROPERTY_JOB_RESULT_GUEST_OBJECT_EXISTS        = 3011
VIX_PROPERTY_JOB_RESULT_GUEST_PROGRAM_ELAPSED_TIME = 3017
VIX_PROPERTY_JOB_RESULT_GUEST_PROGRAM_EXIT_CODE    = 3018
VIX_PROPERTY_JOB_RESULT_ITEM_NAME                  = 3035
VIX_PROPERTY_JOB_RESULT_FOUND_ITEM_DESCRIPTION     = 3036
VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_COUNT        = 3046
VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_HOST         = 3048
VIX_PROPERTY_JOB_RESULT_SHARED_FOLDER_FLAGS        = 3049
VIX_PROPERTY_JOB_RESULT_PROCESS_ID                 = 3051
VIX_PROPERTY_JOB_RESULT_PROCESS_OWNER              = 3052
VIX_PROPERTY_JOB_RESULT_PROCESS_COMMAND            = 3053
VIX_PROPERTY_JOB_RESULT_FILE_FLAGS                 = 3054
VIX_PROPERTY_JOB_RESULT_PROCESS_START_TIME         = 3055
VIX_PROPERTY_JOB_RESULT_VM_VARIABLE_STRING         = 3056
VIX_PROPERTY_JOB_RESULT_PROCESS_BEING_DEBUGGED     = 3057
VIX_PROPERTY_JOB_RESULT_SCREEN_IMAGE_SIZE          = 3058
VIX_PROPERTY_JOB_RESULT_SCREEN_IMAGE_DATA          = 3059
VIX_PROPERTY_JOB_RESULT_FILE_SIZE                  = 3061
VIX_PROPERTY_JOB_RESULT_FILE_MOD_TIME              = 3062
VIX_PROPERTY_JOB_RESULT_EXTRA_ERROR_INFO           = 3084

# VIX Property ID: Event properties
# These are sent in the moreEventInfo for some events
VIX_PROPERTY_FOUND_ITEM_LOCATION                   = 4010

# VIX Property ID: VIX_HANDLETYPE_SNAPSHOT properties
VIX_PROPERTY_SNAPSHOT_DISPLAYNAME                  = 4200
VIX_PROPERTY_SNAPSHOT_DESCRIPTION                  = 4201
VIX_PROPERTY_SNAPSHOT_POWERSTATE                   = 4205
VIX_PROPERTY_SNAPSHOT_IS_REPLAYABLE                = 4207

VIX_PROPERTY_GUEST_SHAREDFOLDERS_SHARES_PATH       = 4525

# VIX Property ID: Virtual machine encryption properties
VIX_PROPERTY_VM_ENCRYPTION_PASSWORD                = 7001

# Vix Event Type
VIX_EVENTTYPE_JOB_COMPLETED                        = 2
VIX_EVENTTYPE_JOB_PROGRESS                         = 3
VIX_EVENTTYPE_FIND_ITEM                            = 8
# Deprecated - Use VIX_EVENTTYPE_JOB_COMPLETED instead
#VIX_EVENTTYPE_CALLBACK_SIGNALLED                   = 2

# Property flags for each file
VIX_FILE_ATTRIBUTES_DIRECTORY                      = 0x0001
VIX_FILE_ATTRIBUTES_SYMLINK                        = 0x0002

# VIX Host Options
VIX_HOSTOPTION_USE_EVENT_PUMP                      = 0x0008

# VIX Service Provider
VIX_SERVICEPROVIDER_DEFAULT                        = 1
VIX_SERVICEPROVIDER_VMWARE_SERVER                  = 2
VIX_SERVICEPROVIDER_VMWARE_WORKSTATION             = 3
VIX_SERVICEPROVIDER_VMWARE_PLAYER                  = 4
VIX_SERVICEPROVIDER_VMWARE_VI_SERVER               = 10

# VIX API VERSION
VIX_API_VERSION                                    = -1

# VIX Find Item Type
VIX_FIND_RUNNING_VMS                               = 1
VIX_FIND_REGISTERED_VMS                            = 4

# VIX VM Open Options
VIX_VMOPEN_NORMAL                                  = 0

# VIX Pup Events Options
VIX_PUMPEVENTOPTION_NONE                           = 0

# VIX VM Poer Operation Options
VIX_VMPOWEROP_NORMAL                               = 0
VIX_VMPOWEROP_FROM_GUEST                           = 0x0004
VIX_VMPOWEROP_SUPPRESS_SNAPSHOT_POWERON            = 0x0080
VIX_VMPOWEROP_LAUNCH_GUI                           = 0x0200
VIX_VMPOWEROP_START_VM_PAUSED                      = 0x1000

# VIX VM Delete Options
VIX_VMDELETE_DISK_FILES                            = 0x0002

# VIX Power State
VIX_POWERSTATE_POWERING_OFF                        = 0x0001
VIX_POWERSTATE_POWERED_OFF                         = 0x0002
VIX_POWERSTATE_POWERING_ON                         = 0x0004
VIX_POWERSTATE_POWERED_ON                          = 0x0008
VIX_POWERSTATE_SUSPENDING                          = 0x0010
VIX_POWERSTATE_SUSPENDED                           = 0x0020
VIX_POWERSTATE_TOOLS_RUNNING                       = 0x0040
VIX_POWERSTATE_RESETTING                           = 0x0080
VIX_POWERSTATE_BLOCKED_ON_MSG                      = 0x0100
VIX_POWERSTATE_PAUSED                              = 0x0200
VIX_POWERSTATE_RESUMING                            = 0x0800

# VIX Tools State
VIX_TOOLSSTATE_UNKNOWN                             = 0x0001
VIX_TOOLSSTATE_RUNNING                             = 0x0002
VIX_TOOLSSTATE_NOT_INSTALLED                       = 0x0004

# Optional functions supported by different types of VM
VIX_VM_SUPPORT_SHARED_FOLDERS                      = 0x0001
VIX_VM_SUPPORT_MULTIPLE_SNAPSHOTS                  = 0x0002
VIX_VM_SUPPORT_TOOLS_INSTALL                       = 0x0004
VIX_VM_SUPPORT_HARDWARE_UPGRADE                    = 0x0008

# VixVM_LoginInGuest option flags
VIX_LOGIN_IN_GUEST_REQUIRE_INTERACTIVE_ENVIRONMENT = 0x0008

# VIX Run Program Options
VIX_RUNPROGRAM_RETURN_IMMEDIATELY                  = 0x0001
VIX_RUNPROGRAM_ACTIVATE_WINDOW                     = 0x0002

# VIX Variable Options
VIX_VM_GUEST_VARIABLE                              = 1
VIX_VM_CONFIG_RUNTIME_ONLY                         = 2
VIX_GUEST_ENVIRONMENT_VARIABLE                     = 3

# VIX Remove Snapshot Options
VIX_SNAPSHOT_REMOVE_CHILDREN                       = 0x0001

# VIX Create Snapshot Options
VIX_SNAPSHOT_INCLUDE_MEMORY                        = 0x0002

# flags describing each shared folder
VIX_SHAREDFOLDER_WRITE_ACCESS                      = 0x04

# Screen Capture Format
VIX_CAPTURESCREENFORMAT_PNG                        = 0x01
VIX_CAPTURESCREENFORMAT_PNG_NOCOMPRESS             = 0x02

# VIX Clone Types
VIX_CLONETYPE_FULL                                 = 0
VIX_CLONETYPE_LINKED                               = 1

# VIX Installtools Options
VIX_INSTALLTOOLS_MOUNT_TOOLS_INSTALLER             = 0x00
VIX_INSTALLTOOLS_AUTO_UPGRADE                      = 0x01
VIX_INSTALLTOOLS_RETURN_IMMEDIATELY                = 0x02

# === Exception ===
class VixException(Exception):
    """
    A exception that specifies VIX-related errors and the corresponding messages.
    """
    def __init__(self, err_code):
        """
        Constructor
        
        @param err_code: a VIX error code or a error message.
        """
        _vix.Vix_GetErrorText.restype = c_char_p
        self._err_code = err_code
        self._msg = _vix.Vix_GetErrorText(self._err_code, None)

    def __str__(self):
        return repr(self._msg)

# === Class ===
class VixHost:
    """
    A VIX host that maintains a connection to a host server.
    """
    def __init__(self):
        """
        Constructor
        """
        self.is_connected = False
        self.host_handle = VIX_INVALID_HANDLE

    def connect(self, hostname=None, hostport=0, username=None, password=None):
        """
        Connect to a host server.

        @param hostname: host name or IP address. It will be auto-transform Tool "https://<hostname/IP>/sdk".
        @param hostport: port on the remote host.
        @param username: user name for authentication on the remote host.
        @param password: password for authentication on the remote host.
        """
        self.host_handle = VIX_INVALID_HANDLE

        job_hdl = _vix.VixHost_Connect(VIX_API_VERSION,
            VIX_SERVICEPROVIDER_DEFAULT,
            'https://%s/sdk' % hostname,
            hostport,
            username,
            password,
            0,
            VIX_INVALID_HANDLE,
            None,
            None
        )

        hdl = c_int()
        err = _vix.VixJob_Wait(job_hdl,
            VIX_PROPERTY_JOB_RESULT_HANDLE,
            byref(hdl),
            VIX_PROPERTY_NONE
        )
        _vix.Vix_ReleaseHandle(job_hdl)
        if err != VIX_OK:
            raise VixException(err)

        self.is_connected = True
        self.host_handle = hdl.value

    def disconnect(self):
        """
        Disconnect from a host server.
        """
        if self.is_connected:
            _vix.VixHost_Disconnect(self.host_handle)

        self.is_connected = False
        self.host_handle = VIX_INVALID_HANDLE

class VixVM:
    """
    A Virtual Machine that is included in a host server.
    """
    def __init__(self, vixhost):
        """
        Constructor

        @param vixhost: a VIX host object which specifies the host server to which current VM belongs.
        """
        self.is_opened = False
        self._vm_handle = VIX_INVALID_HANDLE

        if not isinstance(vixhost, VixHost):
            raise TypeError('%r should be a %r object.' % (vixhost, VixHost))

        self._vixhost = vixhost

    def _exec_cmd(self, func, *args, **kwargs):
        if not self._vixhost.is_connected:
            raise VixException('Host disconnected')

        if not self.is_opened:
            raise VixException('VM has not been opened')

        if (not hasattr(func, '__call__')):
            raise TypeError('%r should be callable.' % func)

        job_hdl = func(*args, **kwargs)

        err = _vix.VixJob_Wait(job_hdl, VIX_PROPERTY_NONE)
        _vix.Vix_ReleaseHandle(job_hdl)
        if err != VIX_OK:
            raise VixException(err)

    # VM basic
    def open(self, vmpath):
        """
        Open a virtual machine.

        @param vmpath: VMX file path of the VM.
        """
        if not self._vixhost.is_connected:
            raise VixException('Host disconnected')

        if self.is_opened:
            self.close()

        if not isinstance(vmpath, basestring):
            raise TypeError('%r should be a string.', vmpath)

        job_hdl = _vix.VixVM_Open(self._vixhost.host_handle,
            vmpath,
            None,
            None
        )

        hdl = c_int()
        err = _vix.VixJob_Wait(job_hdl,
            VIX_PROPERTY_JOB_RESULT_HANDLE,
            byref(hdl),
            VIX_PROPERTY_NONE
        )
        _vix.Vix_ReleaseHandle(job_hdl)
        if err != VIX_OK:
            raise VixException(err)

        self.is_opened = True
        self._vm_handle = hdl.value

    def close(self):
        """
        Close current virtual machine.
        """
        if self.is_opened:
            self.is_opened = False
            self._vm_handle = VIX_INVALID_HANDLE

    def wait_for_tools_in_guest(self, time_sec=300):
        """
        Wait until guest is completely booted. This function should be called
        after calling any function that resets or reboots the state of the
        guest operating system.
        """

        if not isinstance(time_sec, int) or time_sec <= 0:
            raise TypeError('%r should be a positive integer.', time_sec)

        self._exec_cmd(_vix.VixVM_WaitForToolsInGuest,
            self._vm_handle,
            time_sec,
            None,
            None
        )

    def power_on(self):
        """
        Power on current virtual machine.
        """
        self._exec_cmd(_vix.VixVM_PowerOn,
            self._vm_handle,
            VIX_VMPOWEROP_NORMAL,
            VIX_INVALID_HANDLE,
            None,
            None
        )

        self.wait_for_tools_in_guest()

    def power_off(self):
        """
        Power off current virtual machine.
        """
        self._exec_cmd(_vix.VixVM_PowerOff,
            self._vm_handle,
            VIX_VMPOWEROP_NORMAL,
            None,
            None
        )

    def shutdown(self):
        """
        Shutdown current virtual machine from the guest OS.
        """
        self._exec_cmd(_vix.VixVM_PowerOff,
            self._vm_handle,
            VIX_VMPOWEROP_FROM_GUEST,
            None,
            None
        )

    def reset(self):
        """
        Power reset current virtual machine.
        """
        self._exec_cmd(_vix.VixVM_Reset,
            self._vm_handle,
            VIX_VMPOWEROP_NORMAL,
            None,
            None
        )

        self.wait_for_tools_in_guest()

    def reboot(self):
        """
        Reboot current virtual machine from the guest OS.
        """
        self._exec_cmd(_vix.VixVM_Reset,
            self._vm_handle,
            VIX_VMPOWEROP_FROM_GUEST,
            None,
            None
        )

        self.wait_for_tools_in_guest()

    def suspend(self):
        """
        Suspend current virtual machine.
        """
        self._exec_cmd(_vix.VixVM_Suspend,
            self._vm_handle,
            0,
            None,
            None
        )

    def resume(self):
        """
        Resume current virtual machine (an alias of power_on).
        """
        self.power_on()
        self.wait_for_tools_in_guest()

    def pause(self):
        """
        Pause current virtual machine.
        """
        self._exec_cmd(_vix.VixVM_Pause,
            self._vm_handle,
            0,
            VIX_INVALID_HANDLE,
            None,
            None
        )

    def unpause(self):
        """
        Unpause current virtual machine.
        """
        self._exec_cmd(_vix.VixVM_Unpause,
            self._vm_handle,
            0,
            VIX_INVALID_HANDLE,
            None,
            None
        )

    # Guest user auth
    def login(self, username, password):
        """
        Login with specified username and password to the guest OS.
        Some commands may need to login first.

        @param username: user name in the guest OS.
        @param password: password of the corresponding user.
        """
        if not isinstance(username, basestring):
            raise TypeError('%r should be a string.', username)

        if not isinstance(password, basestring):
            raise TypeError('%r should be a string.', password)

        self._exec_cmd(_vix.VixVM_LoginInGuest,
            self._vm_handle,
            username,
            password,
            0,
            None,
            None
        )

    def logout(self):
        """
        Logout from the guest OS.
        """
        self._exec_cmd(_vix.VixVM_LogoutFromGuest,
            self._vm_handle,
            None,
            None
        )

    # Guest program running
    def run_program(self, prog, args=''):
        """
        Run a program inside the guest OS.

        @param prog: program path.
        @param args: arguments for the program.
        """
        if not isinstance(prog, basestring):
            raise TypeError('%r should be a string.', prog)

        if not isinstance(args, basestring):
            raise TypeError('%r should be a string.', args)

        self._exec_cmd(_vix.VixVM_RunProgramInGuest,
            self._vm_handle,
            prog,
            args,
            0,
            VIX_INVALID_HANDLE,
            None,
            None
        )

    def open_url(self, url):
        """
        Use default browser to open a URL in the guest OS.

        @param url: URL path.
        """
        if not isinstance(url, basestring):
            raise TypeError('%r should be a string.', url)

        self._exec_cmd(_vix.VixVM_OpenUrlInGuest,
            self._vm_handle,
            url,
            0,
            VIX_INVALID_HANDLE,
            None,
            None
        )

    # Snapshot
    def create_snapshot(self, name=None, description=None):
        """
        Create a snapshot for current virtual machine.

        @param name       : a customized snapshot name.
        @param description: description for this snapshot.
        """
        self._exec_cmd(_vix.VixVM_CreateSnapshot,
            self._vm_handle,
            name,
            description,
            VIX_SNAPSHOT_INCLUDE_MEMORY,
            VIX_INVALID_HANDLE,
            None,
            None
        )

    def _get_snapshot_by_name(self, name):
        """
        Get a snapshot handle by name.

        @param name: a customized snapshot name.
        """
        hdl = c_int()
        err = _vix.VixVM_GetNamedSnapshot(self._vm_handle, name, byref(hdl))
        if err != VIX_OK:
            raise VixException(err)

        return hdl.value

    def remove_snapshot(self, name):
        """
        Remove a snapshot from the guest OS.

        @param name: a customized snapshot name.
        """
        snap_handle = self._get_snapshot_by_name(name)
        self._exec_cmd(_vix.VixVM_RemoveSnapshot,
            self._vm_handle,
            snap_handle,
            0,
            None,
            None
        )
        _vix.Vix_ReleaseHandle(snap_handle)

    def revert_to_snapshot(self, name):
        """
        Revert to a snapshot.

        @param name: a customized snapshot name.
        """
        snap_handle = self._get_snapshot_by_name(name)
        self._exec_cmd(_vix.VixVM_RevertToSnapshot,
            self._vm_handle,
            snap_handle,
            0,
            VIX_INVALID_HANDLE,
            None,
            None
        )
        _vix.Vix_ReleaseHandle(snap_handle)

        self.wait_for_tools_in_guest()

    # Property
    def get_property_type(self, prop):
        """
        Get property type for the property of current virtual machine.

        @param prop: property.
        """
        if not self._vixhost.is_connected:
            raise VixException('Host disconnected')

        if not self.is_opened:
            raise VixException('VM has not been opened')

        type = c_int()
        err = _vix.Vix_GetPropertyType(self._vm_handle, prop, byref(type))
        if err != VIX_OK:
            raise VixException(err)

        return type.value

    def get_property(self, prop):
        """
        Get property value for the property of current virtual machine.

        @param prop: property.
        """
        if not self._vixhost.is_connected:
            raise VixException('Host disconnected')

        if not self.is_opened:
            raise VixException('VM has not been opened')

        type = self.get_property_type(prop)
        propval = c_int()
        if type == VIX_PROPERTYTYPE_STRING or type == VIX_PROPERTYTYPE_BLOB:
            propval = c_char_p()

        err = _vix.Vix_GetProperties(self._vm_handle,
            prop,
            byref(propval),
            VIX_PROPERTY_NONE
        )
        if err != VIX_OK:
            raise VixException(err)

        return bool(propval.value) if type == VIX_PROPERTYTYPE_BOOL else propval.value

    # File transfer
    def send_file(self, src, dest):
        """
        Copy local file to the guest.

        @param src : the path of source file that to be sent from local machine.
        @param dest: the path of destination file that to be saved to remote guest.
        """
        if not isinstance(src, basestring):
            raise TypeError('%r should be a string.', src)

        if not isinstance(dest, basestring):
            raise TypeError('%r should be a string.', dest)

        self._exec_cmd(_vix.VixVM_CopyFileFromHostToGuest,
            self._vm_handle,
            src,
            dest,
            0,
            VIX_HANDLETYPE_NONE,
            None,
            None
        )

    def receive_file(self, src, dest):
        """
        Copy remote file from the guest to local.

        @param src : the path of source file that to be received from remote guest.
        @param dest: the path of destination file that to be saved to local machine.
        """
        if not isinstance(src, basestring):
            raise TypeError('%r should be a string.', src)

        if not isinstance(dest, basestring):
            raise TypeError('%r should be a string.', dest)

        self._exec_cmd(_vix.VixVM_CopyFileFromGuestToHost,
            self._vm_handle,
            src,
            dest,
            0,
            VIX_HANDLETYPE_NONE,
            None,
            None
        )
