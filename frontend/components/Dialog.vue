<template>
  <div
    class="Dialog"
    :style="`min-width: ${minWidth};max-width: ${maxWidth};width: ${width};
                min-height: ${minHeight};max-height: ${maxHeight}; height:  ${height}`"
  >
  </div>
</template>

<script>
export default {
  props: {
    minWidth: {
      type: String,
      default: "10rem"
    },
    maxWidth: {
      type: String,
      default: "100%;"
    },
    width: {
      type: String,
      default: "50%;"
    },
    minHeight: {
      type: String,
      default: "0"
    },
    maxHeight: {
      type: String,
      default: "100vh"
    },
    height: {
      type: String,
      default: "auto"
    }
  }
};
</script>

<style lang="scss" scoped>
.Dialog {
  position: fixed;
}
</style>