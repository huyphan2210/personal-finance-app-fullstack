<template>
  <div class="input">
    <label class="input_label" :for="uuid">Email</label>
    <input
      required
      v-model="value"
      :id="uuid"
      :type="typeRecords[type]"
      placeholder="johndoe@yopmail.com"
    />
  </div>
</template>
<script lang="ts" setup>
import { randomUUID } from "crypto";
import type { InputTypeHTMLAttribute } from "vue";
import { InputEnumType, type IInput } from "~/interfaces/shared.interface";
const uuid = randomUUID();
const value = ref<string>();
const { type } = defineProps<IInput>();

const typeRecords: Record<InputEnumType, InputTypeHTMLAttribute> = {
  [InputEnumType.Text]: "text",
  [InputEnumType.Email]: "email",
  [InputEnumType.Password]: "password",
};
</script>
<style lang="scss"></style>
