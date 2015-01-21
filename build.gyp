{
  "targets": [
    {
      "configurations": {
        "Debug": {        
          "msvs_settings": {
            "VCLinkerTool": {
              "GenerateDebugInformation": "true"
            }
          }
        }
      },
      "target_name": "crossplatform-demo",
      "type": "executable",
      "msvs_guid": "5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65",
      "dependencies": [
        "./demolib/demolib.gyp:demolib"
      ],
      "defines": [],
      "include_dirs": [
        "."
      ],
      "sources": [
        "crossplatform-demo.cc"
      ],
      "conditions": [
        [
          "OS==\"linux\"",
          {
            "defines": [],
            "include_dirs": []
          }
        ],
        [
          "OS==\"win\"",
          {
            "defines": []
          },
          {
            "defines": []
          }
        ]
      ]
    },
    {
      "target_name": "crossplatform-demo-test",
      "type": "executable",
      "msvs_guid": "5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65",
      "dependencies": [
        "./demolib/demolib.gyp:demolib_test",
        "./demolib/demolib.gyp:demolib_test_bin"
      ],
      "defines": [],
      "include_dirs": [
        "."
      ],
      "sources": [
        "crossplatform-demo-test.cc"
      ]
    }
  ]
}
