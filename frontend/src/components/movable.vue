<template>
  <component
    :is="tag"
    :move-disabled="disabled"
    :style="position"
    class="--movable-base"
    v-movable="moveArgs"
  >
    <slot />
  </component>
</template>

<script></script>
