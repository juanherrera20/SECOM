<template>
    <div class="input-box">
        <label class="input-label">{{ label }}</label>
        <select
        class="input select"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        :required="isRequired"
        :disabled="isDesabled"
        >
        <option v-for="opt in options" :key="opt.value" :value="opt.value">
            {{ opt.label }}
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
        type: String,
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
            default: false,
            required: false
        },
        isDesabled: {
            type: Boolean,
            default: false,
            required: false
        }
    })

    const emit = defineEmits(['update:modelValue'])
</script>

<style scoped lang="scss">
   
    .input-box {
        @include input-box;

        .input {
            @include form-field;
        }

        .input[required] {
            @include form-field($focus-color: $error_red50);
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
  