# This file is part of Telegram Desktop,
# the official desktop application for the Telegram messaging service.
#
# For license and copyright information please follow this link:
# https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL

{
  'conditions': [[ 'build_mac', {
    'mac_hardened_runtime': 1,
    'mac_bundle': '1',
    'mac_bundle_resources': [
      '<!@(python -c "for s in \'<@(langpacks)\'.split(\' \'): print(\'<(res_loc)/langs/\' + s + \'.lproj/Localizable.strings\')")',
      '<(DEPTH)/../Telegram/Images.xcassets',
    ],
    'xcode_settings': {
      'INFOPLIST_FILE': '../Telegram.plist',
      'CURRENT_PROJECT_VERSION': '<!(helpers/common/print_version.sh <(DEPTH)/../build/version)',
      'ASSETCATALOG_COMPILER_APPICON_NAME': 'AppIcon',
      'ENABLE_HARDENED_RUNTIME': 'YES',
      'OTHER_CODE_SIGN_FLAGS': [
        '--deep',
      ],
      'OTHER_LDFLAGS': [
        '-lbsm',
        '-lm',
        '/usr/local/lib/liblzma.a',
      ],
    },
    'include_dirs': [
      '/usr/local/include',
    ],
    'library_dirs': [
      '/usr/local/lib',
    ],
    'sources': [
      '<(DEPTH)/../Telegram/Telegram.entitlements',
    ],
    'configurations': {
      'Debug': {
        'xcode_settings': {
          'GCC_OPTIMIZATION_LEVEL': '0',
        },
      },
      'Release': {
        'xcode_settings': {
          'DEBUG_INFORMATION_FORMAT': 'dwarf-with-dsym',
          'LLVM_LTO': 'YES',
          'GCC_OPTIMIZATION_LEVEL': 'fast',
        },
      },
    },
  }], [ 'build_macold', {
    'xcode_settings': {
      'OTHER_CPLUSPLUSFLAGS': [ '-nostdinc++' ],
      'OTHER_LDFLAGS': [
        '-isysroot', '/',
        '-L/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/lib/',
        '-lbase',
        '-lcrashpad_client',
        '-lcrashpad_util',
        '/usr/local/macold/lib/libz.a',
        '/usr/local/macold/lib/libopus.a',
        '/usr/local/macold/lib/libopenal.a',
        '/usr/local/macold/lib/libiconv.a',
        '/usr/local/macold/lib/libavcodec.a',
        '/usr/local/macold/lib/libavformat.a',
        '/usr/local/macold/lib/libavutil.a',
        '/usr/local/macold/lib/libswscale.a',
        '/usr/local/macold/lib/libswresample.a',
        '/usr/local/macold/lib/libexif.a',
        '/usr/local/macold/lib/libc++.a',
        '/usr/local/macold/lib/libc++abi.a',
      ],
    },
    'include_dirs': [
      '/usr/local/macold',
      '/usr/local/macold/include/c++/v1',
      '<(libs_loc)/macold/libexif-0.6.20',
      '<(libs_loc)/macold/crashpad',
      '<(libs_loc)/macold/crashpad/third_party/mini_chromium/mini_chromium',
    ],
    'configurations': {
      'Debug': {
        'xcode_settings': {
          'PRODUCT_BUNDLE_IDENTIFIER': 'com.tdesktop.TelegramDebugOld',
        },
        'library_dirs': [
          '<(libs_loc)/macold/crashpad/out/Debug',
        ],
      },
      'Release': {
        'xcode_settings': {
          'PRODUCT_BUNDLE_IDENTIFIER': 'com.tdesktop.Telegram',
        },
        'library_dirs': [
          '<(libs_loc)/macold/crashpad/out/Release',
        ],
      },
    },
    'postbuilds': [{
      'postbuild_name': 'Force Frameworks path',
      'action': [
        'mkdir', '-p', '${BUILT_PRODUCTS_DIR}/Telegram.app/Contents/Frameworks/'
      ],
    }, {
      'postbuild_name': 'Copy Updater to Frameworks',
      'action': [
        'cp',
        '${BUILT_PRODUCTS_DIR}/Updater',
        '${BUILT_PRODUCTS_DIR}/Telegram.app/Contents/Frameworks/',
      ],
    }, {
      'postbuild_name': 'Force Helpers path',
      'action': [
        'mkdir', '-p', '${BUILT_PRODUCTS_DIR}/Telegram.app/Contents/Helpers/'
      ],
    }, {
      'postbuild_name': 'Copy crashpad_handler to Helpers',
      'action': [
        'cp',
        '<(libs_loc)/macold/crashpad/out/${CONFIGURATION}/crashpad_handler',
        '${BUILT_PRODUCTS_DIR}/Telegram.app/Contents/Helpers/',
      ],
    }],
  }, {
    'xcode_settings': {
      'OTHER_LDFLAGS': [
        '/usr/local/lib/libz.a',
        '/usr/local/lib/libopus.a',
        '/usr/local/lib/libopenal.a',
        '/usr/local/lib/libiconv.a',
        '/usr/local/lib/libavcodec.a',
        '/usr/local/lib/libavformat.a',
        '/usr/local/lib/libavutil.a',
        '/usr/local/lib/libswscale.a',
        '/usr/local/lib/libswresample.a',
      ],
    },
    'include_dirs': [
      '<(libs_loc)/crashpad',
      '<(libs_loc)/crashpad/third_party/mini_chromium/mini_chromium',
    ],
    'configurations': {
      'Debug': {
        'library_dirs': [
          '<(libs_loc)/crashpad/out/Debug',
        ],
      },
      'Release': {
        'library_dirs': [
          '<(libs_loc)/crashpad/out/Release',
        ],
      },
    },
  }], [ '"<(build_macold)" != "1" and "<(build_macstore)" != "1"', {
    'xcode_settings': {
      'OTHER_LDFLAGS': [
        '-lbase',
        '-lcrashpad_client',
        '-lcrashpad_util',
      ],
     },
    'configurations': {
      'Debug': {
        'xcode_settings': {
          'PRODUCT_BUNDLE_IDENTIFIER': 'com.tdesktop.TelegramDebug',
        },
      },
      'Release': {
        'xcode_settings': {
          'PRODUCT_BUNDLE_IDENTIFIER': 'com.tdesktop.Telegram',
        },
      },
    },
    'postbuilds': [{
      'postbuild_name': 'Force Frameworks path',
      'action': [
        'mkdir', '-p', '${BUILT_PRODUCTS_DIR}/Telegram.app/Contents/Frameworks/'
      ],
    }, {
      'postbuild_name': 'Copy Updater to Frameworks',
      'action': [
        'cp',
        '${BUILT_PRODUCTS_DIR}/Updater',
        '${BUILT_PRODUCTS_DIR}/Telegram.app/Contents/Frameworks/',
      ],
    }, {
      'postbuild_name': 'Force Helpers path',
      'action': [
        'mkdir', '-p', '${BUILT_PRODUCTS_DIR}/Telegram.app/Contents/Helpers/'
      ],
    }, {
      'postbuild_name': 'Copy crashpad_client to Helpers',
      'action': [
        'cp',
        '<(libs_loc)/crashpad/out/${CONFIGURATION}/crashpad_handler',
        '${BUILT_PRODUCTS_DIR}/Telegram.app/Contents/Helpers/',
      ],
    }],
  }], [ 'build_macstore', {
    'mac_sandbox': 1,
    'mac_sandbox_development_team': '6N38VWS5BX',
    'product_name': 'Telegram Desktop',
    'sources': [
      '<(DEPTH)/../Telegram/Telegram Desktop.entitlements',
    ],
    'xcode_settings': {
      'PRODUCT_BUNDLE_IDENTIFIER': 'org.telegram.desktop',
      'OTHER_LDFLAGS': [
        '-framework', 'Breakpad',
      ],
      'FRAMEWORK_SEARCH_PATHS': [
        '<(libs_loc)/breakpad/src/client/mac/build/Release',
      ],
    },
    'defines': [
      'TDESKTOP_DISABLE_AUTOUPDATE',
      'OS_MAC_STORE',
    ],
    'postbuilds': [{
      'postbuild_name': 'Clear Frameworks path',
      'action': [
        'rm', '-rf', '${BUILT_PRODUCTS_DIR}/Telegram Desktop.app/Contents/Frameworks'
      ],
    }, {
      'postbuild_name': 'Force Frameworks path',
      'action': [
        'mkdir', '-p', '${BUILT_PRODUCTS_DIR}/Telegram Desktop.app/Contents/Frameworks/'
      ],
    }, {
      'postbuild_name': 'Copy Breakpad.framework to Frameworks',
      'action': [
        'cp', '-a',
        '<(libs_loc)/breakpad/src/client/mac/build/Release/Breakpad.framework',
        '${BUILT_PRODUCTS_DIR}/Telegram Desktop.app/Contents/Frameworks/Breakpad.framework',
      ],
    }]
  }]],
}
