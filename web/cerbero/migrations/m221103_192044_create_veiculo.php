<?php

use yii\db\Migration;

/**
 * Class m221103_192044_create_veiculo
 */
class m221103_192044_create_veiculo extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->createTable('veiculo', [
            'id' => $this->primaryKey(),
            'placa' => $this->text()->notNull(),
            'data' => $this->date()->notNull(),
            'imagem' => $this->text()->notNull(),
        ]);
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        $this->dropTable('veiculo');
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m221103_192044_create_veiculo cannot be reverted.\n";

        return false;
    }
    */
}
