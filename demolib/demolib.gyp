{
  "target_defaults": {
    "configurations": {
      "Debug": {
        "defines": [
          "DEBUG",
          "_DEBUG"
        ]
      }
    }
  },
  "targets": [
    {
      "target_name": "demolib",
      "type": "static_library",
      "msvs_guid": "5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65",
      "dependencies": [],
      "defines": [
        "DEFINE_DEMOLIB"
      ],
      "include_dirs": [
        "."
      ],
      "direct_dependent_settings": {
        "defines": [
          "DEFINE_DEMOLIB"
        ],
        "linkflags": []
      },
      "export_dependent_settings": [],
      "sources": [
        "demolib.cc"
      ]
    },
    {
      "target_name": "demolib_test",
      "type": "static_library",
      "msvs_guid": "5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65",
      "dependencies": [
        "./demolib.gyp:demolib"
      ],
      "defines": [
        "DEFINE_DEMOLIB_TEST"
      ],
      "include_dirs": [
        "."
      ],
      "export_dependent_settings": [
        "./demolib.gyp:demolib"
      ],
      "direct_dependent_settings": {
        "defines": [
          "DEFINE_DEMOLIB_TEST"
        ]
      },
      "sources": [
        "demolib_test.cc"
      ]
    },
    {
      "target_name": "demolib_test_bin",
      "type": "executable",
      "msvs_guid": "5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65",
      "dependencies": [
        "./demolib.gyp:demolib"
      ],
      "sources": [
        "demolib_test.cc"
      ]
    }
  ]
}
