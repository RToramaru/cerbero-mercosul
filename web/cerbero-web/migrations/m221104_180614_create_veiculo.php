<?php

use yii\db\Migration;

/**
 * Class m221104_180614_create_veiculo
 */
class m221104_180614_create_veiculo extends Migration
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

        $this->addCommentOnTable('veiculo', 'Tabela de veículos');
        $this->addCommentOnColumn('veiculo', 'id', 'Identificador do veículo');
        $this->addCommentOnColumn('veiculo', 'placa', 'Placa do veículo');
        $this->addCommentOnColumn('veiculo', 'data', 'Data de cadastro do veículo');
        $this->addCommentOnColumn('veiculo', 'imagem', 'Imagem do veículo');
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
        echo "m221104_180614_create_veiculo cannot be reverted.\n";

        return false;
    }
    */
}
