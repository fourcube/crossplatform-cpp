{
 'target_defaults': {
     'configurations': {
       'Debug': {
         'defines': [ 'DEBUG', '_DEBUG' ],
         'msvs_settings': {
            'VCLinkerTool': {
              'GenerateDebugInformation': 'true'
            },
          },
       },
     },
 },
'targets': [
  {
    'target_name': 'crossplatform-demo',
    'type': 'executable',
    'msvs_guid': '5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65',
    'dependencies': [
      './demolib/demolib.gyp:demolib',
    ],
    'defines': [
      #
    ],
    'include_dirs': [
      '.',
    ],
    'sources': [
      'test.cc'
    ],
    'conditions': [
      ['OS=="linux"', {
        'defines': [
          # 'LINUX_DEFINE',
        ],
        'include_dirs': [
          # 'include/linux',
        ],
      }],
      ['OS=="win"', {
        'defines': [
          # 'WINDOWS_SPECIFIC_DEFINE',
        ],
      }, { # OS != "win",
        'defines': [
          # 'NON_WINDOWS_DEFINE',
        ],
      }]
    ],
  },
],
}
