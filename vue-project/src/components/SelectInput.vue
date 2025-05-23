<template>
  <div class="input-box">
    <label class="input-label">{{ label }}</label>
    <select
      class="input select"
      :value="modelValue"
      @change="onChange"
      :required="isRequired"
      :disabled="isDesabled"
    >
      <option disabled value="">Selecciona una opción</option>
      <option v-for="opt in options" :key="opt.id" :value="opt.id">
        {{ opt.name }}
      </option>
    </select>
    <span class="input-helper">{{ extra }}</span>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  options: {
    type: Array,
    required: true
  },
  modelValue: {
    type: [String, Number],
    required: false
  },
  label: {
    type: String,
    required: true
  },
  extra: {
    type: String,
    default: 'Seleccionar una opción válida'
  },
  isRequired: {
    type: Boolean,
    default: false
  },
  isDesabled: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue'])

function onChange(event) {
  const intVal = parseInt(event.target.value)
  emit('update:modelValue', intVal)
}
</script>

<style scoped lang="scss">
     .input-box {
        @include input-box;

        .input[required] {
            @include form-field($focus-color: $error_red50);
        }

        .input {
            @include form-field;
        }
        .input[disabled] {
            @include form-field($focus-color: $third_color100);
        }

        .select {
            @include form-field;
            appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg fill='gray' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 0.5rem center;
            background-size: 1rem;
            padding-right: 2rem;
            cursor: pointer;
        }
    }
</style>
  