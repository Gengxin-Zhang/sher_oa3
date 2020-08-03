module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  parserOptions: {
    parser: 'babel-eslint'
  },
  extends: [
    '@nuxtjs',
    'plugin:nuxt/recommended'
  ],
  plugins: [
  ],
  // add your custom rules here
  rules: {
    "indent": ["off", 2],
    "vue/max-attributes-per-line": [2, {
      "singleline": 10,
      "multiline": {
        "max": 1,
        "allowFirstLine": false
      }
    }],
    "vue/html-self-closing": ["error", {
      "html": {
        "void": "any",
        "normal": "any",
        "component": "any"
      },
      "svg": "any",
      "math": "any"
    }],
    "vue/singleline-html-element-content-newline": "off",
    'vue/no-parsing-error': [2, { "invalid-first-character-of-tag-name": false }],
    "vue/no-use-v-if-with-v-for": "off",
    "vue/multiline-html-element-content-newline": "off",
    "vue/name-property-casing": [0, "PascalCase"],
    "vue/html-closing-bracket-newline": [0, {
      "singleline": "never",
      "multiline": "always"
    }],
    "vue/no-side-effects-in-computed-properties": 0,
    'arrow-spacing': [2, {
      'before': true,
      'after': true
    }],
    'comma-dangle': [2, 'never'],
    'comma-spacing': [2, {
      'before': false,
      'after': true
    }],
    "space-before-function-paren": 0,
  }
}
