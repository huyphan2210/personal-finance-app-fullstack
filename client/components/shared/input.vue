<template>
  <div ref="field" class="field-wrapper">
    <label
      v-if="label ?? defaultLabelRecords[type]"
      class="field-wrapper_label"
      :for="INPUT_ID"
    >
      {{ label ?? defaultLabelRecords[type] }}
    </label>
    <div class="field-wrapper_input-wrapper">
      <span class="field-wrapper_input-wrapper_prefix" v-if="prefix">
        {{ prefix }}
      </span>
      <input
        ref="input"
        required
        :value="value"
        @input="customInputHandler"
        @focusin="() => field?.classList.add('focus')"
        @focusout="() => field?.classList.remove('focus')"
        @change="(e) => emits(VALUE_CHANGE_EVENT, (e.currentTarget as HTMLInputElement).value)"
        :min="minValue || 0"
        :max="maxValue"
        :maxlength="maxLength"
        :id="INPUT_ID"
        :type="typeRecords[type]"
        :placeholder="placeholder ?? defaultPlaceholderRecords[type]"
      />
    </div>
    <slot></slot>
  </div>
</template>
<script lang="ts" setup>
import type { InputTypeHTMLAttribute } from "vue";
import { InputEnumType, type IInput } from "~/interfaces/shared.interface";

const VALUE_CHANGE_EVENT = "on-value-change";
const INPUT_ID = Math.random().toString();

interface IField extends HTMLDivElement {
  isFocused: boolean;
}

const field = ref<IField>();
const input = ref<HTMLInputElement>();
const emits = defineEmits([VALUE_CHANGE_EVENT]);
const {
  type,
  label,
  placeholder,
  prefix,
  customInputHandler,
  value,
  maxLength,
  minValue,
  maxValue,
} = defineProps<IInput>();

const defaultLabelRecords: Record<InputEnumType, string> = {
  [InputEnumType.Text]: "Text",
  [InputEnumType.Email]: "Email",
  [InputEnumType.Password]: "Password",
  [InputEnumType.Number]: "Number",
  [InputEnumType.Search]: "",
};

const typeRecords: Record<InputEnumType, InputTypeHTMLAttribute> = {
  [InputEnumType.Text]: "text",
  [InputEnumType.Email]: "email",
  [InputEnumType.Password]: "password",
  [InputEnumType.Number]: "number",
  [InputEnumType.Search]: "search",
};

const defaultPlaceholderRecords: Record<InputEnumType, string> = {
  [InputEnumType.Text]: "John Doe",
  [InputEnumType.Email]: "johndoe@yopmail.com",
  [InputEnumType.Password]: "johndoedabest",
  [InputEnumType.Number]: "e.g. 2000",
  [InputEnumType.Search]: "Type somthing...",
};
</script>
<style lang="scss" scoped>
.field-wrapper {
  &_label {
    @include label-style;
  }

  &_input-wrapper {
    @include input-wrapper-style;
    display: flex;
    align-items: center;
    gap: 0.75rem;

    &_prefix {
      @include text-preset-4;
      color: var(--beige-500);
    }

    input {
      @include text-preset-4;
      border: none;
      outline: none;
      color: var(--grey-900);
      width: 100%;
      &::placeholder {
        color: var(--beige-500);
      }

      &[type="search"] {
        &::-webkit-search-decoration,
        &::-webkit-search-cancel-button,
        &::-webkit-search-results-button,
        &::-webkit-search-results-decoration {
          display: none;
        }
      }
    }
  }

  &.focus {
    .field-wrapper {
      &_label {
        color: var(--grey-900);
      }
      &_input-wrapper {
        outline: solid 1px var(--grey-900);
      }
    }
  }
}
</style>
