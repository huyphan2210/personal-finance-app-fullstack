<template>
  <table class="transactions_table">
    <colgroup>
      <col style="width: 50%" />
      <col style="width: 20%" />
      <col style="width: 15%" />
      <col style="width: 15" />
    </colgroup>
    <thead class="transactions_table_head">
      <tr>
        <th>Recipient / Sender</th>
        <th>Category</th>
        <th>Transaction Date</th>
        <th>Amount</th>
      </tr>
    </thead>
    <tbody class="transactions_table_body">
      <tr class="transactions_table_body_item" v-for="item in data">
        <td class="transactions_table_body_item_name">
          <figure>
            <img :src="item.avatarUrl" loading="lazy" :alt="item.name" />
            <figcaption>
              <span>{{ item.name }}</span>
              <span>{{ item.category }}</span>
            </figcaption>
          </figure>
        </td>
        <td class="transactions_table_body_item_category">
          {{ item.category }}
        </td>
        <td class="transactions_table_body_item_date">
          {{ transformDate(item.transactionDate) }}
        </td>
        <td class="transactions_table_body_item_amount">
          <span
            :class="{
              'positive-amount': item.amount > 0,
            }"
            >{{ enUSFormatter.format(item.amount) }}</span
          >
          <span>{{ transformDate(item.transactionDate) }}</span>
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script lang="ts" setup>
import { type ITransactionsTable } from "~/interfaces/transactions.interface";

const { data } = defineProps<ITransactionsTable>();

const enUSFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
  signDisplay: "always",
});

const transformDate = (dateString: string) => {
  const date: Date = new Date(dateString);
  return date.toLocaleString("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
};
</script>
<style lang="scss" scoped>
.transactions {
  &_table {
    margin-bottom: 1.5rem;

    &.is-loading {
      flex: 1;
    }

    colgroup {
      display: none;
    }

    table-layout: fixed;
    width: 100%;

    th,
    td {
      text-align: start;
      color: var(--grey-500);
      padding-block: 1rem;
      border-bottom: solid 1px var(--grey-100);
      @include text-preset-5;

      &:last-child {
        text-align: end;
      }

      &:not(:last-child):not(:first-child) {
        display: none;
      }
    }

    &_head {
      display: none;
    }

    &_body {
      &_item {
        &:first-child {
          td {
            padding-top: 0;
          }
        }
        &:last-child {
          td {
            padding-bottom: 0;
            border-bottom: none;
          }
        }
        &_name {
          figure {
            display: flex;
            align-items: center;
            gap: 5.5px;

            img {
              width: 100%;
              max-width: 2rem;
              border-radius: 50%;
            }

            figcaption {
              span {
                display: block;

                &:first-child {
                  color: var(--grey-900);
                  margin-bottom: 0.25rem;
                  @include text-preset-4-bold;
                }
              }
            }
          }
        }

        &_amount {
          span {
            display: block;

            &:first-child {
              color: var(--grey-900);
              margin-bottom: 0.25rem;
              @include text-preset-4-bold;

              &.positive-amount {
                color: var(--green);
              }
            }
          }
        }
      }
    }
  }
}

@media screen and (min-width: 48rem) {
  .transactions {
    &_table {
      colgroup {
        display: table-column-group;
      }
      th,
      td {
        text-align: start;
        color: var(--grey-500);
        border-bottom: solid 1px var(--grey-100);
        @include text-preset-5;

        &:not(:last-child):not(:first-child) {
          display: table-cell;
        }
      }

      th {
        padding-block: 21px;
      }

      td {
        padding-block: 1rem;
      }

      &_head {
        display: table-header-group;
      }

      &_body {
        &_item {
          &:first-child {
            td {
              padding-top: 1.5rem;
            }
          }

          &_name {
            figure {
              gap: 9.5px;
              img {
                max-width: 2.5rem;
              }

              figcaption {
                span {
                  display: none;
                  &:first-child {
                    display: unset;
                    margin-bottom: 0;
                  }
                }
              }
            }
          }

          &_amount {
            span {
              display: none;
              &:first-child {
                display: unset;
                margin-bottom: 0;
              }
            }
          }
        }
      }
    }
  }
}

@media screen and (min-width: 90rem) {
  .transactions {
    &_table {
      th,
      td {
        &:first-child {
          padding-left: 1rem;
        }
      }

      th {
        padding-block: 0.75rem;
      }
    }
  }
}
</style>
