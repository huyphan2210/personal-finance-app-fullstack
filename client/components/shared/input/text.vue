<template>
  <div ref="field" class="field-wrapper">
    <label class="field-wrapper_label" :for="INPUT_ID">{{
      label ?? defaultLabelRecords[type]
    }}</label>
    <div class="field-wrapper_input-wrapper">
      <span class="field-wrapper_input-wrapper_prefix" v-if="prefix">{{
        prefix
      }}</span>
      <input
        ref="input"
        required
        @change="(e) => emits(VALUE_CHANGE_EVENT, (e.currentTarget as HTMLInputElement).value)"
        :id="INPUT_ID"
        :type="typeRecords[type]"
        :placeholder="placeholder ?? defaultPlaceholderRecords[type]"
      />
    </div>
  </div>
</template>
<script lang="ts" setup>
import type { InputTypeHTMLAttribute } from "vue";
import { InputEnumType, type IInput } from "~/interfaces/shared.interface";

const VALUE_CHANGE_EVENT = "on-value-change";
const INPUT_ID = Math.random().toString();

const field = ref<HTMLDivElement>();
const input = ref<HTMLInputElement>();
const emits = defineEmits([VALUE_CHANGE_EVENT]);
const { type, label, placeholder, prefix } = defineProps<IInput>();

const defaultLabelRecords: Record<InputEnumType, InputTypeHTMLAttribute> = {
  [InputEnumType.Text]: "Text",
  [InputEnumType.Email]: "Email",
  [InputEnumType.Password]: "Password",
  [InputEnumType.Number]: "Number",
};

const typeRecords: Record<InputEnumType, InputTypeHTMLAttribute> = {
  [InputEnumType.Text]: "text",
  [InputEnumType.Email]: "email",
  [InputEnumType.Password]: "password",
  [InputEnumType.Number]: "text",
};

const defaultPlaceholderRecords: Record<InputEnumType, string> = {
  [InputEnumType.Text]: "John Doe",
  [InputEnumType.Email]: "johndoe@yopmail.com",
  [InputEnumType.Password]: "johndoedabest",
  [InputEnumType.Number]: "e.g. 2000",
};

watch(
  () => document.activeElement,
  (value) => {
    if (value === input.value) {
      field.value?.classList.add("focus");
    }
  }
);
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
    input {
      @include text-preset-4;
      border: none;
      outline: none;
      color: var(--grey-900);
      width: 100%;
    }
    &:focus-within {
      outline: solid 1px var(--grey-900);
    }
  }
  &.focus {
    &_label {
      color: var(--grey-900);
    }
  }
}
</style>
